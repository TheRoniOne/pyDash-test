import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import os, glob
from functions import readCSVs, get_cryptos


app = dash.Dash(__name__)

path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "archive", "*.csv"))

df = readCSVs(csv_files)

app.layout = html.Div([
    html.H1("Crypto tendency exploration with Dash in Python", style={'text-align': 'center'}),

    dcc.Dropdown(
        id="slct_crypto",
        options=get_cryptos(df),
        multi=False,
        value=df["Crypto_name"].unique()[0],
        style={"width": "40%"}
    ),

    html.Div(id="output_container", children=[]),
    html.Br(),

    dcc.Graph(id="crypto_graph", figure={})

])

@app.callback(
    [Output(component_id="output_container", component_property="children"),
     Output(component_id="crypto_graph", component_property="figure")],
    [Input(component_id="slct_crypto", component_property="value")]
)
def update_graph(option_slctd):
    container = f"Showing historic prices of {option_slctd}"

    temp = df
    temp = temp[temp["Crypto_name"] == option_slctd]
    temp.sort_values(by=["Date"])

    fig = px.line(
        data_frame=temp,
        x="Date",
        y="value",
        color="var",
    )

    return container, fig

if __name__ == "__main__":
    app.run_server(debug=True)
