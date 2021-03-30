import plotly.graph_objects as go

# dados dos meses para ser colocados no no eixo X
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
# porcentagens para serem colocadas no eixo Y
produto_a = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
produto_b = [12.5, 54.6, 58.9, 98.0, 73.1, 81.4, 95.5, 112.6, 25.7, 98.6, 45.1, 29.3]

# opções para o filtro
opcoes = ["Produto A", "Produto B"]
nomes_maior_menor_50 = ["Maior que 50%", "Menor que 50%", "Total"]
valor_de_maior_menor_50 = [">50", "<50", "total"]

import dash
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown( #Configurações de filtro dropdown
        id = "filtro",
        options = [{'label': nome, 'value':nome} for nome in opcoes], #Atribuição de nomes e valores para o filtro, respectivamente
        value = "Produto A", # Filtro inicial a ser exibido no gráfico
        clearable = False
    ),
    dcc.RadioItems( #Configurações de filtro dropdown
        id = "filtro_2",
        options = [{'label': nome, 'value':valor} for nome, valor in zip(nomes_maior_menor_50, valor_de_maior_menor_50)], #Atribuição de nomes e valores para o filtro, respectivamente
        value = "total", # Filtro inicial a ser exibido no gráfico
    ),
    dcc.Graph(id = "grafico"), #Identificação para o gráfico
])

# Função que fara a separação dos valores de acordo com o filtro
def separa_dados(nome, valor):
    porcentagens_filtradas = []
    meses_filtrados = []
    if nome == "Produto A":
        y = produto_a
    elif nome == "Produto B":
        y = produto_b
    if valor == ">50":
        for porcentagem, data in zip(y, mes):
            if porcentagem >= 50:
                porcentagens_filtradas.append(porcentagem)
                meses_filtrados.append(data)
    elif valor == "<50":
        for porcentagem, data in zip(y, mes):
            if porcentagem <= 50:
                porcentagens_filtradas.append(porcentagem)
                meses_filtrados.append(data)
    elif valor == "total":
        porcentagens_filtradas = y
        meses_filtrados = mes
    return [porcentagens_filtradas, meses_filtrados]

@app.callback(
    Output(component_id='grafico', component_property= 'figure'), # Define-se o id de saída e seu tipo
    Input(component_id='filtro', component_property='value'), # Definine-se o id do filtro e seu tipo
    Input(component_id='filtro_2', component_property='value') # Definine-se o id do filtro e seu tipo
)

def grafico_1(argumento, maior_menor): # Os comandos que geram o gráfico serão colocados em uma função que receberá um dos valores definidos no filtro, no nosso exemplo "Produto A" ou "Produto B"
    print(argumento)
    print(maior_menor)
    dados_filtrados = separa_dados(argumento, maior_menor) # O argumento escolhido ("Produto A" ou "Produtro B") é colocado como parâmetro para a filtragem de dados pela função separa dados
    eixo_x = dados_filtrados[1]
    eixo_y = dados_filtrados[0]
    print(eixo_x)
    # criação de uma lista chamada "linha1" que será a primeira linha do gráfico
    linha1 = go.Scatter( # todos os dados dentro do comando go.Scatter() receberão uma série de informações para gerar linha
        x = eixo_x,
        y = eixo_y,
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
        plot_bgcolor = "snow", #cor do background refente ao container
    )
    return grafico

if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = False)