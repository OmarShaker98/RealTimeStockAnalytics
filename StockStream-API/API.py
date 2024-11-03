from flask import Flask, jsonify
import pandas as pd
import numpy as np
import datetime

app = Flask(__name__)

# Last day stock prices obtained from the API(basis for generating real-time stock prices)
last_day_data = {
    'AAPL': {'Open': 229.302370, 'High': 228.401188, 'Low': 227.919181, 'Close': 225.870195, 'Volume': 26968152, 'Adj_Close': 225.870195},
    'MSFT': {'Open': 439.249431, 'High': 444.316980, 'Low': 437.121727, 'Close': 436.370458, 'Volume': 2248293, 'Adj_Close': 436.370458},
    'GOOGL': {'Open': 160.348108, 'High': 160.077466, 'Low': 161.899219, 'Close': 160.250863, 'Volume': 2029748, 'Adj_Close': 160.250863},
    'NVDA': {'Open': 117.475374, 'High': 114.663048, 'Low': 116.726589, 'Close': 115.689777, 'Volume': 6111647, 'Adj_Close': 115.689777},
    'BRK-B': {'Open': 455.544448, 'High': 460.657246, 'Low': 449.713193, 'Close': 450.459087, 'Volume': 302757, 'Adj_Close': 450.459087},
    'MA': {'Open': 494.288076, 'High': 489.170497, 'Low': 489.545203, 'Close': 491.738821, 'Volume': 155824, 'Adj_Close': 491.738821},
    'V': {'Open': 283.131479, 'High': 281.719716, 'Low': 281.545518, 'Close': 281.855102, 'Volume': 291460, 'Adj_Close': 281.855102},
    'INTC': {'Open': 18.698638, 'High': 20.197653, 'Low': 19.607270, 'Close': 16.284552, 'Volume': 2649658, 'Adj_Close': 16.284552},
    'CSCO': {'Open': 53.191666, 'High': 51.385235, 'Low': 53.938300, 'Close': 53.305591, 'Volume': 646669, 'Adj_Close': 53.305591},
    'JPM': {'Open': 212.376572, 'High': 213.521196, 'Low': 209.153050, 'Close': 212.577946, 'Volume': 0, 'Adj_Close': 212.577946},
    'CRM': {'Open': 259.826751, 'High': 279.957341, 'Low': 260.164636, 'Close': 274.053843, 'Volume': 706230, 'Adj_Close': 274.053843},
    'BA': {'Open': 152.299397, 'High': 152.384058, 'Low': 147.600980, 'Close': 156.285653, 'Volume': 0, 'Adj_Close': 156.285653},
    'CAT': {'Open': 371.046966, 'High': 371.713140, 'Low': 355.802724, 'Close': 360.239195, 'Volume': 25700, 'Adj_Close': 360.239195},
    'CVX': {'Open': 142.042475, 'High': 152.486124, 'Low': 143.115103, 'Close': 150.258354, 'Volume': 1538476, 'Adj_Close': 150.258354},
    'HON': {'Open': 202.986851, 'High': 201.748839, 'Low': 195.619546, 'Close': 200.046871, 'Volume': 285364, 'Adj_Close': 200.046871},
    'IBM': {'Open': 213.055151, 'High': 223.390886, 'Low': 214.215539, 'Close': 220.710880, 'Volume': 628041, 'Adj_Close': 220.710880},
    'GS': {'Open': 500.961346, 'High': 503.670499, 'Low': 500.518944, 'Close': 500.610626, 'Volume': 270985, 'Adj_Close': 500.610626},
    'TRV': {'Open': 238.741602, 'High': 238.362589, 'Low': 237.306214, 'Close': 237.240820, 'Volume': 5890, 'Adj_Close': 237.240820},
    'XOM': {'Open': 124.661904, 'High': 121.620834, 'Low': 115.388487, 'Close': 115.840569, 'Volume': 1793096, 'Adj_Close': 115.840569},
    'COP': {'Open': 112.601956, 'High': 118.276416, 'Low': 111.418962, 'Close': 112.069706, 'Volume': 3763904, 'Adj_Close': 112.069706},
    'PSX': {'Open': 127.840882, 'High': 133.845734, 'Low': 127.947684, 'Close': 130.419884, 'Volume': 1024011, 'Adj_Close': 130.419884},
    'EOG': {'Open': 128.688208, 'High': 122.850268, 'Low': 125.115593, 'Close': 126.005450, 'Volume': 149880, 'Adj_Close': 126.005450},
}

companies = {
    'AAPL': ['Technology', 'Consumer Electronics'],
    'MSFT': ['Technology', 'Software'],
    'GOOGL': ['Communication Services', 'Internet Content'],
    'NVDA': ['Technology', 'Semiconductors'],
    'BRK-B': ['Financial Services', 'Insurance'],
    'MA': ['Financial Services', 'Credit Services'],
    'V': ['Financial Services', 'Credit Services'],
    'INTC': ['Technology', 'Semiconductors'],
    'CSCO': ['Technology', 'Communication Equipment'],
    'JPM': ['Financial Services', 'Banking'],
    'CRM': ['Technology', 'Software'],
    'BA': ['Industrials', 'Aerospace & Defense'],
    'CAT': ['Industrials', 'Construction Machinery'],
    'CVX': ['Energy', 'Oil & Gas'],
    'HON': ['Industrials', 'Conglomerates'],
    'IBM': ['Technology', 'IT Services'],
    'GS': ['Financial Services', 'Capital Markets'],
    'TRV': ['Financial Services', 'Insurance'],
    'XOM': ['Energy', 'Oil & Gas'],
    'COP': ['Energy', 'Oil & Gas'],
    'PSX': ['Energy', 'Refining & Marketing'],
    'EOG': ['Energy', 'Oil & Gas Exploration & Production']
}


current_datetime = datetime.datetime(2024, 10, 1, 14, 30, 0)
volume_dict = {company: values['Volume'] for company, values in last_day_data.items()}

def generate_stock_data(current_datetime):
    data = []
    for company, values in last_day_data.items():
        open_price = values['Open'] + np.random.normal(0, 2.5)
        close_price = values['Close'] + np.random.normal(0, 2.5)
        high_price = max(open_price, close_price) + np.random.normal(0, 2.5)
        low_price = min(open_price, close_price) - np.random.normal(0, 2.5)

        volume_change_range = int(0.1 * values['Volume'])
        if volume_change_range > 0:
            volume_change = np.random.randint(-volume_change_range + 1, volume_change_range + 1)
        else:
            volume_change = volume_dict[company] - 22375  # Set volume change to previous volume + 200
            new_volume = max(volume_dict[company] + volume_change, 1)  # Ensure new volume is at least 1
        new_volume = max(volume_dict[company] + volume_change, 1)  # Ensure new volume is at least 1
        volume_dict[company] = new_volume

        sector, industry = companies[company]
        date = current_datetime.date()
        time = current_datetime.time()

        data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Time': time.strftime('%H:%M:%S'),
            'Company': company,
            'Sector': sector,
            'Industry': industry,
            'Open': open_price,
            'High': high_price,
            'Low': low_price,
            'Close': close_price,
            'Adj_Close': close_price,
            'Volume': new_volume
        })
    
    return data

@app.route('/stock_data', methods=['GET'])
def stock_data():
    global current_datetime

    if current_datetime.time() > datetime.time(15, 55, 0):
        current_datetime = current_datetime.replace(hour=9, minute=30) + datetime.timedelta(days=1)
    
    stock_data = generate_stock_data(current_datetime)
    
    current_datetime += datetime.timedelta(minutes=5)  # Each Interval Date 

    return jsonify(stock_data)

if __name__ == '__main__':
    app.run(debug=True)

