#!/usr/bin/python

from flask import Flask, render_template
from stocks import *


app = Flask(__name__)

@app.route('/')
def test():
  return "hello world"

#dynamic url for stock value
@app.route('/<ticker>')
def stock(ticker):
  stock = Stock(str(ticker))
  
  try:    
    vals = stock_bird(stock)
  except Exception as e:
    return str(e)
  
  return str(vals)



# running flask in port 8080 at the moment
if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 8080)


