from dash import Dash, Input, State, Output
from layout.layout import layout
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.MINTY])

app.layout = layout  # Alfa

if __name__ == '__main__':
    app.run(port=5000, debug=True)
