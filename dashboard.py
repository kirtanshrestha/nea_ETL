import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

DB_USER = "postgres"
DB_PASS = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "NEA"
TABLE_NAME = "electricity_consumption"


engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

@st.cache_data
def load_data():
    query = f"SELECT * FROM {TABLE_NAME}"
    return pd.read_sql(query, engine)

df = load_data()
df["date"] = pd.to_datetime(df["date"])

st.title("⚡ Nepal Electricity Consumption Dashboard")
st.markdown("Data for learning — showing 3 months of daily consumption across provinces.")

provinces = df["province"].unique()
selected_province = st.selectbox("Select Province", sorted(provinces))

province_df = df[df["province"] == selected_province]

fig1 = px.line(
    province_df,
    x="date",
    y="consumption_mwh",
    title=f"Daily Electricity Consumption in {selected_province}",
    markers=True,
)
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(
    province_df,
    x="date",
    y="consumption_change_%",
    title=f"Daily % Change in Consumption — {selected_province}",
    markers=True,
)
st.plotly_chart(fig2, use_container_width=True)

avg_outages = df.groupby("province")["outages"].mean().reset_index()
fig3 = px.bar(
    avg_outages,
    x="province",
    y="outages",
    title="Average Daily Outages per Province",
)
st.plotly_chart(fig3, use_container_width=True)

st.subheader("📊 Summary Stats")
st.dataframe(
    df.groupby("province")
      .agg({"consumption_mwh": "mean", "peak_load_mw": "mean", "outages": "sum"})
      .round(2)
      .reset_index()
)
