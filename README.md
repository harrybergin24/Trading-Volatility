# Volatilty Trading

This project is involved in explaining and testing some of the trading strategies listed in (Z. Kakushadze and J.A. Serur. 151 Trading Strategies). I have always been interested in risk premia investing, I have now got to the technical level in my programming and mathematics to give a basic outline and create a simple backtest for one of the volatility trading strategies. In the future as I develop my techincal skills I hope to dive deeper, explaining and breaking down the replication stratergy for the variance swaps. Some other stratergies I hope to adress in the future is trading volatility, specifically the volatility risk premium(VRP), using gamma hedging. 

 ## [Variance Swaps](<Variance_swap_trading/variance_swap.md>)  

Here I backtest a variance swap strategy by attempting to use VIX as a estimator of the 'fair strike', using a z-score of the Volatility Risk Premium, the premium investors are willing to pay to avoid negative returns, seen through investors willing to pay high put prices pushing up implied volatility, creating this idea we are hoping to exploit 'expensive' volatility.
| File | Description | Results |
|---|---|---|
|[Variance Swap](<Variance_swap_trading/variance_swap.md>)|Explation and theory behind variance swaps| I show that they have convex payoffs |
|[Backtest](<Variance_swap_trading/Variance%20swap%20backtes%20OOSt.ipynb>)|Back testing on S&P 500| sharpe ratio and other metrics |
|[SPX VRP vs NDAQ VRP](<Variance_swap_trading/Difference%20in%20Between%20VRP%20for%20NDAQ%20and%20SPX.ipynb>)|I try highlight causes for the Difference in returns between NDAQ and SPX| Correlation between S&P VRP and NDAQ VRP has increased dramatically over the last 3 years|

I have updated this to forecast volatility using GARCH(1,1), I backtest garch on in and out of sample data because garch relies on historical data to fit the paramters. This is where the importance of in and out of sample backtesting comes in. 

Checklist updated version: 
| File | Description | Results |
|---|---|---|
|[Introduction and Motivation](</Variance_swap_trading/FinalVS/Introduction_1.ipynb>)| Theory behind variance swaps|  Done |
|[Defining the VRP](</Variance_swap_trading/FinalVS/Introduction_to_VRP.pdf>)| Defining the VIX| done|
|Justifying Use of the VIX| Find $K_{Var}$| Not done yet |
|Forecasting Volaitlty |Use Garch to forecast future vol | Not done yet|
|Back Test  |Back test on in and out of sample| Not done yet|
| Comparison |Look at other methods of trading vol | Not done yet|

## VRP Trading with gamma hedging

This is another stratergy I would like to explore in the future, however, first I will need to improve my mathematics. This is why I am taking Topics in mathematics with applications to Finance, along with reading 'Mastering python for finance' to ensure I can program these intresting ideas. 

