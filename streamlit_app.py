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
col2.metric("# of Columns", trades_to_show.shape[1], "0")
col3.metric("Total Gain / Loss", trades_to_show['Amount'].sum(), "0")

#ideas
st.header('Holdings as of Today')

my_holdings_list = pd.read_csv("Portfolio_Positions_Jul-16-2022.csv") 

my_holdings_list = my_holdings_list.set_index('Symbol')
holdings_selected = st.multiselect("Pick some trades:", list(my_holdings_list.index.drop_duplicates()))
holdings_to_show = my_holdings_list.loc[trades_selected]
st.dataframe(holdings_to_show)

"""Add holdings list as well. Let users search through it too. 
Use it to calc how much you've made on a given security. Basically current amounts - amount in trading data frame

Manage state better so it doesn't change every time you change your selection."""


