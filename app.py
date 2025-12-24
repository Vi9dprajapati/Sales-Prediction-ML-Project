from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("sales_prediction_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    tv = float(request.form['tv'])
    radio = float(request.form['radio'])
    newspaper = float(request.form['newspaper'])

    # Create DataFrame (IMPORTANT)
    data = pd.DataFrame([[tv, radio, newspaper]],
                         columns=['TV', 'Radio', 'Newspaper'])

    prediction = model.predict(data)[0]

    return render_template(
        'index.html',
        prediction_text=f"Predicted Sales: {prediction:.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)
