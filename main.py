import time
import sys, getopt
import datetime

def main(argv):
    period = 10

    try:
        opts, args = getopt.getopt(argv, "hp:", ["period=",])
    except getopt.GetoptError:
        print('main.py -p <period>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("main.py -p <period>")
            sys.exit()
        elif opt in ("-p", "--period"):
            if int(arg) in [300, 900, 1800, 7200, 14400, 86400]:
                period = arg
            else:
                print("Poloniex requires periods in 300, 900, 1800, 7200, 14400, 86400")
                sys.exit(2)
    while True:
        print("{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " Period ", period )
        time.sleep(int(period))

if __name__ == "__main__":
    main(sys.argv[1:])