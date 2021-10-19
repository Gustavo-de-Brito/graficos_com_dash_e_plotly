import pandas as pd
import plotly.graph_objects as go

dados = pd.read_csv("01-aula_dash/frutas.csv", sep=";")

dados_array = dados.values

frutas = []

for dado in dados_array:
    frutas.append(dado[0])


# Função que irá filtrar a quantida de kg de cada fruta no mês especificado
def filtra_meses(mes):
    vendas = []

    if "jan" == mes or "Janeiro" == mes:
        index = 1
    elif "fev" == mes or "Fevereiro" == mes:
        index = 2
    elif "mar" == mes or "Março" == mes:
        index = 3
    elif "abr" == mes or "Abril" == mes:
        index = 4
    
    for dado in dados_array:
        vendas.append(dado[index])

    return vendas

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import Input, Output


# Importação de um css externo
css = ["https://bootswatch.com/4/darkly/bootstrap.css"]

# listas com Labels e Values para o filtro
meses = ["Janeiro", "Fevereiro", "Março", "Abril"]
meses_abreviados = ["jan", "fev", "mar", "abr"]

opcoes = []

# Criação do dicionário com label e value para ser usado no filtro
for mes, abreviacao in zip(meses, meses_abreviados):
    opcoes.append({"label" : mes, "value": abreviacao})

pag = dash.Dash(
    __name__,
    external_stylesheets=css # CSS exterior é importado para dentro da página
)

pag.layout = html.Div([
    html.Div("Vendas por mês", style={"font-size":"30px", "text-align":"center"},className="card-header"),
    html.Div([
        html.Div(
            dcc.Dropdown(
                id = "dropdown",
                options= opcoes,
                value= "jan",
                clearable= False,
                style={"width":"400px", "border-radius":"10px", "border":" 1px solid white", "font-weight":"bold"}
        ), className="nav-item dropdown"),
        html.Div(
            dcc.Graph(id = "grafico", style={"margin-top": "20px"})
        )],className="card-body"
    ),
], className="card text-white bg-primary mb-3")


'''

# Versão mais "extensa" do uso do callback

@pag.callback(
    Output(component_id="grafico", component_property="figure"),
    Input(component_id="dropdown", component_property="value")
)

'''

# Versão mais resumida do uso do callback
@pag.callback(
    Output("grafico", "figure"),
    Input("dropdown", "value")
)

def gera_grafico(mes):

    vendas = filtra_meses(mes)
    
    grafico = go.Figure(
        go.Bar(
            x = frutas,
            y = vendas
        )
    )

    grafico.update_layout(
        xaxis = dict(
            tickfont = dict(
                color = "white"
            )
        ),
        yaxis = dict(
            tickfont = dict(
                color = "white"
            )
        ),
        plot_bgcolor = "#444",
        paper_bgcolor = "#375a7f"
    )

    return grafico

if __name__ == "__main__":
    pag.run_server(use_reloader = False, debug = True)