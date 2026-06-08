import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(
    page_title="Sales Forecast Dashboard",
    layout="wide"
)

st.title("📈 Predictive Analytics Dashboard")

# Load data
df = pd.read_csv("sales_forecast.csv")

# Convert Month column to datetime
df["Month"] = pd.to_datetime(df["Month"])

# Create month numbers
df["Month_Number"] = range(1, len(df)+1)

# Features and target
X = df[["Month_Number"]]
y = df["Sales"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next 6 months
future_months = np.array(
    range(len(df)+1, len(df)+7)
).reshape(-1,1)

predictions = model.predict(future_months)

# Future dates
future_dates = pd.date_range(
    start=df["Month"].max() + pd.DateOffset(months=1),
    periods=6,
    freq="MS"
)

future_df = pd.DataFrame({
    "Month": future_dates,
    "Sales": predictions
})

# Combine data
combined_df = pd.concat(
    [df[["Month","Sales"]], future_df],
    ignore_index=True
)

# KPI
col1, col2 = st.columns(2)

col1.metric(
    "Current Total Sales",
    f"₹{df['Sales'].sum():,.0f}"
)

col2.metric(
    "Predicted Next 6 Months Sales",
    f"₹{future_df['Sales'].sum():,.0f}"
)

# Forecast Chart
st.subheader("Sales Forecast")

fig = px.line(
    combined_df,
    x="Month",
    y="Sales",
    markers=True,
    title="Historical & Forecasted Sales"
)

st.plotly_chart(fig, use_container_width=True)

# Dataset
st.subheader("Historical Data")
st.dataframe(df)

# Predictions
st.subheader("Future Predictions")
st.dataframe(future_df)