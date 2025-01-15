import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Sample dataset
data = {
    "Feature1": [1, 2, 3, 4, 5],
    "Feature2": [5, 4, 3, 2, 1],
    "Target": [1.1, 1.9, 3.0, 4.1, 5.1],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Split into features and target
X = df[["Feature1", "Feature2"]]
y = df["Target"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
