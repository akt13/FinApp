from dash import Dash, html, dcc
from . import expense, stockTable


def create_layout(app: Dash) -> html.Div:
    return html.Div([
        dcc.Tabs([
            dcc.Tab(label='Overview', children=[
                html.H6("Page with overview infos")
            ]),
            dcc.Tab(label='Investment Summary', children=[
                html.H6(
                    "Page with details of NPS, PPF, MF, Stocks, SGB etc details ")
            ]),
            dcc.Tab(label='Stocks', children=[                
                    stockTable.render(app)
            ]),
            dcc.Tab(label='Expense Tracker', children=[
                expense.render(app)
            ]),
            dcc.Tab(label='Taxes', children=[
                html.H6("Page with income tax info")
            ]),
        ]),
    ])
