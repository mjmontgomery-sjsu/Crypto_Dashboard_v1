#Cryptocurrency Dashboard

import streamlit as st
import pandas as pd
import datetime
import plotly.graph_objects as go

from PIL import Image

st.write("""
# Cryptocurency Dashboard Application
Visually show data on crypto (BTC, ETH & DOGE) from **'2019-06-18' to '2021-06-17'**
""")

image = Image.open("/Users/michaelmontgomery/Documents/Programming/Projects/Crypto Dashboard/image2.jpg")
st.image(image, use_column_width=True)

st.sidebar.header("User Input")

def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-01-01")
    end_date = st.sidebar.text_input("End Date","2020-08-01")
    crypto_symbol = st.sidebar.text_input("Crypto Symbol (BTC, ETH or DOGE)", "BTC")
    return start_date, end_date, crypto_symbol

def get_crypto_name(symbol):
    symbol = symbol.upper()
    if symbol == "BTC":
        return "Bitcoin"
    elif symbol == "ETH":
        return "Ethereum"
    elif symbol == "DOGE":
        return "Dogecoin"
    else:
        return "None"

def get_data(symbol,start,end):
    symbol = symbol.upper()
    if symbol == "BTC":
        df = pd.read_csv("/Users/michaelmontgomery/Documents/Programming/Projects/Crypto Dashboard/Cryptocurrencies/BTC.csv")
    elif symbol == "ETH":
        df = pd.read_csv("/Users/michaelmontgomery/Documents/Programming/Projects/Crypto Dashboard/Cryptocurrencies/ETH.csv")
    elif symbol == "DOGE":
        df = pd.read_csv("/Users/michaelmontgomery/Documents/Programming/Projects/Crypto Dashboard/Cryptocurrencies/DOGE.csv")
    else:
        df = pd.DataFrame(columns=['Date', 'Close','Open','Volume','Adj Close'])

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.loc[start:end]


start, end, symbol = get_input()

df = get_data(symbol, start, end)
crypto_name = get_crypto_name(symbol)

fig = go.Figure(
    data = [go.Candlestick(
    x = df.index,
    open = df['Open'],
    high = df['High'],
    low = df['Low'],
    close = df['Close'],
    increasing_line_color = 'green',
    decreasing_line_color = 'red'
    )
    ]
)

st.header(crypto_name+" Data")
st.write(df)

st.header(crypto_name+ " Data Statistics")
st.write(df.describe())

st.header(crypto_name+ " Close Price")
st.line_chart(df['Close'])

st.header(crypto_name+ " Volume")
st.bar_chart(df['Volume'])

st.header(crypto_name+ " Candle stick")
st.plotly_chart(fig)
