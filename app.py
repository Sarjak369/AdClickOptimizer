import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

FEATURE_NAMES = [
    'Daily Time Spent on Site',
    'Age',
    'Area Income',
    'Daily Internet Usage',
    'Male'
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # get form inputs
    values = [float(x) for x in request.form.values()]

    # build DataFrame with the same feature names used in training
    input_df = pd.DataFrame([values], columns=FEATURE_NAMES)

    # class prediction (0/1)
    pred_class = int(model.predict(input_df)[0])

    # probability of clicking on ad (class 1)
    prob_click = float(model.predict_proba(input_df)[0][1])

    if pred_class == 1:
        text = (
            f"There is a higher chance that user will click on an ad. "
            f"The probability of a user clicking on an ad is {prob_click:.2f}"
        )
    else:
        text = (
            f"There is a lower chance that user will click on an ad. "
            f"The probability of a user clicking on an ad is {prob_click:.2f}"
        )

    return render_template('index.html', prediction_text=text)


@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    values = [float(v) for v in data.values()]
    input_df = pd.DataFrame([values], columns=FEATURE_NAMES)
    pred_class = int(model.predict(input_df)[0])
    return jsonify(pred_class)


if __name__ == "__main__":
    app.run(debug=True)
