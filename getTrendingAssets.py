import re

def cleanArray(a):
    p = []
    for index, item in enumerate(a):
        if index != 0:
            item = float(re.sub(r'^[^ ]* ','',item))
        p.append(item)
    return {p[0].split(',')[0]: 1 if p[5] > p[1] and p[5] > p[2] and p[5] > p[3] and p[5] > p[4] 
                else (-1 if p[5] < p[1] and p[5] < p[2] and p[5] < p[3] and p[5] < p[4] else 0)}

inputD = dict()
file_path = "C:\\Users\\redar\\AppData\\Roaming\\MetaQuotes\\Terminal\\Common\\Files\\LiquidStocksInfo.csv"
with open(file_path, "r") as file:
    tickerTrends = {}
    for index, line in enumerate(file):
        if index > 0:
            first_key, first_value = next(iter(cleanArray(line.split(' | ')).items()))
            c = tickerTrends[first_key] if first_key in tickerTrends else None
            tickerTrends[first_key] = first_value if c is None else (0 if c != first_value else c)
    [print(res) for res in[k for k, v in reversed(tickerTrends.items()) if v == 1 or v == -1]]

