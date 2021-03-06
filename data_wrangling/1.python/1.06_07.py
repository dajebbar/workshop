stocks = {
    "Solar Capital Ltd.":"$920.44M",
    "Zoe's Kitchen, Inc.":"$262.32M",
    "Toyota Motor Corp Ltd Ord":"$156.02B",
    "Nuveen Virginia Quality Municipal Income Fund":"$238.33M",
    "Kinross Gold Corporation":"$5.1B",
    "Vulcan Materials Company":"$17.1B",
    "Hi-Crush Partners LP":"$955.69M",
    "Lennox International, Inc.":"$8.05B",
    "WMIH Corp.":"$247.66M",
    "Comerica Incorporated":"n/a",
}

print(stocks["WMIH Corp."])
print(stocks.get("WMIH Corp", 'not found'))
stocks["WMIH Corp."] = "$300M"

# remove $ and M

stocks_clean = {k:v.replace('$', '').replace('M', '').replace('B', '') for k, v in stocks.items()}
# print(stocks_clean)

# split price and value(M, B)
stocks_clean_2 = {k: [v[:-1].replace('$', ''), v[-1]] for k, v in stocks.items()}
print(stocks_clean_2)