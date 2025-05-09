import pandas as pd
import holoviews as hv
import geoviews as gv
import datashader as ds
from colorcet import fire, rainbow, bgy, bjy, bkr, kb, kr
from datashader.colors import colormap_select, Greys9
from holoviews.streams import RangeXY
from holoviews.operation.datashader import datashade, dynspread, rasterize
from bokeh.io import push_notebook, show, output_notebook
from functools import partial
from datashader.utils import export_image
from IPython.display import HTML, display
from datashader import transfer_functions as tf

class Map:
    def __init__(self):
        output_notebook()
        hv.extension('bokeh')

        #%opts Overlay [width=800 height=600 toolbar='above' xaxis=None yaxis=None]
        #%opts QuadMesh [tools=['hover'] colorbar=True] (alpha=0 hover_alpha=0.2)

        self.T = 0.05
        self.PX = 1
        self.background = "black"
        self.cm = partial(colormap_select, reverse=(self.background!="black"))
        self.export = partial(export_image, background = self.background, export_path="export")
        #self.display(HTML("<style>.container { width:100% !important; }</style>"))
        self.W = 700 
    def plot_map(self, data, label, agg_data, agg_name, cmap): 
        url="http://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{Z}/{Y}/{X}.png"
        geomap = gv.WMTS(url)
        points = hv.Points(gv.Dataset(data, kdims=['x', 'y'], vdims=[agg_name]))
        agg = datashade(points, element_type=gv.Image, aggregator=agg_data, cmap=cmap)
        zip_codes = dynspread(agg, threshold=self.T, max_px=self.PX)
        hover = hv.util.Dynamic(rasterize(points, aggregator=agg_data, width=50, height=25, streams=[RangeXY]), operation=hv.QuadMesh)
        hover = hover.options(cmap=cmap, tools=['hover'], colorbar=True, alpha=0, hover_alpha=0.2)
        img = geomap * zip_codes * hover
        img = img.relabel(label)
        return img

    def create_map(self, data, cmap, data_agg, export_name='img'):
        #self.background = "black"
        #self.cm = partial(colormap_select, reverse=(self.background!="black"))
        #self.export = partial(export_image, background = self.background, export_path="export")
        display(HTML("<style>.container { width:100% !important; }</style>"))
        #self.W = 700 
        pad = (data.x.max() - data.x.min())/50
        x_range, y_range = ((data.x.min() - pad, data.x.max() + pad), 
                             (data.y.min() - pad, data.y.max() + pad))

        ratio = (y_range[1] - y_range[0]) / (x_range[1] - x_range[0])

        plot_width  = int(self.W)
        plot_height = int(plot_width * ratio)
        if ratio > 1.5:
            plot_height = 550
            plot_width = int(plot_height / ratio)
        
        cvs = ds.Canvas(plot_width=plot_width, plot_height=plot_height, x_range=x_range, y_range=y_range)

        agg = cvs.points(data, 'x', 'y', data_agg)
        img = tf.shade(agg, cmap=cmap, how='eq_hist')
        return self.export(img, export_name)