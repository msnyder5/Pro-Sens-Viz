import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
from bs4 import BeautifulSoup


def get_table():
    url = "https://prosettings.net/lists/apex-legends/"
    response = requests.get(
        url,
        headers={
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
        },
    )
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", id="pro-list-table")
        df = pd.read_html(str(table))[0]
        return df
    else:
        print(f"Failed to retrieve data: Status Code {response.status_code}")
        return None


def visualize(df):
    # Calculate eDPI
    df["eDPI"] = df["DPI"] * df["Sens"]

    # Visualization 1: Scatterplot of DPI vs Sens
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="DPI", y="Sens")
    plt.title("Scatterplot of DPI vs Sens")
    plt.xlabel("DPI")
    plt.ylabel("Sensitivity (Sens)")
    plt.xticks(range(0, int(df["DPI"].max()) + 400, 400))
    plt.grid(True)
    plt.show()

    df["eDPI"] = df["DPI"] * df["Sens"]
    df = df[df["eDPI"] <= 4_000]
    # Visualization 2: Distribution of eDPI
    plt.figure(figsize=(10, 6))
    sns.histplot(df["eDPI"], kde=True)
    plt.title("Apex Pro eDPI Distribution")
    plt.xlabel("eDPI")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()


def main():
    df = get_table()
    if df is not None:
        visualize(df)


if __name__ == "__main__":
    main()
