import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error  import URLError

streamlit.title('My Moms New Healthy Diner')


streamlit.header('Breakfast Menu')
streamlit.text('🥣  Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) 
# setting default
fruits_to_show = my_fruit_list.loc[fruits_selected]
#Display the table on the page
streamlit.dataframe(fruits_to_show)
#dataframe shows only selected fruit

streamlit.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = streamlit.text_input('What fruit would you like more information about?')
    if not fruit_choice:
        Streamlit.error("please select a fruit to get information.")
    else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit" + fruity_choice)
        fruityvice_normalized = pandas.json_normalized(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)
        
     



  



# streamlit.header('Fruityvice Fruit Advice!')
# try:
#     fruit_choice = streamlit.text_input('What fruit would you like information about?')
#    if not fruit_choice:
#         streamlit.error("Please select a fruit to get information.")
#     else:
#         back_from_function = get_fruityvice_data(fruity_choice)
#         streamlit.dataframe(back_from_function)

     
except URLError as e:
   streamlit.error()
    
  #streamlit.write('The user entered ', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) #just writes th data to the screen

#take the json version of the response and normalize it

#output it to the screen as a table

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)




   
 #streamlit.stop()      

#fruit_choice = streamlit.text_input('What fruit would you like toadd?','jackfruit')

#streamlit.write('Thanks for adding ',add_my_fruit)
#streamlit.text('Thanks for adding jackfruit')

add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")




##my_fruit_list = my_fruit_list.set_index('Fruit')


#fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
#streamlit.dataframe(fruits_to_show)
