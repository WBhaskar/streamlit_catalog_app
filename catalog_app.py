import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Dress Catalog')
try:
  dress_choice = streamlit.text_input('What dress will you like to view?')
  if not dress_choice:
     streamlit.error("Please select a dress to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
