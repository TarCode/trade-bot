import os
import time
import sys, getopt
import datetime
from poloniex import Poloniex

from dotenv import load_dotenv

load_dotenv()

def main(argv):
    period = 10
    pair="BTC_ETH"
    prices = []
    lengthOfMA = 0
    currentMovingAverage = 0

    try:
        opts, args = getopt.getopt(argv, "hp:c:n:", ["period=","currency=", "points="])
    except getopt.GetoptError:
        print('main.py -p <period> -c <currency pair> -n <period of moving average>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("main.py -p <period> -c <currency pair>")
            sys.exit()
        elif opt in ("-p", "--period"):
            if int(arg) in [10, 300, 900, 1800, 7200, 14400, 86400]:
                period = arg
            else:
                print("Poloniex requires periods in 300, 900, 1800, 7200, 14400, 86400")
                sys.exit(2)
        elif opt in ("-c", "--currency"):
            pair = arg
        elif opt in ("-n", "--points"):
            lengthOfMA = int(arg)
    KEY = os.getenv("POLONIEX_KEY")
    SECRET = os.getenv("POLONIEX_SECRET")
    conn = Poloniex(KEY, SECRET)

    while True:
        currentValues = conn.returnTicker()
        lastPairPrice = currentValues[pair]["last"]

        if len(prices) > 0:
            currentMovingAverage = sum(prices) / float(len(prices))


        print("{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " Period " + period + "s" + " Pair: " + pair + " Last pair price: " + str(lastPairPrice) + " Curr moving avg: " + str(currentMovingAverage) )
        prices.append(float(lastPairPrice))
        # prices = prices[-lengthOfMA]
        time.sleep(int(period))

if __name__ == "__main__":
    main(sys.argv[1:])