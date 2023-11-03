from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd 
  
data = [['tom', 10], ['nick', 15], ['juli', 14]] 
  
df = pd.DataFrame(data, columns=['Name', 'Age']) 

def render(app: Dash) -> html.Div:
    return html.Div(
        children = [
            dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
        ]
    )