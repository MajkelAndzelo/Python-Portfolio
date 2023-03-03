import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date

st.write('''
# Simple Stock Price App
Shown are the stock closing price and volume of Google
''')

tickerSymbol = st.text_input("Enter ticker symbol:  (Like TSLA etc.)")
tickerData = yf.Ticker(str(tickerSymbol))
start = st.text_input("Enter start date(yyyy-mm-dd): ")
end = st.text_input("Enter end date(yyyy-mm-dd or 'today'): ")
if end == 'today':
    end = date.today()

try:
    tickerDf = tickerData.history(period='1d', start=start, end=end)
    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
except ValueError:
    st.error("Error: Invalid input. Please enter valid start and end dates in the format 'yyyy-mm-dd'.")
