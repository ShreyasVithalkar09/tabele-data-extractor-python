from dotenv import load_dotenv
import pandas as pd
from bs4 import BeautifulSoup
import requests
import os


load_dotenv()

url = os.environ.get("WEBSITE_URL")
res = requests.get(url)


soup = BeautifulSoup(res.text, "lxml")

table = soup.find("table", class_ = "table table-bordered")

# get table headers
headers =  table.find_all("th")

titles = []

for i in headers:
    titles.append(i.text)

df = pd.DataFrame(columns=titles)

# get rows
rows = table.find_all("tr")
for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    l = len(df)
    df.loc[l] = row

df.to_csv("output.csv", index=False)


