import kagglehub
import pandas as pd
import os

path = kagglehub.dataset_download("yasserh/titanic-dataset")

files = os.listdir(path)

csv_file = None
for file in files:
    if file.endswith(".csv"):
        csv_file = file
        break

full_path = os.path.join(path, csv_file)
df = pd.read_csv(full_path)

print("First 10 Rows:")
print(df.head(10))

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())
