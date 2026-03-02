# 🚀 Quick Start Guide - Password Strength Checker Flask App

Follow these steps to get the Flask application running in less than 5 minutes!

## Step 1: Open Terminal/PowerShell

Navigate to your project folder:
```powershell
cd "d:\Data science Cybersecurity\latihan\Checking-Password-Strength-using-Machine-Learning"
```

## Step 2: Create Virtual Environment

```powershell
python -m venv venv
```

## Step 3: Activate Virtual Environment

**On Windows (PowerShell)**:
```powershell
.\venv\Scripts\Activate
```

You should see `(venv)` at the beginning of your command prompt.

## Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

This will install Flask, scikit-learn, pandas, and other required packages.

## Step 5: Train the Model

```powershell
python train_model.py
```

Wait for the training to complete. You should see:
```
✓ Model saved to 'models/gb_model.pkl'
✓ Vectorizer saved to 'models/tfidf_vectorizer.pkl'
Ready to use with Flask app!
```

## Step 6: Start the Flask Application

```powershell
python app.py
```

You should see:
```
✓ Model and vectorizer loaded successfully!
WARNING: This is a development server. Do not use it in production.
Running on http://0.0.0.0:5000
```

## Step 7: Open Web Browser

Go to:
```
http://localhost:5000
```

Or:
```
http://127.0.0.1:5000
```

## ✨ You're All Set!

Now you can:
1. Enter any password in the input field
2. Click "Check Strength" or press Enter
3. See the strength assessment with real-time ML analysis!

## 💡 Tips

- **Show/Hide Password**: Click the 👁️ button to toggle password visibility
- **Try Examples**: 
  - `123` → Weak 🔴
  - `MyPass123` → Medium 🟡
  - `MySecureP@ss123!` → Strong 🟢

## 🛑 Stop the Application

Press `Ctrl + C` in the terminal to stop the Flask server.

## 📝 File Structure Created

```
models/
├── gb_model.pkl                    # Trained model
└── tfidf_vectorizer.pkl            # Text vectorizer

templates/
└── index.html                       # Web interface

static/
├── style.css                        # Styling
└── script.js                        # Frontend logic

app.py                               # Flask application
train_model.py                       # Training script
requirements.txt                     # Dependencies
FLASK_README.md                      # Full documentation
QUICKSTART.md                        # This file
```

## 🔧 Troubleshooting

### Problem: "Module not found" error
**Solution**: Make sure you activate the virtual environment:
```powershell
.\venv\Scripts\Activate
```

### Problem: "Address already in use"
**Solution**: Another app is using port 5000. Change the port in `app.py`:
Edit line at the end from:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```
To:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```
Then access: `http://localhost:5001`

### Problem: "Model not loaded"
**Solution**: Make sure `train_model.py` ran successfully and created the `models/` folder.

## 📖 Learn More

See `FLASK_README.md` for comprehensive documentation including:
- API endpoints
- Model performance metrics
- Deployment guide
- Advanced configuration

## 🎉 Enjoy!

Your machine learning password strength checker is now running! Share your feedback and suggestions.

---
**Need help?** Check the logs in the terminal for error messages.
