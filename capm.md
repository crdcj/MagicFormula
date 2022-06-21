# Magic Formula

## What is the Magic Formula and why use it?

The Magic Formula is a portfolio management system that uses a combination of quality metrics and value proxies to identify the best possible portfolio for a given set of assets. Quality translates in the capacity that an enterprise have to maintain a consistent growth. This is a strategy that, at first, makes sense, since both quality and value are associated with long term price growth. (Nessa parte fiquei com duvida do que eh quality investing)

The canonical formula presented by GreenBlatt is composed of two parts:

## The dataset

In order to apply the Magic Formula to the Brazilian stocks market, we will need two types of data to do our backtest: accounting data and market prices.

The accounting data is provided by the financial statements, a document produced by each company that presents a instant picture on how its assets and liabilities are distributed. The financial statement can be published in two forms: yearly our quarterly. Once a year, within the first three months after the end of the business year, each company holds the Shareholder's General Meeting - SGM, with the goal to present and approve an agenda with topics fixed through a legal requirement, with one of the points of this agenda being the approval of the financial statement of the last business year. At the same time, each company can publish quarterly financial statements that reflect only the accountancy of the last three months. This quarterly document can be a regulatory requirement our just a good governance practice.

Since the quarterly financial statements can't be directly compared without some kind of adjustment, we're gonna use only the yearly docs. One benefit of this choice is that this doc is more robust and trustworthy, given that it passes through the approval of the SGM and is audited by an independent firm.

A peculiarity of the Brazilian market, that we don't know if replicates elsewhere, is the fact that some companies act in a dual role, as a individual firm and as a holding. With that, two financial statements are created, one at the individual level, considering only the business generated directly by the company, and other consolidated, reflecting the participations in other business. This leads to a choice of what type of doc will be used in the backtest. A natural choice is the consolidated, since we expect that the market price reflects the overall holdings of a particular company. But this choice has a catch. The rule for consolidation is as follows: a participation up to 50% is not consolidated, while a participation above 50% is consolidated. The objective of the rule is to inform how much business the company controls, not how much business it generates. Despite that, considering that is not a 100% picture of the actual financial situation of the company, we will use the consolidated financial statement, due to its link with the market price, as pointed above.

Still remaining in the individual/consolidated topic, we use the outstanding number of shares in the individual level. It doesn't make sense to consolidate the shares of different companies. While a financial account is a monetary value that, given is measured in a common currency, can be summed or subtracted of other accounts of the same nature, a share can only do mathematical operations with other identical shares.

The time interval that we defined for the backtest is from 2010 to 2022, comprising 12 years. A technicality that must be clear is that, for example, the financial statements from 2010 are available only in the early months of 2011. This is a important fact to pay attention, to avoid using information that is not available at the time of the decision. Is easy to be mistaken and think that a financial statement of a particular year was published in that same year. Usually, the Brazilian business year goes from January to December, with the financial statement necessarily being released until march 31st. 

### Different Measures of Risk

### Systematic and Unsystematic Risk

&emsp;When making a strategy analysis, we must pay attention to the risk that a asset or portfolio is exposed. One approach is to consider the Capital Asset Pricing Model, as presented by the article "In-Depth Analysis of GreenBlatt's Magic Formula: Risk or True Value":

$R_{i,t} - R_{f,t} = \alpha_{i} + \beta_{i} * (R_{m,t} - R_{f,t}) + \epsilon_{i,t}$

where,

- $R_{i,t}$: return of firm $i$ at time $t$;
- $R_{f,t}$: risk-free rate at time $t$;
- $\alpha_{i}$: part of the return on stock $i$ that is not explained by covariation with the market;
- $\beta_{i}$: exposure of a stock's return to the market return;
- $R_{m,t}$: return of the benchmark market index at time t;
- $\epsilon_{i,t}$: error term for the given stock at the given time (unsystematic).

&#8195;A question that arises when doing the above calculation is what is the discretization of time we will use. Considering for a moment that the above equation could be valuable to a high frequency trader, a time frame of milliseconds would be used and an $\alpha$ for an asset or for a high frequency portfolio would be generated. The problem in this extreme scenario is that a lot of returns would be zero, considering that most assets in the brazilian market have low to medium frequency trades. Since, when using the Magic Formula, we are interested in scanning the maximum number of assets, respecting some minimum traded volume threshold, we discard high frequency time frames, as also intraday returns.

&#8195;Our dataset will be comprised of daily returns.
