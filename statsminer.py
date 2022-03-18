
from bs4 import BeautifulSoup
import requests
import re
import json
import pandas as pd
pd.set_option("max_rows", None)


def get_financials_html(ticker):
    url1 = 'http://financials.morningstar.com/finan/financials/getFinancePart.html?&callback=xxx&t=' + ticker
    soup1 = BeautifulSoup(json.loads(re.findall(r'xxx\((.*)\)', requests.get(url1).text)[0])['componentData'], 'lxml')
    return soup1

def get_keystats_html(ticker):
    url2 = 'http://financials.morningstar.com/finan/financials/getKeyStatPart.html?&callback=xxx&t=' + ticker
    soup2 = BeautifulSoup(json.loads(re.findall(r'xxx\((.*)\)', requests.get(url2).text)[0])['componentData'], 'lxml')
    return soup2

def make_dataframes(soup1, soup2):
    df = pd.read_html(soup1.prettify())
    tables = pd.read_html(soup2.prettify())

    df0 = df[0].dropna()
    df1 = tables[0].dropna()
    df2 = tables[1].dropna()
    df3 = tables[2].dropna()
    df4 = tables[3].dropna()
    df5 = tables[4].dropna()
    df6 = tables[5].dropna()
    df7 = tables[6].dropna()


    for i in range(7):
        print(eval('df' + str(i)).to_string())
   


 # dict = {}
 #    for i in range(7:
 #      dict['df' + str(i)] = tables.shift(i).add_suffix('_df' + str(i))
ticker = input("Enter Stock Ticker: ").upper()
make_dataframes(get_keystats_html(ticker), get_keystats_html(ticker))