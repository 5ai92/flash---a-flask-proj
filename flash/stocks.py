#author : bhargav sai dama

from googlefinance import getQuotes
from yahoo_finance import Share
# import timeit

class Stock:
    stockcount = 0
    
    def __init__(self, symbol):
        Stock.stockcount += 1
        self.symbol = symbol
    
    def display_count(self):
        return "Total count of stocks %s" %(Stock.stockcount)
    
    def display_stock(self):
        return "Company symbol : %s" %(self.symbol)
    
    def current(self):       
        open_price = float(Share(self.symbol).get_open())
        curr_price = float(getQuotes(self.symbol)[0]['LastTradeWithCurrency'])
        change_price = round((curr_price-open_price),2)
        change_percent =round(((change_price/open_price) * 100), 2)        
        return (open_price, curr_price, change_price, change_percent)
        
    
    def historical_volume(self, from_date, to_date):
        historical = Share(self.symbol).get_historical(from_date, to_date)
        return historical
        
    def fundementals(self):
        marketcap = (Share(self.symbol).get_market_cap())
        bookvalue = Share(self.symbol).get_book_value()
        dividend = Share(self.symbol).get_dividend_share()
        dividend_paydate = Share(self.symbol).get_dividend_pay_date()
        dividend_yield = Share(self.symbol).get_dividend_yield()
        
        return (marketcap, bookvalue, dividend, dividend_paydate, dividend_yield)

      
def stock_bird(stock):
   
#    print start_time = timeit.default_timer()
    
#     key_name = ('symbol', 'open_price', 'curr_price', 'change_price', 'change_perccent', 'marketcap', 'bookvalue', 'dividend', 'dividend_paydate', 'dividend_yield')
#     vals = (stock.display_stock(), stock.current(), stock.fundementals())

#    printtimeit.default_timer() - start_time)

    return (stock.display_stock(), stock.current(), stock.fundementals())
    

if __name__ == '__main__':
    stock_bird()

        
        
