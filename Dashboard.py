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

# แสดงข้อมูลในตาราง
st.write(df.head(10))

# แสดงข้อมูลในแผนภูมิ
fig = px.line(df, x="ปี", y="ยอดขาย", color="ภูมิภาค")
st.plotly_chart(fig)

# แสดงตัวเลือกเพิ่มเติม
options = ["เอเชีย", "ยุโรป", "อเมริกา"]
region = st.selectbox("ภูมิภาคที่คุณต้องการดูข้อมูลยอดขาย", options)
st.write("ยอดขายประจำปีของภูมิภาค", region, "คือ", df[df["ภูมิภาค"] == region]["ยอดขาย"].sum())