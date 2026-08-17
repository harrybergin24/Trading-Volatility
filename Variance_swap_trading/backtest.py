import matplotlib as plt
import pandas as pd   
import yfinance as yf

spx = yf.download("^GSPC", start="2000-01-01", end="2026-01-01")

prices = spx.close()

#daily log prices for the S&P 500 

log_prices_n = np.log(prices)