import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
import base64

dash.register_page(__name__, path='/', title="UFABC_da")


layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(html.Img(src="assets/logo.png")),
                # html.H1("UFABC_da"),
                html.P(["""Ao fazer o upload você declara estar de acordo com o uso dos seus
                          dados para ..."""]),
            ]
        ),

        dbc.Container(
            [
                dcc.Upload(
                    html.A(["Arraste o arquivo ou faça o upload."], style={"cursor": "pointer"}),
                    style={
                        "width": "100%",
                        "height": "60px",
                        "lineHeight": "60px",
                        "borderWidth": "1px",
                        "borderStyle": "dashed",
                        "borderRadius": "5px",
                        "textAlign": "center",
                        "margin": "10px",
                        }, 
                        multiple=False,
                        accept="application/json",
                        id="user_data"),


                html.Br(),

                dbc.Row(
                    [
                        ## Op1 
                        # dbc.Col(dbc.Button("Home", href="/", color="dark", className="d-grid col-6 mx-auto")),
                        # dbc.Col(dbc.Button("Performance", href="/performance", color="dark", className="d-grid col-6 mx-auto")),
                        # dbc.Col(dbc.Button("Predições", href="/predicoes", color="dark", className="d-grid col-6 mx-auto"))
                        
                        ## Op2
                        dbc.ButtonGroup(
                            [
                                dbc.Button("Home", href="/", color="dark"),
                                dbc.Button("Performance", href="/performance", color="dark"),
                                dbc.Button("Predições", href="/predicoes", color="dark")
                            ]
                        )

                    ], align="center", justify="center"
                ),
            ],
        ),

        html.Div(None, id="null")
    ]
)

@dash.callback(
    Output("null", "children"),
    Input("user_data", "contents")
)
def save_data(user_data):
    if user_data is not None:
        data = user_data.encode("utf8").split(b";base64,")[1]

        with open('./tmp/teste.json', 'wb') as file:
            file.write(base64.decodebytes(data))
        
