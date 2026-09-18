# Variance Swap Strategy Back Test
In this project I back test 30-day variance swaps, which behave similarly to straddles due to their short expiration date. However, I cannot back test how straddles would have performed in the past due to a lack of historical options data. This is an issue I repeatedly run into throughout the project. This project is broken up into several different parts, each giving a mathematical and conceptual explanation for the results. I start by giving a motivating example, the large returns of selling puts previously generated. I then move on to why this explains the presence of the Volatility Risk Premium(VRP) and what this concept is. Then I move onto the method of extracting this premium from the market, variance swaps. After discussing this product I derive the replication formula, famously discovered by a team at Goldman Sachs. I then show the connection between this formula and the methodology of the VIX, supporting my method of using adapted VIX prices to estimate the swap’s strike value. To make our VRP I forecast realised volatility using GARCH and subtracting this from the 30-day Implied volatility, which the VIX calculates. I then use the mean reversion of the VRP, to make a signal based on the deviations from a mean(I test rolling and expanding as well). Then I optimise this signal for entry parameters having different entry requirements for short and long volatility. This then generates returns over time, I am now working on analysing these returns and attempting to spot a pattern across indices where the strategy performs well or badly on.
| File | Description | Results |
|---|---|---|
|[Introduction and Motivation](<Introduction_1.ipynb>)| Theory behind variance swaps|  Done |
|[Defining the VRP](<Introduction_to_VRP.pdf>)| Defining the VIX| Done|
|[Variance Swaps](<Variance_swap_trading/FinalVS/Variance%20Swaps.ipynb>)|Explain the convex payoff of variance swaps and Greeks |Done|
|[Justifying Use of the VIX](<Justifying_the_use_of_the_VIX__through_replication.pdf>)| The mathematics behind it all| Done |
|[Back Test](<Backtest_SPX_FINAL.ipynb>)  |GARCH, VRP and culmative returns| Done|
| PnL Analysis | Trying to explain the returns and compare to other methods| Not done yet|

Recent Changes:
- Walk Foward validiation for GARCH volatitily modelling
 
- Train and test split for entry paramater to enter a postion
 
- Replication Formula derivation for the Variance Swap

Key discoveries and findings:
- For the optimisation of the z-score parameter it would of course choose a value very close to zero as a majority of the time $VRP > 0$, so I have adapted the strategy to have two different entry parameters for entering a short variance swap and a long variance swap.

- The returns are disappointing, this is caused by the large tail risk of shorting volatility espcially for variance swaps being short 'vol of vol'. 

- The strategy performs better on the Nasdaq, I hypothesise: the performance is better due to tech stocks having traits conducive to investors over estimating future volatility, therefore short volatility strategies are effective. These traits of tech stocks include having high valuation multiples, low return on invested capital and an especially important idea of concentration risk amongst the 100 stocks in the index

Future Additions:
- Instead of going through the strategy returns for each index or asset it is tested on would be quite time consuming, I think it would be more useful to try and gain a general rule between the traits of a asset and what makes trading its volatility profitable or not. This is currently what I am working on, trying to identify across assets from gold to the russell 2000 to try and identify a pattern

- I have to change the amount of for loops, as currently it is quite slow. I am going to take Harvard's course on Data Structures and Algorithms to hopefully learn more to speed this up
