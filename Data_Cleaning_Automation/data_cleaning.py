import pandas as pd

# Load dataset
df = pd.read_csv("raw_data.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing Salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Fill missing Experience
df["Experience"] = df["Experience"].fillna(df["Experience"].median())

# Fill missing City
df["City"] = df["City"].fillna("Unknown")

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Cleaning Completed Successfully!")
print("Cleaned Shape:", df.shape)