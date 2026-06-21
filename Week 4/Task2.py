import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [50000, 500, 1500, 12000],
    "Quantity": [5, 20, 15, 7]
}

df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

print("\nProduct Column:")
print(df["Product"])

print("\nProduct and Price Columns:")
print(df[["Product", "Price"]])

print("\nProducts with Price > 1000:")
print(df[df["Price"] > 1000])

print("\nProducts with Quantity < 10:")
print(df[df["Quantity"] < 10])

print("\nProducts with Price > 1000 AND Quantity < 10:")
print(df[(df["Price"] > 1000) & (df["Quantity"] < 10)])
