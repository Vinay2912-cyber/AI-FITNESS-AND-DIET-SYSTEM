<p align="center">
  <img src="banner.png" alt="AI Fitness & Diet Recommendation System Banner" width="100%">
</p>

# AI Fitness & Diet Recommendation System  

> A smart AI-powered web application that recommends **personalized diet and fitness plans** using **Machine Learning** and **Flask**.  
> Built as part of MCA Cloud & DevOps specialization to promote health awareness through data-driven insights.  

---

## Project Overview  

The **AI Fitness & Diet Recommendation System** analyzes user health metrics — such as **height, weight, age, activity level, and fitness goal** — to:  
✅ Predict required daily calorie intake  
✅ Suggest a custom **diet plan**  
✅ Recommend a matching **workout routine**

It uses a trained **Linear Regression Machine Learning model** and serves results through a beautiful **Flask-based web interface**.

---

##  Features  

| Category | Description |
|-----------|--------------|
|  **AI Prediction** | Calculates daily calorie requirements based on user input |
|  **Diet Suggestion** | Offers personalized meal recommendations |
|  **Workout Routine** | Suggests light, medium, or high activity workouts |
|  **Responsive Web UI** | Clean, modern interface built with HTML & CSS |
|  **Tech Stack** | Flask, Python, scikit-learn, Pandas, HTML, CSS |

---

## Tech Stack  

| Component | Technology Used |
|------------|----------------|
| **Frontend** | HTML5, CSS3 |
| **Backend** | Python Flask |
| **Machine Learning** | scikit-learn (Linear Regression) |
| **Data Handling** | Pandas, NumPy |
| **Model Storage** | Pickle |
| **Deployment** | Localhost / GitHub / Render / Replit |

---

## Project Structure

AI-Fitness-Diet-System/ │ ├── app.py                 # Main Flask app ├── model.py               # Trains Linear Regression Model ├── model.pkl              # Saved trained model ├── requirements.txt       # Dependencies list ├── README.md              # Project Documentation │ ├── templates/ │   ├── index.html         # Input form │   └── result.html        # Result page │ └── static/ └── style.css          # Styling file

---

##  How to Run the Project  

### 1️⃣ Install Dependencies  
```bash
pip install -r requirements.txt

2️⃣ Train the Model

python model.py

3️⃣ Run the Flask App

python app.py

4️⃣ Open in Browser

Go to → http://127.0.0.1:5000
