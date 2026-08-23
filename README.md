# Trading-Volatility

This project is involved in explaining and testing some of the trading strategies listed in (Z. Kakushadze and J.A. Serur. 151 Trading Strategies). I have always been interested in risk premia investing, I have now got to the technical level in my programming and mathematics to give a basic outline and create a simple backtest for one of the volatility trading strategies. In the future as I develop my techincal skills I hope to dive deeper, explaining and breaking down the replication stratergy for the variance swaps. Some other stratergies I hope to adress in the future is trading volatility, specifically the volatility risk premium(VRP), using gamma hedging. 

 ## [Variance Swaps](<Variance_swap_trading/variance_swap.md>)  

Here I backtest a variance swap strategy by attempting to use vix as a estimator of the 'fair strike', using a z-score of the Volatility Risk Premium, the premium investors are willing to pay to avoid negative returns, seen through investors willing to pay high put prices pushing up implied volatility, creating this idea we are hoping to exploit 'expensive' volatility. I explain the theory behind variance swaps, in the link above, and then in [Backtest](<Variance_swap_trading/backtest.md>) I walk through my signal explaining my logic and code, finallly showing the results of the out of sample backtesting. 
