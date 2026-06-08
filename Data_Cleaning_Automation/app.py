import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Data Cleaning Dashboard",
    layout="wide"
)

st.title("🧹 Data Cleaning & Reporting Dashboard")

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Employees", len(df))
col2.metric("Average Salary", f"₹{df['Salary'].mean():,.0f}")
col3.metric("Departments", df["Department"].nunique())

# Department Analysis
st.subheader("Department Distribution")

fig1 = px.pie(
    df,
    names="Department",
    title="Employees by Department"
)

st.plotly_chart(fig1, use_container_width=True)

# Salary Analysis
st.subheader("Salary Analysis")

fig2 = px.bar(
    df,
    x="Employee_Name",
    y="Salary",
    color="Department"
)

st.plotly_chart(fig2, use_container_width=True)

# Performance Analysis
st.subheader("Performance Rating")

fig3 = px.scatter(
    df,
    x="Experience",
    y="Performance_Rating",
    color="Department",
    size="Salary"
)

st.plotly_chart(fig3, use_container_width=True)

# Dataset Table
st.subheader("Cleaned Dataset")

st.dataframe(df)