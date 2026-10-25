import pandas as pd
from sklearn.model_selection import 
train_test_split
from sklearn.preprocessing import 
LabelEncoder
from sklearn.linear_model import 
LogisticRegression
from sklearn.metrics import 
accuracy_score, 
classification_report

# Load dataset
pd.read_csv("predictive_maintanance.csv")

# Display first few records
print(data.head())

# Remove unnecessary 
columns_data = data.drop(columns=["UDI", 
"Product ID"])

# Encode categorical 
column_encoder = LabelEncoder() 
data["Type"] = encoder.fit_transform(data["Type"])

# Features and target 
X = data.drop(columns=["Machine failure"]) 
y = data["Machine failure"]

# Split dataset 
X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size=0.2, random_state=42 
)

# Create Logistic Regression model 
model = LogisticRegression(max_iter=1000)

# Train model 
model.fit(X_train, y_train)

# Predict machine failure 
y_pred = model.predict(X_test)

# Calculate accuracy 
accuracy = accuracy_score(y_test, y_pred) 
print("\nAccuracy:", accuracy)

# Classification report 
print("\nClassification Report:") 
print(classification_report(y_t est, y_pred))

# Example prediction 
sample = X_test.iloc[[0]] 
prediction = model.predict(sample) 
if prediction[0] == 1:     
    print("\nPredicted Result: Machine Failure") 
else:     
    print("\nPredicted Result: No Machine Failure")
