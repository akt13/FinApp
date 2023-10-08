from dash import Dash, html, dcc, Input, Output

def render(app: Dash) -> html.Div:
    return html.Div(
        children = [
            html.H6("Total Income"),
            dcc.Dropdown(
                ["Food","Subscriptions","Fuel","Shopping"],
                placeholder="Select a category",
                ),
            html.H6("Total expense"),
            dcc.Textarea(
                id='textarea-example',
                value='Enter total expense here',
                style={'width': '100%', 'height': 50},
                ),
            html.Button('Submit', id='textarea-state-example-button', n_clicks=0),
            html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
        ]
    )