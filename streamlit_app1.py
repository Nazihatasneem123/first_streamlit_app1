import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header ('Breakfast Menu')
streamlit.text ('Omega 3 & Blueberry Oatmeal')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
# pre populate the list  
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
 
#reading from api --> normalizing it --> displaying it in the data frame/table format

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())   #just writes the data from the api into the streamlit app 
#fruityvice_normalize = pandas.json_normalize(fruityvice_response.json()) #normalizes the json data
#streamlit.dataframe(fruityvice_normalize)  #outputs the data in the table

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests 
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalize = pandas.json_normalize(fruityvice_response.json()) #normalizes the selected data 
#streamlit.dataframe(fruityvice_response)  
streamlit.text(fruityvice_response.json()) 
streamlit.dataframe(fruityvice_normalize)  #outputs the data in the table


#inorder to include snowflake libarary (snowflake connector python) - create a file requirements.txt and add the line snowflake-connector-python
#go to streamlip app - settings -- secretes and then give user id password 
#[snowflake]
#user = "naztastrialaccount2024A1"
#password = "Computerpwd23@"
#account = "PEFHZIV-XM23150" 
#warehouse = "pc_rivery_wh" 
#database = "pc_rivery_db" 
#schema = "public"
#role = "AccountAdmin"

#streamlit.stop()
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('The user entered ', add_my_fruit)
my_cnx1 = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur1 = my_cnx1.cursor()
my_cur1.execute("insert into fruit_load_list values ('add_my_fruit')")
streamlit.write("Done")
