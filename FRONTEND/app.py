import streamlit as st
import pandas as pd
df = pd.read_csv("E:\datascience-assignment\Cleaned_data.csv")
st.title("Trader Performance Dashboard")
sentiment = st.selectbox("Select Sentiment", df['classification'].unique())
filtered = df[df['classification'] == sentiment]
st.write("Average PnL:", filtered['PnL'].mean())
st.write("Win Rate:", filtered['win_rate'].mean())
st.write("Trades:", filtered['num_trades'].mean())