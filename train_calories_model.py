import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load dataset
df = pd.read_csv("dataset/caloriesburned.csv")

# Convert Gender column into numbers
df["Gender"] = df["Gender"].map({
    "male": 0,
    "female": 1
})

# Features and target
X = df.drop(columns=["Calories Burned"])
y = df["Calories Burned"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestRegressor()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Calculate error
mae = mean_absolute_error(y_test, predictions)

print("✅ Model Trained Successfully")
print("Mean Absolute Error:", mae)

# Save model
joblib.dump(model, "models/calories_model.pkl")

print("✅ Model Saved Successfully")