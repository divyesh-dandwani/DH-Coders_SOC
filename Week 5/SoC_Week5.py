#!/usr/bin/env python
# coding: utf-8

# # Import Libraries and Load Dataset

# In[1]:


import pandas as pd

path = r"C:\Users\Divyesh\.cache\kagglehub\datasets\bhavikjikadara\car-price-prediction-dataset\versions\1\car_prediction_data.csv"

df = pd.read_csv(path)


# # Task 1 : Load the Dataset

# In[2]:


# Import Required Library
import pandas as pd

# Load Dataset
path = r"C:\Users\Divyesh\.cache\kagglehub\datasets\bhavikjikadara\car-price-prediction-dataset\versions\1\car_prediction_data.csv"

df = pd.read_csv(path)

# Display First 5 Rows
print("========== First 5 Rows ==========")
print(df.head())

# Display Last 5 Rows
print("\n========== Last 5 Rows ==========")
print(df.tail())

# Display Shape
print("\n========== Shape of Dataset ==========")
print(df.shape)

# Display Column Names
print("\n========== Column Names ==========")
print(df.columns)

# Display Data Types
print("\n========== Data Types ==========")
print(df.dtypes)


# # Task 2 : Explore the Dataset

# In[3]:


# Display Dataset Information
print("========== Dataset Information ==========")
df.info()

# Display Statistical Summary
print("\n========== Statistical Summary ==========")
print(df.describe())

# Find Missing Values
print("\n========== Missing Values ==========")
print(df.isnull().sum())

# Find Duplicate Rows
print("\n========== Duplicate Rows ==========")
duplicates = df.duplicated().sum()
print("Number of Duplicate Rows :", duplicates)

# Remove Duplicate Rows (if any)
if duplicates > 0:
    df = df.drop_duplicates()
    print("\nDuplicate rows removed successfully.")
else:
    print("\nNo duplicate rows found.")

# Verify Duplicate Removal
print("\n========== Verify Duplicate Rows ==========")
print("Duplicate Rows :", df.duplicated().sum())


# # Task 3 : Data Cleaning

# In[4]:


from sklearn.preprocessing import LabelEncoder

print("========== Missing Values Before Cleaning ==========")
print(df.isnull().sum())

# Handle Missing Values
# (Is dataset me missing values nahi hain, fir bhi ye code future ke liye useful hai.)

df = df.dropna()

print("\n========== Missing Values After Cleaning ==========")
print(df.isnull().sum())


# -----------------------------------------
# Convert Categorical Columns to Numerical
# -----------------------------------------

encoder = LabelEncoder()

categorical_columns = [
    "Car_Name",
    "Fuel_Type",
    "Seller_Type",
    "Transmission"
]

for column in categorical_columns:
    df[column] = encoder.fit_transform(df[column])

print("\n========== Dataset After Encoding ==========")
print(df.head())


# -----------------------------------------
# Check Data Types
# -----------------------------------------

print("\n========== Data Types ==========")
print(df.dtypes)


# -----------------------------------------
# Check Invalid / Inconsistent Data
# -----------------------------------------

print("\n========== Checking Invalid Values ==========")

print("Negative Selling Price :", (df["Selling_Price"] < 0).sum())

print("Negative Present Price :", (df["Present_Price"] < 0).sum())

print("Negative Kms Driven :", (df["Kms_Driven"] < 0).sum())

print("Invalid Owner Value :", (df["Owner"] < 0).sum())


# -----------------------------------------
# Dataset Ready for Machine Learning
# -----------------------------------------

print("\n==============================================")
print("Dataset is cleaned and ready for Machine Learning.")
print("==============================================")


# # Task 4 : Data Visualization (Matplotlib)

# In[5]:


import matplotlib.pyplot as plt

# -----------------------------------------
# Histogram of Selling Price
# -----------------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["Selling_Price"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram of Selling Price")
plt.xlabel("Selling Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


# -----------------------------------------
# Scatter Plot : Kms Driven vs Selling Price
# -----------------------------------------

plt.figure(figsize=(8,5))
plt.scatter(df["Kms_Driven"], df["Selling_Price"], color="red")
plt.title("Kms Driven vs Selling Price")
plt.xlabel("Kms Driven")
plt.ylabel("Selling Price")
plt.grid(True)
plt.show()


# -----------------------------------------
# Scatter Plot : Year vs Selling Price
# -----------------------------------------

plt.figure(figsize=(8,5))
plt.scatter(df["Year"], df["Selling_Price"], color="green")
plt.title("Year vs Selling Price")
plt.xlabel("Year")
plt.ylabel("Selling Price")
plt.grid(True)
plt.show()


# -----------------------------------------
# Bar Chart : Fuel Types
# -----------------------------------------

fuel_counts = df["Fuel_Type"].value_counts()

plt.figure(figsize=(6,5))
plt.bar(fuel_counts.index, fuel_counts.values, color=["blue","orange","green"])
plt.title("Number of Cars by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Count")
plt.show()


# -----------------------------------------
# Correlation Heatmap
# -----------------------------------------

correlation = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))
plt.imshow(correlation, cmap="coolwarm")

plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)

plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Heatmap")

plt.show()


# -----------------------------------------
# Box Plot : Selling Price
# -----------------------------------------

plt.figure(figsize=(5,6))
plt.boxplot(df["Selling_Price"])

plt.title("Box Plot of Selling Price")
plt.ylabel("Selling Price")

plt.show()


# # Task 5 : Feature Selection

# In[6]:


from sklearn.model_selection import train_test_split

# -----------------------------------------
# Select Input Features (X)
# -----------------------------------------

X = df.drop("Selling_Price", axis=1)

# -----------------------------------------
# Select Target Variable (y)
# -----------------------------------------

y = df["Selling_Price"]

# -----------------------------------------
# Split Dataset into Training and Testing Sets
# -----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# -----------------------------------------
# Display Dataset Shapes
# -----------------------------------------

print("========== Dataset Split ==========")

print("Total Features Shape :", X.shape)
print("Total Target Shape   :", y.shape)

print("\nTraining Features Shape :", X_train.shape)
print("Training Target Shape   :", y_train.shape)

print("\nTesting Features Shape  :", X_test.shape)
print("Testing Target Shape    :", y_test.shape)

print("\nDataset successfully split into 80% Training and 20% Testing.")


# # Task 6 : Build a Linear Regression Model

# In[7]:


from sklearn.linear_model import LinearRegression

# -----------------------------------------
# Create Linear Regression Model
# -----------------------------------------

model = LinearRegression()

# -----------------------------------------
# Train the Model
# -----------------------------------------

model.fit(X_train, y_train)

print("Model trained successfully.")

# -----------------------------------------
# Make Predictions on Test Data
# -----------------------------------------

y_pred = model.predict(X_test)

print("\n========== Predicted Selling Prices ==========")
print(y_pred)

# -----------------------------------------
# Compare Actual vs Predicted Values
# -----------------------------------------

print("\n========== Actual vs Predicted ==========")

comparison = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
})

print(comparison.head(10))


# # Task 7 : Model Evaluation

# In[8]:


from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np

# -----------------------------------------
# Calculate Evaluation Metrics
# -----------------------------------------

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

# -----------------------------------------
# Display Results
# -----------------------------------------

print("========== Model Evaluation ==========\n")

print("Mean Absolute Error (MAE) :", mae)

print("Mean Squared Error (MSE) :", mse)

print("Root Mean Squared Error (RMSE) :", rmse)

print("R² Score :", r2)

# -----------------------------------------
# Interpretation
# -----------------------------------------

print("\n========== Interpretation ==========\n")

print("1. MAE tells the average prediction error.")

print("2. MSE gives more importance to large errors.")

print("3. RMSE represents prediction error in the same unit as Selling Price.")

print("4. R² Score tells how well the model predicts the data.")

if r2 >= 0.90:
    print("\nExcellent Model Performance")

elif r2 >= 0.75:
    print("\nVery Good Model Performance")

elif r2 >= 0.50:
    print("\nAverage Model Performance")

else:
    print("\nPoor Model Performance")


# # Task 8 : Prediction

# In[9]:


# -----------------------------------------
# Select One Sample Car
# -----------------------------------------

sample_car = X.iloc[[0]]

print("========== Sample Car Details ==========\n")
print(sample_car)

# -----------------------------------------
# Predict Selling Price
# -----------------------------------------

predicted_price = model.predict(sample_car)

print("\n========== Prediction ==========\n")

print("Predicted Selling Price :", predicted_price[0])

# -----------------------------------------
# Compare with Actual Price
# -----------------------------------------

actual_price = y.iloc[0]

print("Actual Selling Price    :", actual_price)

# -----------------------------------------
# Prediction Summary
# -----------------------------------------

print("\n========== Prediction Summary ==========\n")

print("The trained Linear Regression model successfully predicted the selling price of the selected car.")

