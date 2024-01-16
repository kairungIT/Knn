import streamlit as st
import pandas as pd
import plotly.express as px

# กำหนดข้อมูล
df = pd.DataFrame({
    "ปี": [2022, 2023, 2024],
    "ยอดขาย": [100, 200, 300],
    "ภูมิภาค": ["เอเชีย", "ยุโรป", "อเมริกา"]
})

# สร้างแดชบอร์ด
st.title("ยอดขายประจำปี")

st.header("Header")
st.subheader('Raw data')

# แสดงข้อมูลในตาราง
st.write(df.head(10))

