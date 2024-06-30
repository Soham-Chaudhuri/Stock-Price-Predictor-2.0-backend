from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def getCompanies():
    companies_df = pd.read_csv('big_tech_companies.csv')
    company_suggest = []
    for i, row in companies_df.iterrows():
        temp = {'id': row['stock_symbol'], 'name': row['company'],'idx': i}
        company_suggest.append(temp)
    return company_suggest

def getCandleStickData(stock_symbol):
    # data_df = pd.read_csv('companies_stocks_price_df.csv')
    data_df = pd.read_csv('big_tech_stock_prices.csv')
    result = []
    for i, row in data_df.iterrows():
        if row['stock_symbol'] == stock_symbol:
            temp = {
                'open': row['open'],
                'close': row['close'],
                'high': row['high'],
                'low': row['low'],
                'volume' : row['volume'],
                'adj_close' : row['adj_close'],
                'time': row['date']
            }
            result.append(temp)
    return result

@app.get('/')
def home():
    return 'Hello world'

@app.get('/suggestData')
def suggestData():
    company_suggest = getCompanies()
    return jsonify(company_suggest)

@app.post('/getChartData')
def getChartData():
    stockOption = request.get_json()
    stock_symbol = stockOption['id']
    result = getCandleStickData(stock_symbol)
    # print(result)
    return jsonify({'data':result})

@app.post('/predict')
def predict():
    model=joblib.load('model.pkl')
    data = request.get_json()
    features = [
        float(data['idx']),
        float(data['open']),
        float(data['adj_close']),
        float(data['high']),
        float(data['low']),
        float(data['volume'])
    ]
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': round(prediction[0],2)})



if __name__ == '__main__':
    app.run(debug=True)
