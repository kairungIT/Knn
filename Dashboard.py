import streamlit as st
import pandas as pd

# สร้างแดชบอร์ด
st.title("ทดสอบการใช้งาน Streamlit")

st.header("Header")
st.subheader('Raw data')

# แสดงความ
st.write("testing")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

df = pd.read_csv(url)
st.write(df.head(10))
st.write(df.shape)

df2 = df.groupby('species')['body_mass_g'].mean()
df3=df2.T
st.write(df2)
st.write(df3.head())
st.bar_chart(df2)

genre = st.radio(
     "คุณชอบหนังแบบไหน",
     ('ตลก', 'เศร้า', 'สารคดี'))

st.write(f"หนังที่คุณชอบ คือ {genre}")

# select
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

# Multi select
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)