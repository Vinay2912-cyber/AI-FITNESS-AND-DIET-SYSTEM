import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.DataFrame({
    'height': [150,160,170,180,190],
    'weight': [50,60,70,80,90],
    'age': [20,25,30,35,40],
    'calories': [1800,2000,2200,2400,2600]
})

X = data[['height','weight','age']]
y = data['calories']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open('model.pkl','wb'))
print("✅ Model trained and saved as model.pkl")