Thank you for the clarification! Here's the revised version of your project description, with Streamlit as the framework, and the content shortened further:

---

<h1>🏡 House Price Prediction</h1>

An end-to-end machine learning project to predict house prices using regression models. Built with Python and deployed via a **Streamlit** web app to demonstrate data science, model engineering, and full-stack skills.

<b>🔍 Project Overview:</b>
This project develops and deploys a house price prediction system using historical housing data. It involves:

* Data preprocessing & feature engineering
* Model training, evaluation & comparison
* Serialization of the model pipeline
* Web interface to input house features and predict pricing

<b>🛠️ Key Features:</b>

* **Data Handling & Feature Engineering**: Clean and transform raw data to improve model accuracy.
* **Model Training & Evaluation**: Train and compare regression models (e.g., linear regression, tree-based models).
* **Pipeline & Serialization**: Build a model pipeline and serialize it for production.
* **Streamlit Web Application**: User-friendly UI for real-time price predictions.

<b>📂 Project Structure:</b>
House-Price-Prediction/
├── app.py # Streamlit app entry point
├── House_price_prediction.ipynb # EDA, modeling, experiments
├── kc_house_data.csv # Raw housing data
├── house_price_pipeline.pkl # Serialized model pipeline
├── requirements.txt # Project dependencies
└── README.md # Project documentation

<b>💻 Technologies & Skills:</b>

| Area             | Tools / Libraries                    |
| ---------------- | ------------------------------------ |
| Data Processing  | pandas, numpy, seaborn, matplotlib   |
| Machine Learning | scikit-learn, xgboost, random forest |
| Model Pipeline   | joblib, pickle                       |
| Web Deployment   | Streamlit                            |
| Version Control  | Git                                  |

<b>🚀 Installation & Running:</b>

1. Clone the repo and navigate to the project folder:

   ```bash
   git clone https://github.com/Walidsadiqi/House-Price-Prediction.git
   cd House-Price-Prediction
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

   Open the browser and go to `http://localhost:8501` to use the prediction UI.

<b>📈 Performance & Results:</b>

* Model evaluation metrics (RMSE, MAE, R²) documented in the notebook.
* Comparative performance across algorithms shown with visualizations.
* Deployed model available via the Streamlit app.

<b>🧠 Key Learnings:</b>

* Hands-on experience with data preprocessing, model tuning, and deployment.
* Packaging ML pipelines for production and embedding them in a UI.

⚠️ Note: This project is for educational purposes and requires further validation and scalability for real-world use.

---

### 👤 Author

**Walid Sadiqi**

Data Analyst | ML Engineer | AI Enthusiast | Python | SQL | Data Science

---

This version reflects the use of **Streamlit** instead of Flask, with all other necessary updates. Let me know if you need further adjustments!
