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

grafico.update_layout( #Usa-se esse comando para modificar o layout de forma mais "separada"
    title = dict( #Utiliza-se "title" pra adicionar um título e dict(), para adicionar mais de uma característica ao title
        text = "Título do Gráfico", #Uma das "características" de title, é o texto que será exibido
        font = dict( #"font" também possui mais de um atributo, assim, também usa-se o dict()
            family = "Arial",
            size = 45,
            color = "black"),
        xref = "paper", # paper é a área refente ao fundo do gráfico (cinza/slategray)
        yref = "container", # container é a uma área em que o gráfico está contido (branco/snow)
        x = 0.5, #posição do elemento com relação ao eixo X, na área escolhida no "xref"
        y = 0.9 #posição do elemento com relação ao eixo Y, na área escolhida no "yref"
    ),
    paper_bgcolor = "slategray", #cor do background refente ao paper
    plot_bgcolor = 'snow' #cor do background refente ao container
)

import dash
import dash_core_components as dcc 
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure = grafico),
])
app.run_server(debug = True, use_reloader = False)