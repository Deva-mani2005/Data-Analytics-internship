import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load data
df = pd.read_csv("sales_forecast.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Create month number
df["Month_Number"] = range(1, len(df)+1)

# Features
X = df[["Month_Number"]]

# Target
y = df["Sales"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next 6 months
future_months = np.array(
    range(len(df)+1, len(df)+7)
).reshape(-1,1)

predictions = model.predict(future_months)

future_dates = pd.date_range(
    start="2024-01-01",
    periods=6,
    freq="MS"
)

future_df = pd.DataFrame({
    "Date": future_dates,
    "Predicted_Sales": predictions.astype(int)
})

print(future_df)

future_df.to_csv(
    "outputs/forecast_output.csv",
    index=False
)