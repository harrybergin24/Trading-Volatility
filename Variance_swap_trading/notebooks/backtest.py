import matplotlib.pyplot as plt
import pandas as pd   
import yfinance as yf
import numpy as np


spx = yf.download("^GSPC", start="1995-01-01", end="2026-08-01")

vix = yf.download("^VIX", start="1995-01-01", end="2026-08-01")


prices_spx = spx["Close"].squeeze()
prices_vix = vix["Close"].squeeze()
#daily log prices for the S&P 500 

log_return_daily = np.log(prices_spx).diff()

Kvar = (prices_vix / 100) ** 2


window = 21

# now use previous variance to come up with an estimate value for what Kvar should be

daily_variance_forecast = log_return_daily.rolling(window).var()

prev_15_day_var = log_return_daily.rolling(15).var() *252
prev_30_day_var = log_return_daily.rolling(30).var() *252
prev_60_day_var = log_return_daily.rolling (60).var() *252
prev_90_day_var = log_return_daily.rolling(90).var() *252

forecast_variance = 0.5*prev_15_day_var + 0.3*prev_30_day_var + 0.15*prev_60_day_var + 0.05*prev_90_day_var



# So we have our log prices now we can make signal 

# rules we will implement

# we go long/ short variance depeing on our expectation for variance

# our signal is Kvar - E[RV], the markets expected variance vs ours

# this is VRP 



vrp = Kvar - forecast_variance 
# orginally made a look forward error here using the total 
#std and mean for the whole data set when should on rolling baiss


roll_mean = vrp.expanding(min_periods=252).mean()


roll_std = vrp.expanding(min_periods=252).std()


vrp_z = ((vrp - roll_mean) / roll_std).dropna() 

#vrp_z = vrp_z[(vrp_z.index >= "2018-01-01") &]    
vrp_z = vrp_z[vrp_z.index >= "2018-01-01"]   # out-of-sample

print(vrp_z)

position = 0 # 0 nothign , 1 long var swap, -1 short var swap 

positions = [] 
entry_req = 0.20
Trading_days = 0


# adapted from my pairs trading project

for z in vrp_z:
    entry_today = 0
    if position == 0:
        if z > entry_req:
            position = -1
            entry_today = -1
            Trading_days = 0
    else:
        Trading_days += 1
        if Trading_days >= 30:
            position = 0
            Trading_days = 0
    positions.append(entry_today)

positions_series = pd.Series(positions, index=vrp_z.index, name="Position")

# keep only the rows where a position was actually entered (1 or -1)
entry_record = positions_series[positions_series != 0]
positions_series = pd.Series(positions, index=vrp_z.index, name="Position")

# keep only the rows where a position was actually entered (1 or -1)
entry_record = positions_series[positions_series != 0]

print(entry_record)

# so entry record is important as it gives the start date of the swap and weather we are shorting or going long 
realised_var_30d = {}
for date in entry_record.index:
    loc = log_return_daily.index.get_loc(date) # so we find this data in the daily log returns 

    # find the next 30 days of log returns

    future_returns = log_return_daily.iloc[loc + 1 : loc + 1 + window]
    if len(future_returns) == window:
        realised_var_30d[date] = (future_returns ** 2).sum() * (252 / window)
    else:
        realised_var_30d[date] = np.nan



realised_var_30d = pd.Series(realised_var_30d, name="RealisedVar_30d")

payoff = entry_record * (realised_var_30d - Kvar.loc[entry_record.index])




plt.plot(payoff)
plt.title("Strategy Payoff Over Time")
plt.savefig("Variance_swap_trading/Figures/variance_swap_return_spx")
plt.close()
#entries_full = pd.DataFrame({
    #"Position": entry_record,
   # "Kvar": Kvar.loc[entry_record.index],
   # "RealizedVar_30d": realised_var_30d
#})
cumulative_payoff = (payoff).cumsum()

mean_payoff = payoff.mean()
std_payoff = payoff.std()

sharpe_per_payoff = mean_payoff / std_payoff

trades_per_yr = len(payoff) / 26

sharpe_annual = sharpe_per_payoff * np.sqrt(trades_per_yr)


print(sharpe_annual)

plt.plot(cumulative_payoff)

plt.title("Adapted Vol Forecast SPX VS returns")
plt.figtext(0.5, 0.01, f"Sharpe_In_Sample: {sharpe_annual:.2f}", ha="center", fontsize=9)
plt.savefig("Variance_swap_trading/Figures/Adapted_vol_forecast_SPX_returns_OFS", dpi= 65)
plt.close()









