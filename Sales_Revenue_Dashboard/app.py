import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Title
st.title("📊 Sales & Revenue Analysis Dashboard")

# Load data
df = pd.read_csv("sales_data.csv")

# Convert columns
df["Date"] = pd.to_datetime(df["Date"])
df["Quantity"] = pd.to_numeric(df["Quantity"])
df["Revenue"] = pd.to_numeric(df["Revenue"])
df["Profit"] = pd.to_numeric(df["Profit"])

# Sidebar filters
st.sidebar.header("Filters")

selected_region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

selected_city = st.sidebar.multiselect(
    "Select City",
    df["City"].unique(),
    default=df["City"].unique()
)

# Filter data
filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Category"].isin(selected_category)) &
    (df["City"].isin(selected_city))
]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", int(filtered_df["Quantity"].sum()))
col2.metric("Total Revenue", f"₹{filtered_df['Revenue'].sum():,.0f}")
col3.metric("Total Profit", f"₹{filtered_df['Profit'].sum():,.0f}")
col4.metric("Total Orders", len(filtered_df))

# Top Products
st.subheader("Top Performing Products")

product_sales = filtered_df.groupby("Product")["Revenue"].sum().reset_index()

fig1 = px.bar(
    product_sales,
    x="Product",
    y="Revenue",
    color="Revenue"
)

st.plotly_chart(fig1, use_container_width=True)

# Category-wise Revenue
st.subheader("Category-wise Revenue")

fig2 = px.pie(
    filtered_df,
    names="Category",
    values="Revenue"
)

st.plotly_chart(fig2, use_container_width=True)

# Region-wise Revenue
st.subheader("Region-wise Revenue")

region_sales = filtered_df.groupby("Region")["Revenue"].sum().reset_index()

fig3 = px.bar(
    region_sales,
    x="Region",
    y="Revenue",
    color="Region"
)

st.plotly_chart(fig3, use_container_width=True)

# Payment Method Analysis
st.subheader("Payment Method Analysis")

payment_sales = filtered_df.groupby("Payment_Method")["Revenue"].sum().reset_index()

fig4 = px.bar(
    payment_sales,
    x="Payment_Method",
    y="Revenue",
    color="Payment_Method"
)

st.plotly_chart(fig4, use_container_width=True)

# Order Status Analysis
st.subheader("Order Status")

fig5 = px.pie(
    filtered_df,
    names="Order_Status"
)

st.plotly_chart(fig5, use_container_width=True)

# Data Table
st.subheader("Sales Data")
st.dataframe(filtered_df)