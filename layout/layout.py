import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

layout = html.Div(
    [
        dbc.NavbarSimple(
            [   
                ## Op1
                # dbc.NavItem(dbc.NavLink("Perfomance", href="/performance")),
                # dbc.NavItem(dbc.NavLink("Predições", href="/predicoes"))
                
                ## Op2
                dbc.DropdownMenu(
                    [
                        dbc.DropdownMenuItem("Opções", header=True),
                        dbc.DropdownMenuItem("Performance", href="/performance"),
                        dbc.DropdownMenuItem("Predições", href="/predicoes")
                    ],
                    nav=True,   ## Prefiro sem
                    in_navbar=True,
                    label="Opções",
                    # style={'font-weight': 'bold'}
                ),
                dbc.NavLink("Github", href="https://github.com/azzolinovarella/ufabc-da")
            ],
            brand="UFABC_da",
            brand_href="/",
            color="primary",
            dark=True
        ),
        
        dash.page_container
    ]
)