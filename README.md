# AI Enabled Recommendation Engine for E-Commerce Platform

## Infosys Springboard Internship  
### Milestone 2 – Model Building

---

## 📌 Project Overview
This project focuses on building an AI-based recommendation system for an e-commerce platform.  
The goal of **Milestone 2** is to develop, train, and evaluate a recommendation model using prepared user-item interaction data.

---

## 🎯 Milestone 2 Objective
- Develop and train the core recommendation model  
- Select an appropriate recommendation algorithm  
- Perform initial model tuning  
- Evaluate model performance using suitable metrics  

---

## 🧠 Recommendation Algorithm Used
**Collaborative Filtering – Matrix Factorization (SVD)**

- Learns latent features of users and products
- Commonly used in real-world recommender systems
- Efficient and scalable for large datasets

---

## 📂 Project Structure

---

## 📊 Dataset Description
The dataset contains user-product interaction data.

| Column Name  | Description |
|-------------|------------|
| user_id     | Unique ID of the user |
| product_id  | Unique ID of the product |
| rating      | User rating (1 to 5) |

---

## ⚙️ Model Training
- The SVD model is trained using collaborative filtering
- The dataset is split into training and testing sets
- The model learns latent user and product features

---

## 📈 Model Evaluation
**Evaluation Metric Used:**  
- Root Mean Square Error (RMSE)

Lower RMSE indicates better recommendation accuracy.

---

## 🔧 Initial Model Tuning
- Hyperparameters such as number of latent factors and regularization are tuned
- GridSearchCV is used to find optimal parameters

---

## 🧪 Sample Output
The model generates top-N product recommendations for a given user based on predicted ratings.

---

## ▶️ How to Run the Project

1. Install required libraries:

