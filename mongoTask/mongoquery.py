from pandas import test
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["test"]

mycol = mydb["Market"]

mylist =[
{"Nasdaq Traded": "Y", "Symbol": "A", "Security Name": "Agilent Technologies, Inc. Common Stock", "Listing Exchange": "N", "Market Category": " ", "ETF": "N", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "NaN", "CQS Symbol": "A", "NASDAQ Symbol": "A", "NextShares": "N"},
{"Nasdaq Traded": "Y", "Symbol": "AA", "Security Name": "Alcoa Corporation Common Stock ", "Listing Exchange": "N", "Market Category": " ", "ETF": "N", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "NaN", "CQS Symbol": "AA", "NASDAQ Symbol": "AA", "NextShares": "N"},
{"Nasdaq Traded": "Y", "Symbol": "AAAU", "Security Name": "Perth Mint Physical Gold ETF", "Listing Exchange": "P", "Market Category": " ", "ETF": "Y", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "NaN", "CQS Symbol": "AAAU", "NASDAQ Symbol": "AAAU", "NextShares": "N"},
{"Nasdaq Traded": "Y", "Symbol": "AACG", "Security Name": "ATA Creativity Global - American Depositary Shares, each representing two common shares", "Listing Exchange": "Q", "Market Category": "G", "ETF": "N", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "N", "CQS Symbol": "NaN", "NASDAQ Symbol": "AACG", "NextShares": "N"},
{"Nasdaq Traded": "Y", "Symbol": "AADR", "Security Name": "AdvisorShares Dorsey Wright ADR ETF", "Listing Exchange": "P", "Market Category": " ", "ETF": "Y", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "NaN", "CQS Symbol": "AADR", "NASDAQ Symbol": "AADR", "NextShares": "N"},
{"Nasdaq Traded": "Y", "Symbol": "AAL", "Security Name": "American Airlines Group, Inc. - Common Stock", "Listing Exchange": "Q", "Market Category": "Q", "ETF": "N", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "N", "CQS Symbol": "NaN", "NASDAQ Symbol": "AAL", "NextShares": "N"},
{"Nasdaq Traded": "Y", "Symbol": "AAMC", "Security Name": "Altisource Asset Management Corp Com", "Listing Exchange": "A", "Market Category": " ", "ETF": "N", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "NaN", "CQS Symbol": "AAMC", "NASDAQ Symbol": "AAMC", "NextShares": "N"},
{"Nasdaq Traded": "Y", "Symbol": "AAME", "Security Name": "Atlantic American Corporation - Common Stock", "Listing Exchange": "Q", "Market Category": "G", "ETF": "N", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "N", "CQS Symbol": "NaN", "NASDAQ Symbol": "AAME", "NextShares": "N"},
{"Nasdaq Traded": "Y", "Symbol": "AAT", "Security Name": "American Assets Trust, Inc. Common Stock", "Listing Exchange": "N", "Market Category": " ", "ETF": "N", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "NaN", "CQS Symbol": "AAT", "NASDAQ Symbol": "AAT", "NextShares": "N"},
{"Nasdaq Traded": "Y", "Symbol": "AAU", "Security Name": "Almaden Minerals, Ltd. Common Shares", "Listing Exchange": "A", "Market Category": " ", "ETF": "N", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "NaN", "CQS Symbol": "AAU", "NASDAQ Symbol": "AAU", "NextShares": "N"},
{"Nasdaq Traded": "Y", "Symbol": "A", "Security Name": "Agilent Technologies, Inc. Common Stock", "Listing Exchange": "N", "Market Category": " ", "ETF": "N", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "NaN", "CQS Symbol": "A", "NASDAQ Symbol": "A", "NextShares": "N"},
{"Nasdaq Traded": "Y", "Symbol": "AA", "Security Name": "Alcoa Corporation Common Stock ", "Listing Exchange": "N", "Market Category": " ", "ETF": "N", "Round Lot Size": 100.0, "Test Issue": "N", "Financial Status": "NaN", "CQS Symbol": "AA", "NASDAQ Symbol": "AA", "NextShares": "N"}
]

x = mycol.insert_many(mylist)

# show all the data in test
for x in mycol.find():
  print(x)





