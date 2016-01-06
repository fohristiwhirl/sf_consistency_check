import time
import stockfighter_minimal as sf

INFO = sf.Order()

INFO.account = "EXB123456"
INFO.venue = "TESTEX"
INFO.symbol = "FOOBAR"

sf.change_api_key("YOUR API KEY HERE")      # <----------------------- FIX THIS

while 1:

    print("Clearing the book... (2 orders)")
    INFO.qty = 999999
    INFO.orderType = "market"
    INFO.price = 1
    INFO.direction = "buy"
    r = sf.execute(INFO)
    print("Last ID was {}".format(r["id"]))
    INFO.direction = "sell"
    r = sf.execute(INFO)
    print("Last ID was {}".format(r["id"]))
    
    print("Placing limit order...")
    INFO.orderType = "limit"
    INFO.price = 5000
    INFO.qty = 50
    INFO.direction = "sell"
    r = sf.execute(INFO)
    print("Last ID was {}".format(r["id"]))
    
    print("Buying 40 of it back...", end = "")
    INFO.qty = 40
    INFO.direction = "buy"
    r = sf.execute(INFO)
    print(r["fills"])
    print("Last ID was {}".format(r["id"]))
    
    print("Buying final 10 with market...", end = "")
    INFO.qty = 10
    INFO.direction = "buy"
    INFO.orderType = "market"
    r = sf.execute(INFO)
    print(r["fills"])
    print("Last ID was {}".format(r["id"]))
    q = sf.quote(INFO.venue, INFO.symbol)
    ls = q["lastSize"]
    print("Last size was {}".format(ls), end = "")
    if ls != 10:
        print("   <---------------------------------------")
        time.sleep(5)
        q = sf.quote(INFO.venue, INFO.symbol)
        print("After 5 seconds: Last size was {}".format(q["lastSize"]))
    else:
        print()
