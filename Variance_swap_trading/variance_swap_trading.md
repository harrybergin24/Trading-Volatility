

# Variance Swap Payoff

## Libaries

```python
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
```
## Payoff Function

Here we define our payoff funciton as outline in [Variance Swaps](<Variance_swap_trading/variance_swap.md>), we use $ P(T) = N \times (v(T)- K) $. We can see from here that the convexity arises,

```python
realised_vol = np.linspace(0, 0.50, 3000)
N = 1 
k = 0.20
vs_payoff = N * (realised_vol ** 2 - k ** 2)
```

## Plot Payoff Curve

```python
fig, ax = plt.subplots()
ax.plot(realised_vol, vs_payoff)
```

## Format the Axes

Here through youtube videos I learnt how to put the X-axis through the orgin point, this allows us to show the PnL of the swap better. 

```python
# put the x axis through 0 payoff

ax.spines['left'].set_position(('data', 0))

ax.spines['bottom'].set_position(('data', 0))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
```

## Making the graph

```python
ax.set_xlabel("realised vol")
ax.set_ylabel("Payoff Function")
plt.savefig("Variance_swap_trading/Figures/variance_swap_payoff.png")
plt.close()
```
![Variance Swap Payoff, Strike = 0.2](Figures/variance_swap_payoff.png)

Here we can see the PnL is zero when realzied volitity is equal to the strike. 