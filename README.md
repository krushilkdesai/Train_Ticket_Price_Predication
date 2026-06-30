# Train Ticket Price Prediction

A Machine Learning application to predict train ticket prices using **Random Forest Regressor**. Includes a Flask web application for real-time price predictions.

------


## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Objective](#-objective)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Features](#-features)
- [Model Details](#-model-details)
- [Technologies Used](#-technologies-used)

---

## 📘 Project Overview

The **Train Ticket Price Prediction** project predicts train ticket prices based on travel parameters using a **Random Forest Regressor** machine learning model. The system includes:
- Data preprocessing and analysis via Jupyter Notebook
- Trained Random Forest model saved as a pickle file
- Flask web application for user-friendly predictions
- Support for 11 different train types and multiple routes

---

## 🎯 Objective

- Predict train ticket prices based on train type, source city, and destination city
- Provide a simple web interface for real-time price predictions
- Ensure accurate and reliable price estimations using Random Forest Regressor
- Validate input to prevent invalid route selections

---

## 📁 Project Structure

```
Train_Ticket_Price_Prediction/
│
├── rail.csv                              # Dataset with historical train data
├── main.py                               # Flask web application
├── Rail_Ticket_Price_Predication.ipynb  # Jupyter notebook with data analysis
├── README.md                             # Project documentation
├── random_forest_regression_model.pkl   # Trained Random Forest model
│
└── templates/
    └── index.html                        # Web interface
```

---

## 💻 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone or Download the Project**
   ```bash
   cd Train_Ticket_Price_Prediction
   ```

2. **Create Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install flask pandas numpy scikit-learn matplotlib seaborn jupyter
   ```

### Deploy to Vercel
1. Install the Vercel CLI if it is not already installed:
   ```bash
   npm install -g vercel
   ```
2. Log into Vercel and deploy from your project folder:
   ```bash
   cd /Users/kk/AI_Projects/Train_Ticket_Price_Predication
   vercel login
   vercel
   ```
3. Confirm the default settings when prompted.

This project now includes `vercel.json`, `requirements.txt`, and an `api/main.py` entrypoint for deployment.

---

## 🚀 How to Run

### Run Web Application
```bash
python main.py
```
- Opens at `http://localhost:5000`
- Select train, source, and destination city
- Click "Predict Price" to get the estimated ticket price

### Run Jupyter Notebook
```bash
jupyter notebook Rail_Ticket_Price_Predication.ipynb
```
- Explore data analysis and model building
- Review preprocessing steps and visualizations

---

## ✨ Features

✅ **Random Forest Regressor Model** - Accurate price predictions  
✅ **User-Friendly Web Interface** - Simple dropdown selection  
✅ **11 Train Types Supported** - Garib Rath, Humsafar Express, Rajdhani Express, etc.  
✅ **Multiple Routes** - 5 source cities & 6 destination cities  
✅ **Input Validation** - Prevents same source and destination selection  
✅ **Real-Time Predictions** - Instant price estimates  
✅ **Responsive Design** - Works on desktop and mobile  

---

## 🤖 Model Details

**Algorithm:** Random Forest Regressor

**Performance Metrics:**
- **R² Score:** 0.96 (explains 96% of price variance)
- **RMSE:** ₹98.32 (average prediction error)
- **Model File:** `random_forest_regression_model.pkl`

**Input Parameters:**
- Train Type (11 categories)
- Source City (5 options)
- Destination City (6 options)

**Output:**
- Predicted ticket price in Indian Rupees (₹)

---

## 🛠️ Technologies Used

| Technology | Purpose |
|:-----------|:---------|
| **Python** | Core programming language |
| **Scikit-learn** | Random Forest Regressor |
| **Pandas & NumPy** | Data manipulation |
| **Flask** | Web framework |
| **HTML/CSS/Bootstrap** | Web interface |
| **Jupyter Notebook** | Data exploration |
| **Matplotlib & Seaborn** | Data visualization |

---

## 📝 Additional Notes

- Source and destination cities cannot be the same
- Ticket prices are predicted in Indian Rupees (₹)
- The model uses a pre-trained pickle file for consistent predictions
- No internet connection required for local predictions

---

