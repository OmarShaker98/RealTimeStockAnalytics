# Flask Stock API

This project is a Flask-based API for generating simulated stock data for various companies. It provides an endpoint to fetch stock data that updates in intervals, mimicking real-time stock price changes.

## Features

- Provides stock data for well-known companies like AAPL, MSFT, GOOGL, and more.
- Simulates realistic stock data with open, close, high, low prices, volume, and adjusted close.
- Uses a random distribution to generate stock price fluctuations to resemble real market behavior.

## API Endpoint

### `/stock_data`

- **Method**: GET
- **Description**: Returns the stock data of companies with updated prices in intervals.
- **Response Format**: JSON containing stock information like Date, Time, Open, High, Low, Close, Volume, etc.

## Installation

1. Clone the repository:
    ```
    git clone <repository-url>
    ```
2. Navigate into the project directory:
    ```
    cd flask-stock-api
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Running the API

1. To start the Flask server, execute the following command:
    ```
    python api.py
    ```
2. The API will run on `http://127.0.0.1:5000/` by default.

3. Access the stock data by visiting:
    ```
    http://127.0.0.1:5000/stock_data
    ```

## Dependencies

- Flask: Web framework for building the API.
- Pandas: Used for data manipulation.
- NumPy: Used for generating random numbers to simulate stock price changes.

## License

This project is licensed under the MIT License.
