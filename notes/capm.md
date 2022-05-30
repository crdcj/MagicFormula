# Capital Asset Pricing Model

## When making a strategy analysis, we must pay attention to the risk that a asset or portfolio is exposed. One approach is to consider the Capital Asset Pricing Model, as presented by the article "In-Depth Analysis of GreenBlatt's Magic Formula: Risk or True Value":

$$R_{i,t} - R_{f,t} = \alpha_{i} + \beta_{i} * (R_{m,t} - R_{f,t}) + \epsilon_{i,t}$$

where,
- $R_{i,t}$: return of firm $i$ at time $t$;
- $R_{f,t}$: risk-free rate at time $t$;
- $\alpha_{i}$: part of the return on stock $i$ that is not explained by covariation with the market;
- $\beta_{i}$: exposure of a stock's return to the market return;
- $R_{m,t}$: return of the benchmark market index at time t;
- $\epsilon_{i,t}$: error term for the given stock at the given time (unsystematic).

&emsp;A question that arises when doing the above calculation is what is the discretization of time we will use. Considering for a moment that the above equation could be valuable to a high frequency trader, a time frame of milliseconds would be used and an $\alpha$ for an asset or for a high frequency portfolio would be generated. The problem in this extreme scenario is that a lot of returns would be zero, considering that most assets in the brazilian market have low to medium frequency trades. Since, when using the Magic Formula, we are interested in scanning the maximum number of assets, respecting some minimum traded volume threshold, we discard high frequency time frames, as also intraday returns. 

&emsp;Our dataset will be comprised of daily returns. 
