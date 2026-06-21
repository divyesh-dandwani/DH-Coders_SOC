import pandas as pd

data = {
    "Student": ["A", "B", "C", "D"],
    "Maths": [85, 70, 95, 60],
    "Science": [90, 65, 88, 75]
}

df = pd.DataFrame(data)

df["Total"] = df["Maths"] + df["Science"]

df["Average"] = df["Total"] / 2

print("Updated DataFrame:")
print(df)

print("\nStudent with Highest Total:")
print(df.loc[df["Total"].idxmax()])

print("\nSorted by Average (Descending):")
print(df.sort_values(by="Average", ascending=False))

print("\nStudents with Average > 80:")
print(df[df["Average"] > 80])
