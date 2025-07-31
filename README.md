# 🚘 Car Price Prediction App (Deployed in INR 🇮🇳)

This is a Machine Learning web app built using **Streamlit** that predicts the **market price of a car in Indian Rupees** 💰 based on specifications like brand, manufacturing year, fuel type, transmission type, and more.

---

## 📌 Project Overview

In this project, I built a regression model using a **Random Forest algorithm** to predict the MSRP (Manufacturer’s Suggested Retail Price) of cars.  
The original data was in USD, which I converted to INR for Indian users.

This app allows users to enter details through an interactive interface and instantly get the predicted car price.

---

## 🚀 Live Demo

👉 [Try the App Here](https://carpricepredicitonapp-r9yhz8dob9nqckzd3jvgqc.streamlit.app/)  
👉 [GitHub Repository](https://github.com/RishiKukadiya/Car_Price_Prediciton_App)

---

## 🛠 Technologies Used

- Python 🐍
- Pandas & NumPy for data handling
- Scikit-learn for ML model training
- Streamlit for web app development
- Joblib for model deployment
- Git & GitHub for version control and sharing

---

## 📈 Features

- Predicts car price in INR based on technical specs
- Clean, user-friendly UI with dropdowns and sliders
- Converts USD price to INR using exchange rate
- Deployed on Streamlit Cloud

---

## 🧠 ML Model Details

- **Model Type**: Random Forest Regressor
- **Encoding**: Label encoding + One-hot encoding
- **Preprocessing**: Feature scaling, input transformation
- **Deployment**: Model saved using `joblib`, served via Streamlit

---

## 📦 Installation (to run locally)

```bash
git clone https://github.com/RishiKukadiya/Car_Price_Prediciton_App.git
cd Car_Price_Prediciton_App
pip install -r requirements.txt
streamlit run app.py
