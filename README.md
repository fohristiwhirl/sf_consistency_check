# sf_consistency_check

You must add your API key to the source files in the obvious place.

* quote_check: runs a repeated sequence of orders on TESTEX and shows when the quote was not updated. [Bug report](https://discuss.starfighters.io/t/some-successful-orders-dont-touch-the-quote/4765).
* quote_simul_check: runs orders which generate 2 fills at once, and shows what the claimed last trade is. [Bug report](https://discuss.starfighters.io/t/when-2-fills-occur-at-once-it-is-arbitrary-which-one-sets-the-quote/4725).
