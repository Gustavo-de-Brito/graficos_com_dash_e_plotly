import plotly.graph_objects as go

# dados dos meses para ser colocados no no eixo X
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
# porcentagens para serem colocadas no eixo Y
high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]

# criação de uma lista chamada "linha1" que será a primeira linha do gráfico
linha1 = go.Scatter( # todos os dados dentro do comando go.Scatter() receberão uma série de informações para gerar linha
    x = mes,
    y = high_2000,
    mode = "lines",
)

grafico = go.Figure(linha1) # tranforma a lista("linha1") em uma Figure

x = 4**(1/2)
print(x)

import dash
import dash_core_components as dcc 
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure = grafico),
])
app.run_server(debug = True, use_reloader = False)