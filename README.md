# 🚗 Car Price Prediction (Machine Learning)

This is an **end-to-end machine learning project** that predicts car prices using multiple regression models such as **Linear Regression**, **Decision Tree Regressor**, **Random Forest Regressor**, and **XGBoost**.  
The project demonstrates the complete ML workflow, including data preprocessing, feature engineering, pipelines, cross-validation, and model evaluation using **RMSE** and **R² score**.

---

## 📌 Problem Statement
The objective of this project is to **predict the price of a car** based on its technical specifications and characteristics.  
This is a **supervised regression problem** where the target variable is continuous.

---

## 📊 Dataset Features

The dataset contains the following features:

| Feature Name | Description |
|-------------|------------|
| **model** | Car model name |
| **year** | Manufacturing year of the car |
| **price** | Car price *(target variable)* |
| **transmission** | Transmission type (Manual / Automatic) |
| **mileage** | Total distance driven |
| **fuelType** | Fuel type (Petrol, Diesel, Hybrid, etc.) |
| **tax** | Road tax |
| **mpg** | Miles per gallon (fuel efficiency) |
| **engineSize** | Engine size in liters |
| **Manufacturer** | Car brand or manufacturer |

---

## 🎯 Target Variable
- **price** → The value that the model predicts.

---

## 🧠 Feature Types

### Categorical Features
- model  
- transmission  
- fuelType  
- Manufacturer  

### Numerical Features
- year  
- mileage  
- tax  
- mpg  
- engineSize  

---

## 🧠 Machine Learning Approach
- Type: **Supervised Learning (Regression)**
- Models implemented:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - XGBoost Regressor

---

## ⚙️ Technologies Used
- Python
- Pandas & NumPy
- Scikit-learn
- XGBoost
- Jupyter Notebook

---

## 🔄 Project Workflow
1. Data loading and exploration
2. Train-test split
3. Data preprocessing:
   - Handling missing values
   - Scaling numerical features
   - One-hot encoding categorical features
4. Building preprocessing pipelines
5. Model training
6. Model evaluation using cross-validation
7. Model comparison and performance analysis

---

## 📊 Evaluation Metrics
The models are evaluated using:
- **Root Mean Squared Error (RMSE)**
- **R² Score (Coefficient of Determination)**

Cross-validation is used to ensure reliable and unbiased performance evaluation.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Abhi-prajapat-i/car-price-prediction-ml.git

