from dash import Dash
import dash_html_components as html

app_layout = html.Div(children=[html.H1(children="Hello Dash"), ])


def init_dash(server):
    dash_app = Dash(server=server, routes_pathname_prefix="/demo/",)
    dash_app.layout = app_layout
    return dash_app.server
