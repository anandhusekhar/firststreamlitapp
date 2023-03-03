#created new python file
import streamlit
import pandas as pd
streamlit.title('hello')
streamlit.header('Hi, Noobie 🐔')
streamlit.text('🥣Welcome to the world of programming')
df=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
list1=df.set_index('Fruit')
fruits_selected=streamlit.multiselect("pick some fruits:", list(list1.index))
fruits_to_show=df.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)



