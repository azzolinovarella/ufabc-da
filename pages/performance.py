import dash
import dash_bootstrap_components as dbc
from dash import html, dcc 

dash.register_page(__name__, path='/performance', title="UFABC_da - Performance")


layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(html.H1("Essa é a página de performance")),
                dbc.Row(html.P("Algum texto diferente mas ainda tosco por aqui"))
            ]
        )
    ]
)