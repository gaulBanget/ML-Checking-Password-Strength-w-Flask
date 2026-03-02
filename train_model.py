import warnings
warnings.simplefilter('ignore')

import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
import os

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

print("Loading data...")
data = pd.read_csv("Password Strength.csv", on_bad_lines='skip')

print("Cleaning data...")
df = data.dropna()

x = df['password']
y = df['strength']

print(f"Dataset size: {len(df)}")
print(f"Strength distribution:\n{y.value_counts()}")

# Define character tokenizer
def character(inputs):
    characters = []
    for i in inputs:
        characters.append(i)
    return characters

# TF-IDF Vectorization
print("\nVectorizing passwords...")
vec = TfidfVectorizer(tokenizer=character)
x_vectorized = vec.fit_transform(x)

print(f"Vectorized shape: {x_vectorized.shape}")

# Train-test split
print("\nSplitting data...")
x_train, x_test, y_train, y_test = train_test_split(x_vectorized, y, test_size=0.2, random_state=1000)

# Train Gradient Boosting Model
print("\nTraining Gradient Boosting Model...")
gb_model = GradientBoostingClassifier(random_state=42)
gb_model.fit(x_train, y_train)

# Make predictions
y_pred_train = gb_model.predict(x_train)
y_pred_test = gb_model.predict(x_test)

# Evaluate model
print("\n" + "="*50)
print("MODEL PERFORMANCE")
print("="*50)
print(f"Training Accuracy: {accuracy_score(y_train, y_pred_train):.4f}")
print(f"Testing Accuracy: {accuracy_score(y_test, y_pred_test):.4f}")
print(f"Precision: {precision_score(y_test, y_pred_test, average='weighted'):.4f}")
print(f"Recall: {recall_score(y_test, y_pred_test, average='weighted'):.4f}")
print(f"F1-Score: {f1_score(y_test, y_pred_test, average='weighted'):.4f}")
print("="*50)

# Save model and vectorizer
print("\nSaving model and vectorizer...")
with open('models/gb_model.pkl', 'wb') as f:
    pickle.dump(gb_model, f)

with open('models/tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(vec, f)

print("✓ Model saved to 'models/gb_model.pkl'")
print("✓ Vectorizer saved to 'models/tfidf_vectorizer.pkl'")
print("\nReady to use with Flask app!")
