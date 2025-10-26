# Student_Career_Recommendation_System
# Student Career Recommendation System  

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)  
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Model-green.svg)  
![Status](https://img.shields.io/badge/Status-Completed-success.svg)  
![License](https://img.shields.io/badge/License-MIT-yellow.svg)  

## Overview  
The **Student Career Recommendation System** is a machine learning-based project that helps students choose the **most suitable career path** based on their **academic background**, **skills**, and **interests**.  
It uses machine learning algorithms to analyze educational data and predict the best career match, supporting students in informed career decision-making.  

---

## Objectives  
- Recommend an ideal **career path** for students using data-driven insights.  
- Align students’ **degrees, majors, and skills** with potential job roles.  
- Provide a **personalized prediction** to help plan future career steps.  

---

##  Dataset  
The dataset includes essential student details such as:  
-  **Degree** (e.g., B.Tech, B.Com, B.Sc.)  
-  **Major / Specialization**  
- **Skills / Technical Knowledge**  
-  **Career Path (Target Variable)**  

> The data was cleaned, encoded, and preprocessed for model training and testing.

---

## Tools & Technologies  
| Category | Tools/Technologies |
|-----------|--------------------|
| Language | Python |
| Libraries | Pandas, NumPy, Scikit-learn, Pickle |
| Models | RandomForestClassifier, XGBoost, SVC |
| IDEs | Jupyter Notebook, VS Code |

---

##  Project Workflow  
1. **Data Cleaning & Preprocessing** — Removed null values and standardized input data.  
2. **Exploratory Data Analysis (EDA)** — Analyzed relationships and feature importance.  
3. **Label Encoding** — Converted categorical variables into numerical values.  
4. **Model Training & Evaluation** — Trained models like Random Forest, SVC, and XGBoost.  
5. **Model Saving** — Stored trained model and encoders as `.pkl` files.  

---

##  How It Works  
```python
# Step 1: Load the model
import pickle
model = pickle.load(open('career_model.pkl', 'rb'))

# Step 2: Input student details
input_data = ['B.Com', 'Finance', 'Data Analysis']

# Step 3: Predict career path
predicted_career = model.predict([input_data])
print("Recommended Career:", predicted_career)
