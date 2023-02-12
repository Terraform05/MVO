import numpy as np
import pandas as pd
import yfinance as yf

#define constants
risk_free_rate = 0.03
trial_n = 3
tickers = ['NKE', 'MSFT', 'DIS', 'COST']
start = '2012-1-1'
end = '2022-3-1'

#get data
df_close = yf.download(tickers, start, end, interval='1mo')['Close']

df_close.to_csv('./data/df_close.csv')
if df_close.isnull().values.any():
    df_close.fillna(method='ffill', inplace = True) #front fills
    df_close.fillna(method='bfill', inplace = True) #back fills

#process data
df_pct_change = df_close.pct_change().iloc[1:]
mean_return = df_pct_change.mean() * 12
cov_mat = df_pct_change.cov()*12
corr_mat = df_pct_change.corr()

#eq port
weight = 1/len(tickers)
eq_weights = [weight for i in tickers]
eq_return = eq_weights @ (mean_return)
eq_risk = ((eq_weights @ cov_mat) @ eq_weights)**(1/2)
eq_sharpe = (eq_return - risk_free_rate)/eq_risk

#trial port
efficient_frontier_data = []
for trial in range(trial_n):
    t_weight = np.random.random(len(tickers, ))
    t_weights = t_weight/sum(t_weight)
    t_return = t_weights @ (mean_return)
    t_risk = ((t_weights @ cov_mat) @ t_weights)**(1/2)
    t_sharpe = (t_return - risk_free_rate)/t_risk
    efficient_frontier_data.append([t_weights, t_risk, t_return, t_sharpe])
efficient_frontier_data = pd.DataFrame(efficient_frontier_data, columns=['Weights', 'Risk', 'Return', 'Sharpe'])

# max sharpe
i = efficient_frontier_data['Sharpe'].idxmax()
max_sharpe = efficient_frontier_data.iloc[i, :]

#min risk
i = efficient_frontier_data['Risk'].idxmin()
min_risk = efficient_frontier_data.iloc[i, :]

#max return
i = efficient_frontier_data['Return'].idxmax()
max_return = efficient_frontier_data.iloc[i, :]