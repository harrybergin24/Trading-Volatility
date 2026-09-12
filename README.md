# Volatilty Trading

This project is involved in explaining and testing some of the trading strategies listed in (Z. Kakushadze and J.A. Serur. 151 Trading Strategies). I have always been interested in risk premia investing, I have now got to the technical level in my programming and mathematics to give a basic outline and create a simple backtest for one of the volatility trading strategies. 

 ## [Variance Swaps](<Variance_swap_trading/variance_swap.md>)  
Here I back test a variance swap strategy, the conditions to enter a position is based of the deviations from the mean of the VRP, high upward deviations sell vol and vice versa. The Current version is below and I am currently working on the updated version, which goes into a lot more depth into the mathematics behind the link between replication and the VIX. I am also go into a lot more depth into the forecasting of future volatility using GARCH, as well as showing the distribution of volatility over the last 20 years or so. In the back test I also test the strategy on in and out of sample data, analysing these results and then comparing them to the Nasdaq. I am also going to add an appendix highlighting the link between the gamma formula and the volatility. 

| File | Description | Results |
|---|---|---|
|[Backtest](<Variance_swap_trading/Variance%20swap%20backtes%20OOSt.ipynb>)|Back testing on S&P 500| sharpe ratio and other metrics |
|[SPX VRP vs NDAQ VRP](<Variance_swap_trading/Difference%20in%20Between%20VRP%20for%20NDAQ%20and%20SPX.ipynb>)|I try highlight causes for the Difference in returns between NDAQ and SPX| Correlation between S&P VRP and NDAQ VRP has increased dramatically over the last 3 years|


Checklist updated version: 
| File | Description | Results |
|---|---|---|
|[Introduction and Motivation](<Variance_swap_trading/FinalVS/Introduction_1.ipynb>)| Theory behind variance swaps|  Done |
|[Defining the VRP](<Variance_swap_trading/FinalVS/Introduction_to_VRP.pdf>)| Defining the VIX| Done|
|[Variance Swaps](<Variance_swap_trading/FinalVS/Variance%20Swaps.ipynb>)|Explain the convex payoff of variance swaps |Done|
|[Justifying Use of the VIX](<Variance_swap_trading/FinalVS/Justifying_the_use_of_the_VIX__through_replication.pdf>)| The mathematics behind it all| Done |
|Forecasting volatility and term structure|Use GARCH(1,1) to forecast future vol |In progress|
|Back Test  |Back test on in and out of sample| Not done yet|
| Comparison |Look at other methods of trading vol | Not done yet|
| Appendix A |Link to delta hedged portfolio payoff | Not done yet|


