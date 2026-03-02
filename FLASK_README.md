# Password Strength Checker - Flask Web Application

A machine learning-powered web application to check password strength using Gradient Boosting classifier. This application features a modern, responsive web interface built with Flask.

## 🎯 Features

- **Machine Learning Analysis**: Uses Gradient Boosting model trained on character-level TF-IDF features
- **Real-time Strength Checking**: Instant password strength evaluation
- **Beautiful Web Interface**: Modern, responsive design with smooth animations
- **Detailed Feedback**: Provides strength level, confidence score, and personalized tips
- **Security**: All analysis is done locally - passwords are not stored or sent anywhere
- **Password Tips**: Helpful suggestions for creating stronger passwords

## 📊 Strength Levels

- **🔴 Weak (0)**: Passwords with limited character variety
- **🟡 Medium (1)**: Passwords with moderate complexity
- **🟢 Strong (2)**: Passwords with high complexity and diverse characters

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Navigate to the project directory**:
   ```bash
   cd "Checking-Password-Strength-using-Machine-Learning"
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Train the model** (generate trained models):
   ```bash
   python train_model.py
   ```
   This will:
   - Load the Password Strength.csv dataset
   - Train the Gradient Boosting model
   - Save the vectorizer and model to the `models/` directory
   - Display model performance metrics

6. **Run the Flask application**:
   ```bash
   python app.py
   ```

7. **Access the web interface**:
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
├── app.py                          # Main Flask application
├── train_model.py                  # Model training script
├── requirements.txt                # Python dependencies
├── Password Strength.csv           # Training dataset
├── Checking Password Strength.ipynb # Original Jupyter notebook
├── models/                         # Directory for saved models
│   ├── gb_model.pkl               # Trained Gradient Boosting model
│   └── tfidf_vectorizer.pkl       # TF-IDF vectorizer
├── templates/
│   └── index.html                 # Web interface template
└── static/
    ├── style.css                  # CSS styling
    └── script.js                  # Frontend JavaScript
```

## 🚀 Usage

### Training the Model

Run the training script to train a new model:
```bash
python train_model.py
```

Output example:
```
Loading data...
Cleaning data...
Dataset size: 670000

Vectorizing passwords...
Vectorized shape: (670000, 97)

Training Gradient Boosting Model...

==================================================
MODEL PERFORMANCE
==================================================
Training Accuracy: 0.9687
Testing Accuracy: 0.9685
Precision: 0.9687
Recall: 0.9685
F1-Score: 0.9685
==================================================
```

### Using the Web Application

1. Start the Flask app: `python app.py`
2. Open `http://localhost:5000` in your browser
3. Enter a password in the input field
4. Click "Check Strength" or press Enter
5. View the strength assessment and tips

### API Endpoints

#### Check Password Strength
```
POST /api/check-password
Content-Type: application/json

{
    "password": "YourPassword123!"
}

Response:
{
    "password": "YourPassword123!",
    "strength_code": 2,
    "strength_label": "Strong",
    "confidence": 95.67,
    "emoji": "🟢",
    "color": "#28a745",
    "advice": "Excellent! This is a strong password.",
    "password_length": 16,
    "status": "success"
}
```

#### Get Password Tips
```
GET /api/password-tips

Response:
{
    "tips": [
        "Use at least 8 characters",
        "Include uppercase letters (A-Z)",
        "Include lowercase letters (a-z)",
        "Include numbers (0-9)",
        "Include special characters (!@#$%^&*)",
        ...
    ]
}
```

## 🎓 How It Works

1. **Feature Engineering**: Passwords are converted to numerical features using TF-IDF vectorization at the character level
2. **Model Training**: A Gradient Boosting classifier learns to classify passwords into three strength categories
3. **Prediction**: New passwords are vectorized and classified in real-time
4. **Feedback**: The model provides confidence scores and personalized strength assessments

## 📈 Model Performance

The trained Gradient Boosting model achieves:
- **Training Accuracy**: ~96.87%
- **Testing Accuracy**: ~96.85%
- **F1-Score**: ~0.9685 (weighted average)

## 🔒 Privacy & Security

- **Local Processing**: All password analysis happens locally in your browser/server
- **No Storage**: Passwords are not saved, logged, or transmitted anywhere
- **No External Calls**: The application doesn't send data to external services
- **Use HTTPS**: For production deployment, use HTTPS to encrypt data in transit

## 🐛 Troubleshooting

### Model not found error
```
⚠️  WARNING: Model or vectorizer not found!
Please run 'python train_model.py' first
```
**Solution**: Run `python train_model.py` before starting the Flask app

### Port already in use
```
Address already in use
```
**Solution**: Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5000 to another port
```

### Module not found error
```
ModuleNotFoundError: No module named 'flask'
```
**Solution**: Make sure you've activated the virtual environment and run:
```bash
pip install -r requirements.txt
```

## 🚀 Deployment

For production deployment:

1. **Install gunicorn**:
   ```bash
   pip install gunicorn
   ```

2. **Run with gunicorn**:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Use environment variables** for configuration:
   ```python
   app.run(debug=False, host='0.0.0.0', port=os.environ.get('PORT', 5000))
   ```

## 📚 Technologies Used

- **Backend**: Flask (Python web framework)
- **Machine Learning**: Scikit-learn (Gradient Boosting)
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)

## 📝 Dataset Information

The training data contains:
- **670,000+** unique passwords
- **Strength Labels**: 0 (Weak), 1 (Medium), 2 (Strong)
- **Source**: Password Strength.csv

## 📄 License

This project uses the same license as the original repository. See LICENSE file for details.

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## ❓ FAQ

**Q: Are my passwords safe?**
A: Yes, absolutely. All analysis happens locally in your browser. Passwords are never stored or sent to servers.

**Q: Can I use this for production?**
A: Yes, with proper security measures (HTTPS, authentication, etc.)

**Q: How accurate is the model?**
A: The model achieves ~96.85% accuracy on the test set.

**Q: Can I train on custom data?**
A: Yes, modify `train_model.py` to use your own CSV file with 'password' and 'strength' columns.

## 📧 Support

For issues or questions, please refer to the project repository.

---

**Last Updated**: March 2, 2026
