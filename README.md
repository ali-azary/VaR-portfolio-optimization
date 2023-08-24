# VaR-portfolio-optimization
Value at Risk Portfolio Optimization
<h3>Value at Risk Portfolio Optimization</h3>
Value at Risk (VaR) is a statistical measure used to estimate the potential loss of an investment 
portfolio over a given time horizon at a certain confidence level. Portfolio optimization using VaR 
involves finding the optimal portfolio that minimizes the VaR subject to certain constraints[1][6]. 
The mathematical formula for VaR is:

$$ VaR_{\alpha}(P) = -\inf\{l \in \mathbb{R} : P(L \leq l) \geq 1 - \alpha\} $$

where \(P\) is the probability distribution of portfolio losses, \(L\) is the loss of the portfolio, 
\(\alpha\) is the confidence level, and \(VaR_{\alpha}(P)\) is the VaR at the \(\alpha\) level of 
confidence.
<br>
The optimization problem can be formulated as:

$$ \min_{w} VaR_{\alpha}(P(w)) $$

$$ \text{s.t.} \quad \sum_{i=1}^{n} w_{i} = 1 $$

where \(w_{i}\) is the weight of the \(i\)th asset in the portfolio, and \(n\) is the number of assets 
in the portfolio.
<br>
There are different methods to estimate VaR, including historical simulation, variance-covariance method, 
and Monte Carlo simulation. Once VaR is estimated, it can be used to optimize the portfolio by minimizing 
the VaR subject to constraints on expected return, volatility, and other factors.
<br>
We can also use the modified Sharpe ratio that adjusts for Value-at-Risk (VaR) to optimize a portfolio. 
The modified Sharpe ratio is proposed in a paper titled "Robust Portfolio Optimization with Value-At-Risk 
Adjusted Sharpe Ratio". The formula for the modified Sharpe ratio is:

$$ Sharpe = \frac{\mu_R(\omega)-\mu_F}{\operatorname{VaR}(\alpha ; \omega)} $$

where \(\mu_R(\omega)\) is the expected return of the portfolio, \(\mu_F\) is the risk-free rate, 
\(\operatorname{VaR}(\alpha ; \omega)\) is the VaR of the portfolio at the \(\alpha\) level of confidence, 
and \(\omega\) is the weight of each asset in the portfolio.
<br>
The modified Sharpe ratio can be used to evaluate the risk-adjusted performance of a portfolio and to 
optimize the portfolio by maximizing the ratio subject to constraints on expected return, volatility, 
and other factors.
<h3>Python Implementation</h3>
Now, let's try a simple example in Python. We use 2021 data to calculate the optimum weights and we let 
a factor of 10 leverage for both short and long positions.

![img01](https://github.com/ali-azary/VaR-portfolio-optimization/assets/69943289/98c58480-3088-42cd-b92e-c420d3c6df57)

we get the following portfolio weights and the modified sharpe ratio:<br>
Optimized weights: [-1.66094218 -2.56430555  1.65598121  3.56926652]<br>
Sharpe ratio: 0.028890340594040078<br>
The portfolio performance for 2022 up to date:

![img02](https://github.com/ali-azary/VaR-portfolio-optimization/assets/69943289/a46a98cd-4ec4-4d69-82ca-06d4774ee2b0)

![img03](https://github.com/ali-azary/VaR-portfolio-optimization/assets/69943289/95ed3327-5439-4ff4-ae14-f504295ab9c3)

As it is seen we get a great performance above the assets higher variance but low value at risk.
