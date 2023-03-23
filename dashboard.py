import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app_path = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(app_path, os.path.join("data", "spp_data_2.csv")))


app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

x = 'Date-Hour(NMT)'

theme = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Solar power production - Radiation, System Production, Sunshine'),
                ],
            ),
        ],
    )


def build_graph_1():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df[x][:100],
                    'y': df['Radiation'][:100],
                    'name': 'Radiation',
                    'marker': {'size': 12}
                },
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],   
                'font': {
                    'color': theme['text']
                }
            }
            
        },
        style={
    'display': 'inline-block',
    'vertical-align': 'top',
    'width': '33%',
        }
    )


def build_graph_2():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df[x][:100],
                    'y': df['SystemProduction'][:100],
                    'name': 'System Production',
                    'marker': {'size': 12}
                }
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                }
            }
        },
        style={
    'display': 'inline-block',
    'vertical-align': 'top',
    'width': '33%',
        }
    )

def build_graph_3():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df[x][:100],
                    'y': df['Sunshine'][:100],
                    'name': 'Sunshine',
                    'marker': {'size': 12}
                }
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                }
            }
        },
        style={
    'display': 'inline-block',
    'vertical-align': 'top',
    'width': '33%',
        }
    )

app.layout = html.Div(
    className='big-app-container',
    children=[
        build_banner(),
        html.Div(
            className='app-container',
            children=[
                build_graph_1(),
                build_graph_2(),
                build_graph_3()
            ]
        )
    ]
)