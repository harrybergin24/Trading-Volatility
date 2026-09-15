# Volatilty Trading

This project is involved in explaining and testing some of the trading strategies listed in (Z. Kakushadze and J.A. Serur. 151 Trading Strategies). I have always been interested in risk premia investing, I have now got to the technical level in my programming and mathematics to give a basic outline and create a simple backtest for one of the volatility trading strategies. 

 # Variance Swaps   
Here I back test a variance swap strategy, the conditions to enter a position is based of the deviations from the mean of the VRP, high upward deviations sell vol and vice versa. The Current version is below and I am currently working on the updated version, which goes into a lot more depth into the mathematics behind the link between replication and the VIX. I am also go into a lot more depth into the forecasting of future volatility using GARCH, as well as showing the distribution of volatility over the last 20 years or so. In the back test I also test the strategy on in and out of sample data, analysing these results and then comparing them to the Nasdaq. I am also going to add an appendix highlighting the link between the gamma formula and the volatility. 

| File | Description | Results |
|---|---|---|
|[Introduction and Motivation](<Variance_swap_trading/FinalVS/Introduction_1.ipynb>)| Theory behind variance swaps|  Done |
|[Defining the VRP](<Variance_swap_trading/FinalVS/Introduction_to_VRP.pdf>)| Defining the VIX| Done|
|[Variance Swaps](<Variance_swap_trading/FinalVS/Variance%20Swaps.ipynb>)|Explain the convex payoff of variance swaps and Greeks |Done|
|[Justifying Use of the VIX](<Variance_swap_trading/FinalVS/Justifying_the_use_of_the_VIX__through_replication.pdf>)| The mathematics behind it all| Done |
|[Back Test](<Variance_swap_trading/FinalVS/Backtest_SPX_FINAL.ipynb>)  |GARCH, VRP and culmative returns| Done|
| PnL Analysis | Trying to explain the returns and compare to other methods| Not done yet|

Key discoveries and findings:
- For the optimisation of the z-score parameter it would of course choose a value very close to zero as a majority of the time $VRP > 0$, so I have adapted the strategy to have two different entry parameters for entering a short variance swap and a long variance swap.

- The returns are disappointing, this is caused by the large tail risk of shorting volatility espcially for variance swaps being short 'vol of vol'. 

- The strategy performs better on the Nasdaq, I hypothesise: the performance is better due to tech stocks having traits conducive to investors over estimating future volatility, therefore short volatility strategies are effective. These traits of tech stocks include having high valuation multiples, low return on invested capital and an especially important idea of concentration risk amongst the 100 stocks in the index

Future Additions:
- Instead of going through the strategy returns for each index or asset it is tested on would be quite time consuming, I think it would be more useful to try and gain a general rule between the traits of a asset and what makes trading its volatility profitable or not. This is currently what I am working on, trying to identify across assets from gold to the russell 2000 to try and identify a pattern

- I have to change the amount of for loops, as currently it is quite slow. I am going to take Harvard's course on Data Structures and Algorithms to hopefully learn more to speed this up




## Structuring Aspect
In the future I want to do some work on the pricing of forwards and options on variance swaps. Options will require some more work due to the stochastic volatility models required, which I am going to learn. 

| File | Description | Results |
|---|---|---|
|Variance swap pricer and greeks| Build a pricer and mark-to-market calculator| Not done yet|
|Forward Variance swap pricer |pricing and replicating forwards on variance swaps | Not done yet|

