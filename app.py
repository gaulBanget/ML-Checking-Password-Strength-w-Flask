from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Character tokenizer function (must be defined here for pickle compatibility)
def character(inputs):
    characters = []
    for i in inputs:
        characters.append(i)
    return characters

# Load model and vectorizer
def load_models():
    try:
        with open('models/gb_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('models/tfidf_vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        return model, vectorizer
    except FileNotFoundError:
        return None, None

model, vectorizer = load_models()

# Strength mapping
STRENGTH_MAP = {
    0: {'label': 'Weak', 'emoji': '🔴', 'color': '#dc3545', 'advice': 'This password is weak. Please add uppercase letters, numbers, and special characters.'},
    1: {'label': 'Medium', 'emoji': '🟡', 'color': '#ffc107', 'advice': 'This password is medium strength. Consider adding more special characters.'},
    2: {'label': 'Strong', 'emoji': '🟢', 'color': '#28a745', 'advice': 'Excellent! This is a strong password.'}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/check-password', methods=['POST'])
def check_password():
    if model is None or vectorizer is None:
        return jsonify({
            'error': 'Model not loaded. Please run train_model.py first.',
            'status': 'error'
        }), 500
    
    try:
        data = request.get_json()
        password = data.get('password', '')
        
        if not password:
            return jsonify({
                'error': 'Password is required',
                'status': 'error'
            }), 400
        
        # Vectorize the password
        password_vector = vectorizer.transform([password])
        
        # Predict
        prediction = model.predict(password_vector)[0]
        confidence = max(model.predict_proba(password_vector)[0]) * 100
        
        # Get strength info
        strength_info = STRENGTH_MAP.get(prediction, STRENGTH_MAP[0])
        
        return jsonify({
            'password': password,
            'strength_code': int(prediction),
            'strength_label': strength_info['label'],
            'confidence': round(confidence, 2),
            'emoji': strength_info['emoji'],
            'color': strength_info['color'],
            'advice': strength_info['advice'],
            'password_length': len(password),
            'status': 'success'
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/api/password-tips', methods=['GET'])
def password_tips():
    tips = [
        "Use at least 8 characters",
        "Include uppercase letters (A-Z)",
        "Include lowercase letters (a-z)",
        "Include numbers (0-9)",
        "Include special characters (!@#$%^&*)",
        "Avoid common words and names",
        "Don't use sequential numbers or letters",
        "Mix different types of characters"
    ]
    return jsonify({'tips': tips}), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    if model is None or vectorizer is None:
        print("⚠️  WARNING: Model or vectorizer not found!")
        print("Please run 'python train_model.py' first to train and save the models.")
    else:
        print("✓ Model and vectorizer loaded successfully!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
