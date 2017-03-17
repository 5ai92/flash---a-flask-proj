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
  True
  while True:
    try:    
      vals = stock_bird(stock)
      pe = round((vals[2]/vals[10]),2)
#       return str(vals)
      return render_template("stockpage.html", vals = vals, pe = pe)

    except Exception as e:
      while len(str(e)) > 0:
        vals = stock_bird(stock)
#         return str(vals)# added loop to avoid type error
        return render_template("stockpage.html", vals = vals)
  return render_template("stockpage.html", vals = vals) 
       


# running flask in port 8080 at the moment
if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 8080, debug = True)


