import yfinance as yf
import numpy as np
import scipy.optimize as sco
from scipy.stats import norm
import matplotlib.pyplot as plt

# Define assets and download data
assets = ['AAPL', 'MSFT', 'AMZN', 'GOOG']
data = yf.download(assets, period='1y')['Close']

# Calculate returns
returns = np.log(data / data.shift())
returns.dropna(inplace=True)

# Define risk-free rate and VaR confidence level
rf = yf.Ticker('^TNX').info['previousClose'] / 100.
alpha = 0.95

# Define objective function for Sharpe ratio with VaR adjustment
def neg_sharpe_ratio(weights, returns, rf, alpha):
    port_return = np.sum(returns.mean() * weights) * 252
    port_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    port_var = -port_return + port_volatility * np.sqrt(252) * norm.ppf(alpha)
    sharpe_ratio = (port_return - rf) / port_var
    return -sharpe_ratio

# Define optimization constraints
def constraint1(weights):
    return np.sum(weights) - 1

cons = ({'type': 'eq', 'fun': constraint1})

# Define initial guess and optimization bounds
n_assets = len(assets)
init_guess = np.array([1/n_assets for _ in range(n_assets)])
bounds = tuple((-10, 10) for _ in range(n_assets))

# Optimize portfolio weights
opt_results = sco.minimize(neg_sharpe_ratio, init_guess, 
                           args=(returns, rf, alpha), 
                           method='SLSQP', 
                           bounds=bounds,
                           constraints=cons)

# Print optimized weights and Sharpe ratio
print('Optimized weights:', opt_results.x)
print('Sharpe ratio:', -opt_results.fun)

# future data
data = yf.download(assets, 
                   start='2022-01-01')['Close']

# Calculate returns
returns = np.log(data / data.shift())
returns.dropna(inplace=True)

# Calculate portfolio returns
data['portfolio'] = np.dot(data[assets], opt_results.x)
returns['portfolio'] = np.dot(returns, opt_results.x)

# Plot portfolio performance compared to individual assets
plt.figure(figsize=(10, 6))
(data / data.iloc[0]).plot()

plt.xlabel('Date')
plt.ylabel('Normalized Price')
plt.title('Portfolio Performance vs Individual Assets')
plt.show()
