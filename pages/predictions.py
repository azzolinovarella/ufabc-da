import dash
import dash_bootstrap_components as dbc
from dash import html, dcc 

dash.register_page(__name__, path='/predicoes', title="Performance")


layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(html.H1("Essa é a página de predições")),
                dbc.Row(html.P("Algum texto diferente mas ainda SUPER tosco por aqui"))
            ]
       )
    ]
)