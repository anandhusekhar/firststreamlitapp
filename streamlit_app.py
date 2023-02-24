#created new python file
import streamlit
import pandas as pd
streamlit.title('hello')
streamlit.header('Hi, Noobie 🐔')
streamlit.text('🥣Welcome to the world of programming')
df=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(df)


