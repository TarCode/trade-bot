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

    try:
        opts, args = getopt.getopt(argv, "hp:c:", ["period=","currency="])
    except getopt.GetoptError:
        print('main.py -p <period> -c <currency pair>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("main.py -p <period> -c <currency pair>")
            sys.exit()
        elif opt in ("-p", "--period"):
            if int(arg) in [300, 900, 1800, 7200, 14400, 86400]:
                period = arg
            else:
                print("Poloniex requires periods in 300, 900, 1800, 7200, 14400, 86400")
                sys.exit(2)

    KEY = os.getenv("POLONIEX_KEY")
    SECRET = os.getenv("POLONIEX_SECRET")
    conn = Poloniex(KEY, SECRET)

    while True:
        currentValues = conn.returnTicker()
        lastPairPrice = currentValues[pair]["last"]
        print("{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " Period ", period, pair, lastPairPrice )
        time.sleep(int(period))

if __name__ == "__main__":
    main(sys.argv[1:])