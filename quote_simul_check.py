import stockfighter_minimal as sf

sf.change_api_key("yourkeyhere")      # <----------------------- FIX THIS

order = sf.Order()

order.account = "EXB123456"
order.venue = "TESTEX"
order.symbol = "FOOBAR"

print("Reported last trade: (should be 96 @ 360, but sometimes is 5 @ 237)")

while 1:

	# Clear the book.......................

	order.orderType = "market"

	order.direction = "sell"
	order.qty = 999999
	order.price = 1

	sf.execute(order)

	order.direction = "buy"
	order.qty = 999999
	order.price = 1

	sf.execute(order)

	# -------------------------------------

	order.orderType = "limit"

	order.direction = "sell"
	order.qty = 5
	order.price = 237

	sf.execute(order)

	order.direction = "sell"
	order.qty = 96
	order.price = 360

	sf.execute(order)

	order.direction = "buy"
	order.qty = 96
	order.price = 360
	
	q = sf.quote(order.venue, order.symbol)
	print(q["lastSize"], "@", q["last"])

