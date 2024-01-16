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

st.bar_chart(df2,x="species", y=["body_mass_g"], color=["#FF0000", "#0000FF"])