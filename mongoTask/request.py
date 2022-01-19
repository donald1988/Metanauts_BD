import requests

url = "https://stock-market-data.p.rapidapi.com/market/exchange/nyse"

headers = {
    'x-rapidapi-host': "stock-market-data.p.rapidapi.com",
    'x-rapidapi-key': "5bde482e7fmshfb67387ed5218a7p1d29dfjsn586c97707a7f"
    }

#response = requests.request("GET", url, headers=headers)

#rep = response.json()
d_list = {}
while(True):
    for dt in d_list:
            
        querystring = {"Nasdaq Traded": "Y", "Symbol": "A", "Security Name": "Agilent Technologies, Inc. Common Stock", "Listing Exchange": "N", "Market Category": " ", "ETF": "N", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "NaN", "CQS Symbol": "A", "NASDAQ Symbol": "A", "NextShares": "N"}
    response = requests.request("GET", url, headers=headers, params=querystring)

    d_list.append(response)
    
    print(d_list.json())

    