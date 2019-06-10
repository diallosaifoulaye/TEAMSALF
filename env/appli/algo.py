import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.offline as py
import plotly.figure_factory as ff




df = pd.read_csv("/home/diallo/Documents/EDACY_workspace/Git/Projects/DATA-SCIENCE/bd.csv")
app = dash.Dash()
app.layout = html.Div(children=[
    html.Div(children='''
        TEST
    '''),
dcc.Graph(
    id='example',
    figure ={
        'data' : [
            {'x':df.Anne, 'y':df.Carburant, 'type':'bar', 'name':'VOITURE'},
        ],
        'layout': {
            'title':'VOITURE'
            
        }}
)
])
'''
data = [go.Scatter(
x=df.Anne,
y=df['Carburant'])]
layout = {
'title': 'Suivi Consommation',
'yaxis': {'title': 'Consommation'}
}
fig = dict(data=data, layout=layout)

py.plot(fig)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={''backgroundColor'': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [8, 5, 12,2,6,5,0], 'type': 'hist', 'name': 'Talent 1'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'hist', 'name': 'Talent 2'},
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'hist', 'name': 'Talent 3'},

            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
             }
        }
    )
])
'''
if __name__ == '__main__':
    app.run_server(debug=True)