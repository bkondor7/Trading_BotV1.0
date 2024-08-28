import numpy as np
from sklearn.preprocessing import MinMaxScaler
from config import Config

scaler = MinMaxScaler(feature_range=(0, 1))

def preprocess_data(prices):
    return np.array(prices).reshape(-1, 1)

def scale_data(data):
    return scaler.transform(data)

def inverse_scale(data):
    return scaler.inverse_transform(data)