import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:123456@localhost:5432/postgres")

st.title("Dashboard IoT")

df = pd.read_sql("SELECT * FROM avg_temp_por_dispositivo", engine)

fig = px.bar(df, x="device_id", y="avg_temp")

st.plotly_chart(fig)
