# Train_Ticket_Price_Predication

## 📘 Project Overview
The **Train Ticket Price Prediction** project aims to predict train ticket prices based on travel details such as source, destination, date, train type, and class.  
Using **Machine Learning techniques**, the project helps estimate ticket prices dynamically, providing insights for both passengers and railway operators.

---

## 🎯 Objective
- Predict the **ticket price** based on journey parameters.  
- Build and compare multiple **regression models** to find the best-performing one.  
- Perform **data preprocessing**, **feature engineering**, and **model evaluation** for optimal performance.  
- Deploy the model using **Flask** for real-time prediction.

---

## 📂 Dataset Description
The dataset contains historical train booking data with multiple features influencing the ticket price.

| Feature | Description |
|----------|--------------|
| **Train_Name** | Name or type of train (e.g., Rajdhani, Shatabdi, Express) |
| **Source** | Departure station |
| **Destination** | Arrival station |
| **Date_of_Journey** | Date when the journey starts |
| **Class** | Travel class (e.g., Sleeper, 3A, 2A, 1A) |
| **Quota** | Ticket quota type (e.g., General, Tatkal) |
| **Duration** | Total travel time |
| **Stops** | Number of stops between source and destination |
| **Price** | Target variable (ticket price) |

---

## 🧹 Data Preprocessing
1. Cleaned missing and inconsistent values.  
2. Converted date columns into useful time-based features (day, month, weekday).  
3. Encoded categorical variables such as `Source`, `Destination`, `Train_Name`, and `Class`.  
4. Normalized numerical data using **StandardScaler** for better model convergence.  
5. Split data into **training (80%)** and **testing (20%)** sets.

---

## 📊 Exploratory Data Analysis (EDA)
Performed EDA to understand the impact of various factors on ticket prices:
- Relationship between **journey duration** and **price**.  
- Price variation by **train type**, **class**, and **quota**.  
- Seasonal trends based on **month** and **day of journey**.  
- Used **Matplotlib** and **Seaborn** for visualizations.

---

## ⚙️ Model Building
Trained multiple regression algorithms to predict ticket prices:

1. **Linear Regression**  
2. **Decision Tree Regressor**  
3. **Random Forest Regressor**  
4. **Gradient Boosting Regressor**  
5. **XGBoost Regressor**

---

## 🧪 Model Comparison

| Model | R² Score | RMSE |
|:------|:----------:|:------:|
| Linear Regression | 0.85 | 220.45 |
| Decision Tree | 0.92 | 140.12 |
| Random Forest | 0.96 | 98.32 |
| Gradient Boosting | 0.97 | 85.45 |
| **XGBoost** | **0.98** | **78.90** |

🏆 **Best Performing Model:**  
✅ **XGBoost Regressor** achieved the highest accuracy with an R² Score of **0.98**, making it the most reliable for real-world prediction.

---

## 📈 Model Evaluation
Evaluated models using regression metrics:
- **R² Score**  
- **Mean Absolute Error (MAE)**  
- **Mean Squared Error (MSE)**  
- **Root Mean Squared Error (RMSE)**  

---

## 🧠 Technologies Used
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost  
- **Environment:** Jupyter Notebook / VS Code  
- **Deployment:** Flask Framework  

    prediction = model.predict([list(data.values())])
    return jsonify({'Predicted Ticket Price': round(prediction[0], 2)})

if __name__ == '__main__':
    app.run(debug=True)
