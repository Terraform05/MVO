
# Mean Variance Optimization (MVO)

This repository demonstrates the application of **Mean Variance Optimization (MVO)** for portfolio selection using both **Python** and **Excel**. The project applies Modern Portfolio Theory, maximizing returns while minimizing risk, and plots the Efficient Frontier, Sharpe ratio, and other key financial metrics.

## Key Concepts
- **Mean Variance Optimization (MVO)**: A method to optimize portfolio allocation to maximize expected return for a given level of risk or minimize risk for a given return.
- **Efficient Frontier**: A graphical representation of the optimal portfolios that offer the highest expected return for a defined level of risk.
- **Sharpe Ratio**: A measure of the risk-adjusted return of a portfolio.

## Structure
- **Python Implementation** (`MVO.ipynb` & `mvo_file.py`):
  - Importing historical stock data using `yfinance`
  - Calculating historical percent change, average return, variance, and covariance
  - Generating random portfolios and plotting the Efficient Frontier
  - Identifying optimal, minimum risk, and maximum return portfolios

- **Excel Implementation**:
  - Detailed step-by-step process of obtaining historical data and performing MVO calculations
  - Covariance, correlation matrix, and portfolio generation

## Notebooks and Scripts
- **MVO.ipynb**: Jupyter notebook with Python implementation of MVO.
- **mvo_file.py**: Python script for MVO calculations.
- **spy.py**: Python script related to S&P500 data analysis.

## Data
- `data/df_close.csv`: Historical stock prices.
- `data/df_recent_close.csv`: Recent close price data.
- `data/df_spy_close.csv`: S&P500 stock price data.

## Python Libraries Used
- `pandas`
- `numpy`
- `matplotlib`
- `yfinance`
- `plotly`

## Visuals
- **Matplotlib Plots**: Close price, correlation matrix, percent change, and cumulative product.
- **Plotly Plots**: Interactive visualizations for better exploration of data.

## Reference
Based on [MVO_AlexRamirez.pdf](./MVO_AlexRamirez.pdf), this project implements the concepts described therein, including portfolio optimization using Python and Excel for more effective financial decision-making.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/MVO.git
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebook or Python scripts to experiment with MVO for various stocks.

## Author
Alex Joaquin Ramirez
