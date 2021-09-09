import plotly.graph_objects as go

'''

# ---------------- Exemplo Gráfico de linhas dados no código ---------------------
frutas = ["Maçã", "Banana", "Melancia", "Tomate", "Goiaba"]
quantidade_frutas = [32, 153, 52, 134, 54]


linha1 = go.Scatter(
    x = frutas,
    y = quantidade_frutas
)

grafico = go.Figure(linha1)

# grafico.show()

import dash
import dash_core_components as dcc
import dash_html_components as html

pag = dash.Dash()

pag.layout = html.Div([
    html.H1("Quantidade em Estoque"),
    html.Br(),
    dcc.Graph(figure = grafico)
])

pag.run_server(use_reloader = False, debug = True)
'''

# grafico.show()

# ------------ Exemplo Gráfico de linhas dados .csv ----------------
'''

import pandas as pd

dados = pd.read_csv("plotly/frutas.csv", sep=";")
# print(dados)

dados_array = dados.values
# print(dados_array)

frutas = []
quantidade_frutras = []
preco_frutas_kg = []

for linha in dados_array:
    frutas.append(linha[0])
    quantidade_frutras.append(linha[1])
    preco_frutas_kg.append(linha[2])

#print(frutas)
# frutas = dados_array[:, 0]
# print(frutas)
#quantidade_frutras = dados_array[:, 1]
#preco_frutas_kg = dados_array[:, 2]


linha1 = go.Scatter(
    x = frutas,
    y = quantidade_frutras,
    name = "Quantidade",
    mode = 'lines', #É definido o tipo do gráfico
    line = dict(color = '#676E78'), #Atribuido uma cor para a linha 'Domésticas'
    hovertemplate = '%{y} unidades'.center(8) + '<br>'  + '%{x}' #São utilizados o as informações de Y e de X para vizualização do dado
)

barra1 = go.Bar(
    x = frutas,
    y = preco_frutas_kg
)

grafico = go.Figure(linha1)
grafico_barra = go.Figure(barra1)

grafico.update_layout( #Deifição das configurações de layout
        xaxis_title =dict( #Adição de um título que deixará mais claro que tipo de informação será exibida no eixo X
            text = "<b>Frutas<b>", #Texto que será exibido, colocado em negrito para maior destaque por meio do comando "<b><b>", da linguagem html
            font = dict( #São atribuídas algumas propriedades para o texto
                family = 'Arial', #A fonte do texto
                color = 'white', #A cor do texto
                size = 16 #Tamanho do texto em pixels
            )
        ),
        xaxis = dict( #São atribuídas propriedades para o eixo X e para seus dados
            rangeslider=dict(visible=True), #Um filtro do próprio Plotly
            showline = True, #Mostrar a linha do Eixo X
            tickmode = "linear", #É atribuído 'linear' no tipo de 'tick' para que se possa definir um valor incial para a exibição dos valores em X(tick0) e um passo(dtick)
            showgrid = False, #Não mostrar a grade de linhas do eixo X,
            tickfont = dict(color = "white"),
            linecolor = 'rgb(63, 64, 63)', #Cor da linha do eixo X
            linewidth = 4, #Espessura da linha do eixo X
            ticks = 'outside' #Adição de "traços" do lado de fora do gráfico para melhor vizualização dos dados
        ),
        yaxis = dict( #Atribuição de propriedades para o eixo Y e seus respectivos dados
            gridcolor = 'rgb(63, 64, 63)', #Definição da cor da grade de linhas do eixo Y
            linewidth = 4,
            tickfont = dict(color = "white"),
            zeroline = False, #Para que a linha zero do eixo Y se mostre é atribuido "False" ao comando "zeroline"
            linecolor = "rgb(63, 64, 63)", #É atrbuído uma cor a linha do eixo Y
            showticklabels = True #É dado o comando para não mostrar a legenda padrão do Plotly
        ),
        margin = dict( #Configurações com relação as margens do gráfico
            t = 50, #Distância do gráfico do topo da página em pixels
            l = 100 #Distância do gráfico da lateral esquerda em pixels
        ),
        height = 580, #Altura do gráfico em pixels
        plot_bgcolor = '#D5E4F7', #Definição de cor do background do gráfico,
        paper_bgcolor = "#04387D",
        hoverlabel = dict( #Atrubuição das propriedades para o HOVER
            bgcolor = '#3F3F3F', #Cor do background do HOVER
            align = 'auto', #Alinhamento do texto do hover automático
            font = dict( #Configurações para o texto do hover
                family = 'Arial', #Fonte do texto
                size = 16, #Tamanho do texto em pixels
                color = 'white' #Cor do texto
            )
        )
)

import dash
import dash_core_components as dcc
import dash_html_components as html

pag = dash.Dash()

pag.layout = html.Div([
    html.H1("Quantidade em Estoque"),
    html.Br(),
    dcc.Graph(figure = grafico),

    html.Br(),
    html.Br(),

    html.H1("Preço por kg"),
    html.Br(),
    dcc.Graph(figure = grafico_barra)
])

pag.run_server(use_reloader = False, debug = True)
'''
'''
'''

# ------------------ Gráfico Sunburst com arquivo .csv -----------------------------
import pandas as pd

dados = pd.read_csv("plotly/frutas_verduras.csv", sep=";")

dados_formatados = dados.values

# print(dados_formatados)

frutas_verduras = []
quantidade_estoque = []
preco = []

for linha in dados_formatados:
    frutas_verduras.append(linha[0])
    quantidade_estoque.append(linha[1])
    preco.append(linha[2])

# print(frutas_verduras)

del frutas_verduras[5]
del quantidade_estoque[5]
del preco[5]

frutas = frutas_verduras[0:5]
qtd_frutas = quantidade_estoque[0:5]
preco_kg = preco[0:5]

#print(frutas)

verduras = frutas_verduras[5:]
qtd_verduras = quantidade_estoque[5:]
preco_unidade = preco[5:]

#print(verduras)
porcentagem_verdura = [75, 15, 10]

labels = ["Feira","Frutas", "Verduras"] + frutas + verduras
parents = [""] + ["Feira"] * 2 + ["Frutas"] * len(frutas) + ["Verduras"] * len(verduras)
values = [0] * 3 + preco_kg + preco_unidade


grafico = go.Figure(go.Sunburst(
    labels = ["Feira","Frutas", "Verduras"] + frutas + verduras,
    parents = [""] + ["Feira"] * 2 + ["Frutas"] * len(frutas) + ["Verduras"] * len(verduras),
    values = [0] * 3 + preco_kg + porcentagem_verdura
))

grafico.update_layout(height = 700)

import dash
import dash_core_components as dcc
import dash_html_components as html

pag = dash.Dash()

pag.layout = html.Div([
    html.H1("Preco por kg"),
    html.Br(),
    dcc.Graph(figure = grafico)
])

pag.run_server(use_reloader = False, debug = True)
'''

'''