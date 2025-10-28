from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    age = float(request.form['age'])
    activity = request.form['activity']
    goal = request.form['goal']

    calories = model.predict([[height, weight, age]])[0]

    # Adjust based on activity level
    if activity == "low":
        calories *= 0.9
    elif activity == "high":
        calories *= 1.2

    # Adjust based on goal
    if goal == "weight_loss":
        calories -= 300
    elif goal == "weight_gain":
        calories += 300

    if calories < 2000:
        diet = " High protein + Fruits + Green Tea + Salads"
        workout = " 30 min brisk walk + yoga"
    else:
        diet = " Balanced carbs + Chicken/Fish + Veggies"
        workout = "️ 45 min strength training + stretching"

    return render_template('result.html', calories=int(calories), diet=diet, workout=workout)

if __name__ == '__main__':
    app.run(debug=True)