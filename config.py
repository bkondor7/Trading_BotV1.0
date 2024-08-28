import os

class Config:
    API_KEY = os.getenv('ALPACA_API_KEY', '####################') # Replace with actual API key
    API_SECRET = os.getenv('ALPACA_API_SECRET', '###################################') # Replace with actual API secret
    BASE_URL = 'https://paper-api.alpaca.markets'
    DATABASE_URI = 'sqlite:///trading_bot.db'  # Replace with actual database URI
    MODEL_PATH = 'models/lstm_model.h5'
    SEQUENCE_LENGTH = 50
