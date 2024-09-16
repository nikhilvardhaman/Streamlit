import streamlit as st
import yfinance as yf
import datetime

ticker_symbol = st.text_input("Stock Name", "AAPL")
# start_date = st.date_input("start date", datetime.date(2019, 1, 6))
# end_date = st.date_input("end_date", datetime.date(2024, 1, 6))

# data = yf.download(ticker_symbol, start = start_date, end = end_date)

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("start date", value=datetime.date(2019, 1, 6))

with col2:
    end_date = st.date_input("end_date", value=datetime.date(2024, 1, 6))

data = yf.download(ticker_symbol, start = start_date, end = end_date)

st.write(data)