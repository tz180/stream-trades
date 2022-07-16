#Creating personal streamlit app

import streamlit as st
import pandas as pd
import requests
from urllib.error import URLError

st.title('My Trades')

st.header('Complete List w/ Filter')

my_trade_list = pd.read_csv("Accounts_History_TZ.csv")

#symbol = my_trade_list['Symbol']
#symbol_choice = st.sidebar.selectbox('Select which security:', symbol)

#years = my_trade_list["Run Date"].loc[my_trade_list["Symbol"] == symbol_choice]
#year_choice = st.sidebar.selectbox('', years)

count_row = my_trade_list.shape[0]  # Gives number of rows
count_col = my_trade_list.shape[1]  # Gives number of columns


action_type = st.radio(
     "What type of trades do you want to view",
     ('All', 'Buy', 'Sell', 'Dividend'))

if action_type == 'All':
    my_trade_list = my_trade_list
elif action_type == 'Buy':
    my_trade_list = my_trade_list.loc[my_trade_list['Action'].str.contains("BOUGHT")]
elif action_type == 'Sell':
    my_trade_list = my_trade_list.loc[my_trade_list['Action'].str.contains("SOLD")]
else:
    my_trade_list = my_trade_list.loc[my_trade_list['Action'].str.contains("DIVIDEND")]

my_trade_list = my_trade_list.set_index('Symbol')

# Let's put a pick list here so they can pick the fruit they want to include 
trades_selected = st.multiselect("Pick some trades:", list(my_trade_list.index.drop_duplicates()))
trades_to_show = my_trade_list.loc[trades_selected]

# Display the table on the page.
st.dataframe(trades_to_show)

col1, col2, col3 = st.columns(3)

col1.metric("# of Trades", trades_to_show.shape[0], "0")
col2.metric("Total Gain / Loss", trades_to_show.loc['Amount'].sum(), "0")



