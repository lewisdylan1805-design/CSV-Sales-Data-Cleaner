import pandas as pd

# Step 1: Load data
try:
    df = pd.read_csv("sales_data.csv")
except FileNotFoundError:
    print("❌ File not found. Make sure 'sales_data.csv' is in the same folder as this script.")
    exit()

# Step 2: Clean column names
df.columns = df.columns.str.strip().str.capitalize()

# Step 3: Check for required columns
required_columns = {"Product", "Quantity", "Price"}
if not required_columns.issubset(df.columns):
    print(f"❌ Missing required columns. Found: {list(df.columns)}. Expected: {list(required_columns)}")
    exit()

# Step 4: Handle missing values
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Quantity"].fillna(df["Quantity"].mean(), inplace=True)
df["Price"].fillna(df["Price"].mean(), inplace=True)

# Step 5: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 6: Calculate total per row
df["Total"] = df["Quantity"] * df["Price"]

# Step 7: Export cleaned file
df.to_csv("cleaned_sales_data.csv", index=False)

# Step 8: Display summary
print("✅ Data cleaned and saved as 'cleaned_sales_data.csv'\n")
print("🔹 Summary:")
print(df.describe())
