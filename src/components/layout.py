from dash import Dash, html
from . import expense

def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Div(
                className = "text_Box",
                children = [expense.render(app)]
            )             
        ]
    )