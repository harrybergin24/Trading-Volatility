import matplotlib.pyplot as plt
import pandas as pd   
import yfinance as yf
import numpy as np

spx = yf.download("^GSPC", start="2000-01-01", end="2026-01-01")
vix = yf.download("^VIX", start="2000-01-01", end="2026-01-01")


prices_spx = spx["Close"].squeeze()
prices_vix = vix["Close"].squeeze()
#daily log prices for the S&P 500 

log_return_daily = np.log(prices_spx).diff()

Kvar = (prices_vix / 100) ** 2


window = 30

# now use previous variance to come up with an estimate value for what Kvar should be

daily_variance_forecast = log_return_daily.rolling(window).var()

forecast_30d_variance = 30 * daily_variance_forecast



# So we have our log prices now we can make signal 

# rules we will implement

# we go long/ short variance depeing on our expectation for variance

# our signal is Kvar - E[RV], the markets expected variance vs ours

# this is VRP 



vrp = Kvar - forecast_30d_variance 

mean =vrp.mean()
std = vrp.std()

vrp_z = (vrp - mean ) / std 

vrp_z = vrp_z.dropna()

print(vrp_z)

position = 0 # 0 nothign , 1 long var swap, -1 short var swap 

positions = [] 
entry_req = 0.5
Trading_days = 0


# pretty similar to the 

for z in vrp_z:
    entry_today = 0
    if position == 0:
        if z > entry_req:
            position = -1
            entry_today = -1
            Trading_days = 0
        elif z < -entry_req:
            position = 1 # short var
            entry_today = 1
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

payoff = position * (realised_var_30d - Kvar.loc[entry_record.index])

var_swap_return = 1 + payoff


plt.plot(var_swap_return)
plt.title("Strategy Payoff Over Time")
plt.savefig("Variance_swap_trading/Figures/variance_swap_return")
plt.close()
#entries_full = pd.DataFrame({
    #"Position": entry_record,
   # "Kvar": Kvar.loc[entry_record.index],
   # "RealizedVar_30d": realised_var_30d
#})
cumulative_payoff = (payoff + 1).cumprod() - 1
plt.plot(cumulative_payoff)
plt.title("Cumulative Strategy Payoff Over Time")
plt.savefig("Variance_swap_trading/Figures/cumlative_variance_swap_return")
plt.close()









