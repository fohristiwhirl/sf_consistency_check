import time
import stockfighter_minimal as sf

account = "EXB123456"
venue = "TESTEX"
symbol = "FOOBAR"

sf.change_api_key("yourkeyhere")      # <----------------------- FIX THIS

while 1:

    print("Clearing the book... (2 orders)")
    
    o = {"account": account, "venue": venue, "stock": symbol, "qty": 999999, "orderType": "market", "price": 1, "direction": "buy"}
    r = sf.execute_d(o)
    print("Last ID was {}".format(r["id"]))
    
    o = {"account": account, "venue": venue, "stock": symbol, "qty": 999999, "orderType": "market", "price": 1, "direction": "sell"}
    r = sf.execute_d(o)
    print("Last ID was {}".format(r["id"]))
    
    print("Placing limit order...")

    o = {"account": account, "venue": venue, "stock": symbol, "qty": 50, "orderType": "limit", "price": 5000, "direction": "sell"}
    r = sf.execute_d(o)
    print("Last ID was {}".format(r["id"]))
    
    print("Buying 40 of it back...", end = "")

    o = {"account": account, "venue": venue, "stock": symbol, "qty": 40, "orderType": "limit", "price": 5000, "direction": "buy"}
    r = sf.execute_d(o)
    print(r["fills"])
    print("Last ID was {}".format(r["id"]))
    
    print("Buying final 10 with market...", end = "")

    o = {"account": account, "venue": venue, "stock": symbol, "qty": 10, "orderType": "market", "price": 5000, "direction": "buy"}
    r = sf.execute_d(o)
    print(r["fills"])
    print("Last ID was {}".format(r["id"]))

    q = sf.quote(venue, symbol)
    ls = q["lastSize"]
    print("Quote: lastSize was {}".format(ls), end = "")
    
    if ls != 10:
        print("   <---------------------------------------------------------")
        time.sleep(5)
        q = sf.quote(venue, symbol)
        print("After 5 seconds: Last size was {}".format(q["lastSize"]))
    else:
        print()
