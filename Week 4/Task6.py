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

print("Survival Rate By Gender:")
print(df.groupby("Sex")["Survived"].mean())

print("\nAverage Age By Passenger Class:")
print(df.groupby("Pclass")["Age"].mean())

print("\nPassengers Count By Class:")
print(df.groupby("Pclass").size())

survival_rate = df.groupby("Pclass")["Survived"].mean()

print("\nSurvival Rate By Class:")
print(survival_rate)

print("\nClass With Highest Survival Rate:")
print(survival_rate.idxmax())

print("\nAverage Fare By Class:")
print(df.groupby("Pclass")["Fare"].mean())

print("\nReport Summary:")
print("1. Female passengers had a much higher survival rate than male passengers.")
print("2. First-class passengers had the highest survival rate.")
print("3. Third-class passengers were the largest passenger group.")
print("4. First-class passengers paid the highest average fare.")
print("5. Passenger class and gender strongly affected survival chances.")
