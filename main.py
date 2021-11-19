import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import os
import glob

def readCSVs(csv_files):
    dfs = []

    for csv in csv_files:
        df = pd.read_csv(csv)
        df["Crypto_name"] = csv.split("\\")[-1].split(".")[0]
        dfs.append(df)

    return pd.concat(dfs).drop(columns=["Currency_Name"])


app = dash.Dash(__name__)

path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "archive", "*.csv"))

df = readCSVs(csv_files)
# print(df)

if __name__ == "__main__":
    app.run_server(debug=True)
