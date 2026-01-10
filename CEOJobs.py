import pandas as pd

data = {
    "Id": [1, 2, 3, 4],
    "Name": ["Pankaj", "Meghna", "David", "Lisa"],
    "Role": ["CEO", None, None, None],
    "Salary": [40000, 2000, None, None]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nFirst 2 rows:")
print(df.head(2))
print("\nLast 2 rows:")
print(df.tail(2))

print("\nTotal number of null values in DataFrame:")
print(df.isnull().sum().sum())

print("\nDataFrame Info:")
df.info()

df_drop_rows = df.dropna()
print("\nDataFrame after dropping rows with null values:")
print(df_drop_rows)

df_drop_columns = df.dropna(axis=1)
print("\nDataFrame after dropping columns with null values:")
print(df_drop_columns)

df_filled = df.copy()
df_filled["Salary"] = df_filled["Salary"].fillna(2000)
df_filled["Role"] = df_filled["Role"].fillna("CFO")

print("\nDataFrame after filling null values:")
print(df_filled)
