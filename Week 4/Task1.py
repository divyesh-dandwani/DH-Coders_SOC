import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [21, 19, 22, 20],
    "City": ["Delhi", "Mumbai", "Ahmedabad", "Pune"]
}

df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

print("\nFirst 2 Rows:")
print(df.head(2))

print("\nColumn Names:")
print(df.columns)

print("\nShape of DataFrame:")
print(df.shape)

print("\nDataFrame Info:")
print(df.info())
