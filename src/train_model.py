import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Convert Date into datetime
df["Date"] = pd.to_datetime(df["Date"])

# Convert dates into numbers (0,1,2,3...)
df["Day"] = range(len(df))

# Features
X = df[["Day"]]

# Target
y = df["Units_Sold"]

# Train AI Model
model = LinearRegression()
model.fit(X, y)

print("=" * 50)
print("AI Model Trained Successfully!")
print("=" * 50)

print(f"Slope: {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
# Predict sales for the next day
next_day = [[len(df)]]
prediction = model.predict(next_day)

print(f"Predicted Units Sold Tomorrow: {prediction[0]:.0f}")