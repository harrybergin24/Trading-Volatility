# Trading-Volatility

This project is involved in explaining and testing some of the trading strategies listed in (Z. Kakushadze and J.A. Serur. 151 Trading Strategies). I have always been interested in risk premia investing, I have now got to the technical level in my programming and mathematics to give a basic outline and create a simple backtest for one of the volatility trading strategies. In the future as I develop my techincal skills I hope to dive deeper, explaining and breaking down the replication stratergy for the variance swaps. Some other stratergies I hope to adress in the future is trading volatility, specifically the volatility risk premium(VRP), using gamma hedging. 

 ## [Variance Swaps](<Variance_swap_trading/variance_swap.md>)  

Here I backtest a variance swap strategy by attempting to use VIX as a estimator of the 'fair strike', using a z-score of the Volatility Risk Premium, the premium investors are willing to pay to avoid negative returns, seen through investors willing to pay high put prices pushing up implied volatility, creating this idea we are hoping to exploit 'expensive' volatility. I explain the theory behind variance swaps, in the link above, and then in [Backtest](<Variance_swap_trading/backtest.md>) I walk through my signal explaining my logic and code, finallly showing the results of the out of sample backtesting. I analyse and attempt to explain the results in [Conculsions](<Variance_swap_trading/Conculsions.md>)
| File | Description | Results |
|---|---|---|
|[Variance Swap](<Variance_swap_trading/variance_swap.md>)|Explation and theory behind variance swaps| I show that they have convex payoffs |
|[Backtest](<Variance_swap_trading/Variance Swap backtest Out Of sample.ipynb>)|Back testing on S&P 500| 0.19 Sharpe ratio |
|[Conculsions](<Variance_swap_trading/Conculsions.md>)|Explanations for the results| 0.43 Sharpe ratio when applied to the Nasdaq |

I have updated this to forecast volatitilty using GARCH(1,1).

## Investigating The VRP
In this file I start to look at VRP in a different angle instead of finding strategies to harvest this risk premia, I attempt to investiage how the VRP changes over time. I look at what are its componement parts, how it changes over time and why it changes. Then based of inputs about VRP what trades are the best to make and it has possible applciations to vol managed portfoilos.


## VRP Trading with gamma hedging

This is another stratergy I would like to explore in the future, however, first I will need to improve my mathematics. This is why I am taking Topics in mathematics with applications to Finance, along with reading 'Mastering python for finance' to ensure I can program these intresting ideas. 

