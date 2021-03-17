''' MENU 

    [1] - Cadastrar novo contato
    [2] - Ver Contatos
    [3] - Deletar Contato
    [4] - Editar Contato
    [5] - Sair '''
from plotly import graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))

import dash
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure = fig)
])
app.run_server(debug = True)