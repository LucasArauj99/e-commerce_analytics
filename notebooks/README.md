# 📘 Resumo dos Notebooks

A seguir, estão descritos os objetivos e principais tarefas realizadas em cada notebook deste projeto.

## 📊 01_exploration.ipynb — Análise Exploratória Inicial

- Leitura e junção dos principais datasets da Olist.
- Verificação de tipos de dados, valores ausentes e estatísticas descritivas.
- Análise de variáveis categóricas e numéricas (status do pedido, tipo de pagamento, notas, preços, frete, etc).
- Análise temporal de compras por dia, mês e ano.
- Identificação de outliers e correlação entre variáveis numéricas.

---

## 🧼 02_cleaning.ipynb — Limpeza e Pré-processamento

- Junção e consolidação dos principais datasets.
- Tratamento de valores ausentes e remoção de outliers.
- Conversão de tipos de dados (ex: datas, categorias, numéricos).
- Criação de colunas auxiliares (ex: tempo de entrega, atraso na entrega).
- Salvamento dos dados tratados na pasta data/processed.

---

## 💰 03_sales_analysis.ipynb — Análise de Vendas

- Faturamento total e médio por pedido.
- Produtos mais vendidos por quantidade.
- Produtos com maior receita gerada.
- Sazonalidade de vendas ao longo dos meses.
- Análise de faturamento por categoria de produto.
- Visualizações com Seaborn e Matplotlib.

---

## 👥 04_customers.ipynb — Análise de Clientes

- Quantidade de clientes por estado e cidade.
- Análise geográfica com mapas interativos (Datashader + Holoviews).
- Proporção de clientes únicos e recorrentes.
- Distribuição do número de pedidos por cliente.
- Correlação entre atrasos na entrega e notas de avaliação.
- Top 15 clientes que mais e menos gastaram.
- Clientes com maior valor médio por pedido.
- Formas de pagamento mais utilizadas.
- Avaliações por categoria de produto.
- Análise de correlação entre variáveis numéricas (preço, frete, dimensões, etc).

---

## 🚚 05_logistics.ipynb — Análise Logística

- Conversão e tratamento de colunas de data (entrega, aprovação, envio, estimativa).
- Cálculo e visualização da distribuição dos dias de atraso nas entregas.
- Comparação entre o tempo médio geral de entrega e o atraso médio dos pedidos atrasados.
- Cálculo do tempo de entrega real (da coleta pela transportadora até a entrega).
- Agrupamento por prefixo de CEP (3 dígitos) para análise regional.
- Geração de mapa interativo mostrando o tempo médio de entrega por região.
- Exportação do mapa como imagem com coloração baseada na duração da entrega.

---

