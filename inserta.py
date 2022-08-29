import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
