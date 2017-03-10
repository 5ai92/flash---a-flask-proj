#!/usr/bin/python

from flask import Flask
from stocks import *


app = Flask(__name__)

@app.route('/')
def test():
  return "hello world"

@app.route('/apple')
def stock():
  stock = Stock('aapl')
#   global stock1
#   company, open_price, curr_price, change_price, change_percent, marketcap, bookvalue, dividend, dividend_paydate, dividend_yield = stock_bird()
  d = stock_bird(stock)
  return d['company']


if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 8080)


