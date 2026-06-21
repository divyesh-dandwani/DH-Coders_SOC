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

print("Female Passengers:")
print(df[df["Sex"] == "female"])

print("\nPassengers Older Than 30:")
print(df[df["Age"] > 30])

print("\nPassengers Who Survived:")
print(df[df["Survived"] == 1])

print("\nFemale Passengers Who Survived:")
print(df[(df["Sex"] == "female") & (df["Survived"] == 1)])

print("\nAverage Age of Passengers:")
print(df["Age"].mean())

print("\nOldest Passenger:")
print(df.loc[df["Age"].idxmax()])
