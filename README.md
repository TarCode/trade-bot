# Simple crypto trading bot

A very simple trading bot based on [this repo and video tutorial](https://github.com/bwentzloff/trading-bot). Pretty much just an updated version of the simple moving average trade bot using Python 3.5 and the latest Poloniex Python Client wrapper.

## How to run
An example run script can be found in `run.sh`.
Create a `.env` file with your `POLONIEX_KEY`, `POLONIEX_SECRET`.

### Run with historic data
`python main.py -p 300 -c BTC_ETH -n 20 -s 1491048000 -e 1491091200`

### Run with live data
`python main.py -p 300 -c BTC_ETH -n 20`

`-p`: interval in milliseconds

`-c`: Currency pair (Poloniex specified format)

`-n`: Period of moving avg

`-s`: Start date in unix time

`-e`: End date in unix time