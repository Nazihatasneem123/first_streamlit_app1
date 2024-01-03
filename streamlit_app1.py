import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header ('Breakfats Menu')
streamlit.text ('Omega 3 & Blueberry Oatmeal')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
/* pre populate the list */
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),'Avocado','Strawberries')
streamlit.dataframe(my_fruit_list)
