#Creating personal streamlit app

import streamlit
import pandas
import requests
from urllib.error import URLError

streamlit.title('My Trades')

streamlit.header('Complete List w/ Filter')

my_trade_list = pandas.read_csv('/Users/tylerzon/Documents/Accounts_History_TZ.csv')

my_trade_list = my_trade_list.set_index('Symbol')


# Let's put a pick list here so they can pick the fruit they want to include 
trades_selected = streamlit.multiselect("Pick some trades:", list(my_trade_list.index), ['FAGIX'])
trades_to_show = my_trade_list.loc[trades_selected]

# Display the table on the page.
streamlit.dataframe(trades_to_show)
