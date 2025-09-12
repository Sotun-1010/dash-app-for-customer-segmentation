import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('df_filtered.csv')


columns = df.columns.drop(["Unnamed: 0", "Cluster"]).tolist()

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1('3D Scatter plot of Customer Data from cluster analysis'),
    
    html.Div([
        # Dropdown for the X-axis
        html.Label("X-axis:"),
        dcc.Dropdown(
            id='x-axis-dropdown',
            options=[{'label': i, 'value': i} for i in columns],
            value="Age",  
            clearable=False
        ),
        # Dropdown for the Y-axis
        html.Label("Y-axis:"),
        dcc.Dropdown(
            id='y-axis-dropdown',
            options=[{'label': i, 'value': i} for i in columns],
            value="Income",
            clearable=False
        ),
        # Dropdown for the Z-axis
        html.Label("Z-axis:"),
        dcc.Dropdown(
            id='z-axis-dropdown',
            options=[{'label': i, 'value': i} for i in columns],
            value="Sex",
            clearable=False
        )
    ], style={'width': '50%', 'display': 'inline-block'}),

    # 3D scatter plot graph component
    dcc.Graph(id='3d-scatter-plot'),
    html.P("Cluster 0: The Young Professionals, Cluster 1: The Urban Achievers, Cluster 2: The Established Elite, Cluster 3: The Emerging Segment")
])

# 4. Create a Callback to Update the Plot
# This function is triggered whenever the value of any dropdown changes
@app.callback(
    Output('3d-scatter-plot', 'figure'),
    [Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value'),
     Input('z-axis-dropdown', 'value')]
)

def update_graph(x_col, y_col, z_col):
    """
    Updates the 3D scatter plot based on the selected columns.
    """
    fig = px.scatter_3d(
        df,
        x=x_col,
        y=y_col,
        z=z_col,
        color='Cluster',
        title=f'3D Scatter Plot of {x_col} vs {y_col} vs {z_col}'
    )
    return fig

# 5. Run the app
if __name__ == '__main__':
    app.run(debug=True)