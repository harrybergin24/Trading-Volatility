# Volatilty Trading

This project is involved in explaining and testing some of the trading strategies listed in (Z. Kakushadze and J.A. Serur. 151 Trading Strategies). I have always been interested in risk premia investing, I have now got to the technical level in my programming and mathematics to give a basic outline and create a simple backtest for one of the volatility trading strategies. 

 # Variance Swaps   
Here I back test a variance swap strategy, the conditions to enter a position is based of the deviations from the mean of the VRP, high upward deviations sell vol and vice versa. The Current version is below and I am currently working on the updated version, which goes into a lot more depth into the mathematics behind the link between replication and the VIX. I am also go into a lot more depth into the forecasting of future volatility using GARCH, as well as showing the distribution of volatility over the last 20 years or so. In the back test I also test the strategy on in and out of sample data, analysing these results and then comparing them to the Nasdaq. I am also going to add an appendix highlighting the link between the gamma formula and the volatility. 
Checklist updated version: 
| File | Description | Results |
|---|---|---|
|[Introduction and Motivation](<Variance_swap_trading/FinalVS/Introduction_1.ipynb>)| Theory behind variance swaps|  Done |
|[Defining the VRP](<Variance_swap_trading/FinalVS/Introduction_to_VRP.pdf>)| Defining the VIX| Done|
|[Variance Swaps](<Variance_swap_trading/FinalVS/Variance%20Swaps.ipynb>)|Explain the convex payoff of variance swaps and Greeks |Done|
|[Justifying Use of the VIX](<Variance_swap_trading/FinalVS/Justifying_the_use_of_the_VIX__through_replication.pdf>)| The mathematics behind it all| Done |
|[Back Test](<(Variance_swap_trading/FinalVS/Backtest_Final_VS_Copy1.ipynb)>)  |GARCH, VRP and culmative returns| Done|
| PnL Analysis | Trying to explain the returns and compare to other methods| Not done yet|



### [Introduction and Motivation](<Variance_swap_trading/FinalVS/Introduction_1.ipynb>) :
I give motivation for investigating volatility as tradeable quantity. I show the example of selling puts being historically a very lucrative strategy. 

### [Defining the VRP](<Variance_swap_trading/FinalVS/Introduction_to_VRP.pdf>) :
I explain and give the mathematical definition of the Volatility risk premium. 

### [Variance Swaps](<Variance_swap_trading/FinalVS/Variance%20Swaps.ipynb>) :
In this section I plot the payoff of a variance swap showing that its payoff is convex in volatility, I also show this mathematically. I am currently adding to this the different Greeks of a variance swap to identify is sensitivities. 


### [Justifying Use of the VIX](<Variance_swap_trading/FinalVS/Justifying_the_use_of_the_VIX__through_replication.pdf>) :
This part is the mathematics behind using the VIX for the S&P 500, which can be generalised to other incides and single stocks with their own volatility measure index.

### [Back Test](<(Variance_swap_trading/FinalVS/Backtest_Final_VS_Copy1.ipynb)>) :
This is the main part of the project computationally speaking. 

### PnL Analysis :





## Structuring Aspect
In the future I want to do some work on the pricing of forwards and options on variance swaps. Options will require some more work due to the stochastic volatility models required, which I am going to learn. 

| File | Description | Results |
|---|---|---|
|Variance swap pricer and greeks| Build a pricer and mark-to-market calculator| Not done yet|
|Forward Variance swap pricer |pricing and replicating forwards on variance swaps | Not done yet|

