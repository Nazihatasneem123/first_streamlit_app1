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
