# Sales Prediction App

A Flask web application for predicting sales based on advertising expenditures across TV, Radio, and Newspaper channels.

## Features

- Input advertising budgets for TV, Radio, and Newspaper
- Predict sales using a trained machine learning model
- Simple web interface with dark theme

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install dependencies:
   ```
   pip install flask joblib pandas scikit-learn
   ```

3. Ensure the trained model file `sales_prediction_model.pkl` is in the root directory.

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`

3. Enter values for TV, Radio, and Newspaper advertising budgets

4. Click "Predict Sales" to get the prediction

## Dataset

The model is trained on the Advertising dataset (`Advertising.csv`) which contains information about sales and advertising budgets.

## Model

The prediction model is stored in `sales_prediction_model.pkl` and uses features: TV, Radio, Newspaper advertising expenditures.

## Technologies Used

- Flask
- scikit-learn
- pandas
- joblib
