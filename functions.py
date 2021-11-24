import pandas as pd
import os, glob

def readCSVs(csv_files):
    dfs = []

    for csv in csv_files:
        df = pd.read_csv(csv)
        df["Crypto_name"] = os.path.split(csv)[1].split(".")[0]
        dfs.append(df)

    return pd.concat(dfs).drop(columns=["Currency_Name"])

def get_cryptos(df):
    cryptos = []

    for crypto in df["Crypto_name"].unique():
        cryptos.append({"label": crypto, "value": crypto})

    return cryptos

def main():
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(path, "archive", "*.csv"))

    df = readCSVs(csv_files)
    #df2 = df.groupby("Crypto_name")
    #print(df[:3])
    
    cryptos = get_cryptos(df)
    print(cryptos)
    #print(df["Crypto_name"].unique())

if __name__ == "__main__":
    main()
