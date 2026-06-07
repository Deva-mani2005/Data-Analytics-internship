import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

st.title("Customer Segmentation Dashboard")

# Load data
df = pd.read_csv("customer_data.csv")

# Features
X = df[['Annual_Income', 'Spending_Score']]

# KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Show table
st.subheader("Customer Data")
st.dataframe(df)

# Scatter Plot
fig = px.scatter(
    df,
    x='Annual_Income',
    y='Spending_Score',
    color='Cluster',
    hover_data=['Customer_ID']
)

st.plotly_chart(fig)

# Cluster Distribution
cluster_count = df['Cluster'].value_counts().reset_index()
cluster_count.columns = ['Cluster', 'Count']

fig2 = px.bar(
    cluster_count,
    x='Cluster',
    y='Count',
    color='Cluster',
    title='Customer Cluster Distribution'
)

st.plotly_chart(fig2)