from flask import request, jsonify, render_template
from . import db
from .model import model
from .utils import preprocess_data, scale_data, inverse_scale
from app import create_app

@app.route('/')
def indez():
    return render_template('index.html')

@app.route('predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_prices = preprocess_data(data['prices'])
    scaled_input_prices = scale_data(input_prices)
    input_data = scaled_input_prices.reshape(1, Config.SEQUENCE_LENGTH, 1)
    prediction = model.predict(input_data)
    predicted_price = inverse_scale(prediction)
    
    return jsonify({'predicted_price': predicted_price})