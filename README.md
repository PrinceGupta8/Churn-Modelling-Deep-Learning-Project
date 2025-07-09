```markdown
# Churn Prediction with Deep Learning 🧠

A project to predict customer churn using an Artificial Neural Network (ANN) built with Keras. It includes data preprocessing, model training, evaluation, and deployment using Flask.

---

## 📂 Project Structure

```

Churn-Modelling-Deep-Learning-Project/
├── Churn\_Modelling.csv                 # Dataset
├── Churn\_Modelling\_DeepLearning.ipynb # Jupyter Notebook for training and evaluation
├── model.h5                            # Trained ANN model (saved Keras model)
├── scaler.pkl                          # Scaler used to transform input data
├── app.py                              # Flask API to serve predictions

````

---

## 📌 Project Description

The project builds a binary classifier to identify whether a bank customer is likely to churn. It uses features like credit score, geography, age, balance, and tenure. The model is trained using Keras and deployed via a Flask API (`app.py`).

---

## 🧪 How to Run

### 1. Install requirements
```bash
pip install -r requirements.txt
````

*(Create this file if not present: include Flask, numpy, pandas, scikit-learn, keras, tensorflow)*

### 2. Start the API server

```bash
python app.py
```

### 3. Make a prediction

Use any REST client (e.g., Postman or curl) to send a JSON POST request to:

```
http://127.0.0.1:5000/predict
```

Example JSON input:

```json
{
  "CreditScore": 600,
  "Geography": "France",
  "Gender": "Male",
  "Age": 40,
  "Tenure": 3,
  "Balance": 60000,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 50000
}
```

---

## 🧠 Model Details

* Framework: Keras (TensorFlow backend)
* Architecture: Fully connected layers with ReLU + Sigmoid
* Output: 0 or 1 (Churn or Not)
* Input: Scaled numeric features + encoded categories

---

## ✅ Status

* ✔️ Model training complete (`.ipynb`)
* ✔️ Model saved (`model.h5`)
* ✔️ Scaler saved (`scaler.pkl`)
* ✔️ API ready (`app.py`)

---

## 📬 Contact

**Prince Gupta**
📧 [princegupta995643@gmail.com](mailto:princegupta995643@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/prince-gupta-a8129a209/)

```
