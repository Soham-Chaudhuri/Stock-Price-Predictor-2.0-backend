# Stock Price Predictor Backend

This repository contains the backend code for the Stock Price Predictor application. The backend is built using Flask and provides the necessary APIs to support the frontend built with ReactJS, Lightweight Charts, and Axios [repo](https://github.com/Soham-Chaudhuri/Stock-Price-Predictor-frontend).

## Overview

The Stock Price Predictor application aims to predict future stock prices using a linear regression model repo [link](https://github.com/Soham-Chaudhuri/Stock-Price-Predictor-2.0). The frontend of the application is hosted at [Stonks by Soham](https://stonks-by-soham.netlify.app/) and the backend, which is this repository, provides the necessary APIs to serve the prediction data.

## Features

- **Stock Price Prediction**: Provides stock price predictions using a linear regression model.
- **Data Retrieval**: Fetches historical stock price data.
- **Company Suggestions**: Provides suggestions for big tech companies.
- **CORS Enabled**: Ensures secure cross-origin requests from the frontend.

## Technologies Used

- **Backend**: Flask
- **Data Processing**: NumPy, Pandas
- **Machine Learning**: Joblib
- **CORS Handling**: Flask-CORS

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Soham-Chaudhuri/Stock-Price-Predictor-2.0-backend.git
    cd Stock-Price-Predictor-2.0-backend
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```

2. The backend server will start on `http://127.0.0.1:5000/`.

## API Endpoints

### GET /

Returns a simple greeting message.
(Just for debugging purposes)

**Response**: `Hello world`

### GET /suggestData

Returns a list of big tech companies for suggestions.

**Response**: JSON array of company suggestions.

### POST /getChartData

Returns candlestick data for a given stock symbol.

**Request Body**: 
```json
{
    "id": "AAPL",
}
```

**Response**: JSON array of candlestick data.

### POST /predict

Returns a stock price prediction based on provided features.

**Request Body**:
```json
{
    "open": 150.00,
    "adj_close": 155.00,
    "high": 157.00,
    "low": 149.00,
    "volume": 1000000
}
```

**Response**: JSON containing the predicted price.

**Request Body**:
```json
{
    "prediction": 152.34
}
```

