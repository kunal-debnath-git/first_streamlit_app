import streamlit
streamlit.title('My Parents New Healthy Diner')

import snowflake.connector


streamlit.header('Breakfast Favourites')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

import requests
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)



streamlit.header("The Fruit load list component")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row = get_fruit_load_list()
  streamlit.dataframe(my_data_row)
  

#streamlit.stop()

import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    streamlit.text(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
  
except URLError as e:
  streamlit.error()


def get_fruitvice_data(this_fruit_choice):
    fruityvice_response_two = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized_two = pandas.json_normalize(fruityvice_response_two.json())
    return fruityvice_normalized_two

streamlit.header("Fruityvice Fruit Advice!...2")
try:
  fruit_choice_two = streamlit.text_input('What fruit would you like information about?..2')
  if not fruit_choice_two:
    streamlit.error("Please select a fruit to get information...2")
  else:
    back_from_function = get_fruitvice_data(fruit_choice_two)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()




streamlit.text('*End*')
