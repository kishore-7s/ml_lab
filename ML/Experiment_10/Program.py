import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("news.csv")

# Display first few records
print(data.head())

# Text and target columns
X = data["text"]
y = data["category"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text into TF-IDF features
vectorizer = TfidfVectorizer(stop_words="english")
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Create Naive Bayes model
model = MultinomialNB()

# Train model
model.fit(X_train_tfidf, y_train)

# Predict categories
y_pred = model.predict(X_test_tfidf)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Example prediction
news = ["The team won the championship match after an exciting game."]

news_tfidf = vectorizer.transform(news)
prediction = model.predict(news_tfidf)

print("\nPredicted News Category:", prediction[0])
