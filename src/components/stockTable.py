from dash import Dash, html, dcc, Input, Output, dash_table, State
import pandas as pd 
import pymongo
from . import createMongo

collection =  createMongo.mongoCreate()

def render(app: Dash) -> html.Div:

    @app.callback(Output('mongo-datatable', component_property='children'),
                  Output('sum_PnL', component_property='children'),
                Input('interval_db', component_property='n_intervals')
                )
    def populate_datatable(n_intervals):
        # Convert the Collection (table) date to a pandas DataFrame
        df = pd.DataFrame(list(collection.find()))
        # Convert id from ObjectId to string so it can be read by DataTable
        df['_id'] = df['_id'].astype(str)
        df['Quantity'] = df['Quantity'].astype(int)
        df['Avg_Price'] = df['Avg_Price'].astype(int)
        df['LTP'] = df['LTP'].astype(int)
        df['Hold_Value'] = df['Quantity'] * df['Avg_Price']
        df['Current_Value'] = df['Quantity'] * df['LTP']
        df['P&L'] = df['Current_Value'] * df['Hold_Value']
        df['P&L %'] = df['P&L'] / df['Hold_Value']
        # print(df.head(20))

        total_PnL = df['P&L'].sum()

        return [
            dash_table.DataTable(
                id='our-table',
                data=df.to_dict('records'),
                columns=[{'id': p, 'name': p, 'editable': True} if p == '_id'
                        else {'id': p, 'name': p, 'editable': True}
                        for p in df],
            ),
            total_PnL,
        ]
    
    
    # store the row id and column id of the cell that was updated
    app.clientside_callback(
        """
        function (input,oldinput) {
            if (oldinput != null) {
                if(JSON.stringify(input) != JSON.stringify(oldinput)) {
                    for (i in Object.keys(input)) {
                        newArray = Object.values(input[i])
                        oldArray = Object.values(oldinput[i])
                        if (JSON.stringify(newArray) != JSON.stringify(oldArray)) {
                            entNew = Object.entries(input[i])
                            entOld = Object.entries(oldinput[i])
                            for (const j in entNew) {
                                if (entNew[j][1] != entOld[j][1]) {
                                    changeRef = [i, entNew[j][0]] 
                                    break        
                                }
                            }
                        }
                    }
                }
                return changeRef
            }
        }    
        """,
        Output('changed-cell', 'data'),
        Input('our-table', 'data'),
        State('our-table', 'data_previous')
    )

    #Add new row to datatable
    @app.callback(
        Output('our-table', 'data'),
        [Input('adding-rows-btn', 'n_clicks')],
        [State('our-table', 'data'),
        State('our-table', 'columns')],
    )
    def add_row(n_clicks, rows, columns):
        if n_clicks > 0:
            rows.append({c['id']: '' for c in columns})
        return rows

    # Save new DataTable data to the Mongo database ***************************
    @app.callback(
        Output("placeholder", "children"),
        Input("save-it", "n_clicks"),
        State("our-table", "data"),
        prevent_initial_call=True
    )
    def save_data(n_clicks, data):
        dff = pd.DataFrame(data)
        collection.delete_many({})
        collection.insert_many(dff.to_dict('records'))
        return ""
    
    return html.Div(
        children = [
            html.Div([
                    html.H1('Stocks in Portfolio', style={'textAlign': 'center'}),
                    # interval activated once/week or when page refreshed
                    dcc.Interval(id='interval_db', interval=86400000 * 7, n_intervals=0),
                    html.Div(id='mongo-datatable', children=[]),
                    html.Button('Add Row', id='adding-rows-btn', n_clicks=0),
                    html.Button("Save", id="save-it"),
                    dcc.Store(id='changed-cell'),
                    html.Div(id="placeholder"),
                    html.Div(id="sum_PnL"),
                ]
            )
        ]
    )