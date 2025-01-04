# Distributed Financial Risk Assessment

**Authors:**
- Anirudh Garg [ag9563@nyu.edu]
- Nikhil Kommineni [nk3853@nyu.edu]
- Sai Preetham [sb9509@nyu.edu]
- Sujana Maithili [sc10648@nyu.edu]

## Abstract

This project aims to implement a distributed framework for financial risk assessment using Monte Carlo simulations to estimate Value at Risk (VaR) and Conditional Value at Risk (CVaR). By leveraging Spark's distributed computing capabilities, we efficiently parallelize processing of large-scale market data, simulating millions of scenarios to generate robust risk metrics. The framework also incorporates techniques to optimize computational performance and ensures scalability for real-world financial datasets, enabling timely and reliable risk evaluation for decision-making. All computations are run on the NYU dataproc cluster hosted on GCP.

## Introduction

Financial markets are characterized by their complexity and volatility, making accurate risk assessment critical. Traditional risk models often lack scalability and fail to adapt in real time to dynamic market conditions. To address these limitations, this work proposes a distributed framework that leverages Spark’s parallel processing capabilities to analyze large-scale financial data efficiently. By improving the precision of risk metrics like VaR and CVaR, our system provides actionable insights for portfolio management and strategic decision-making, empowering stakeholders to navigate uncertainties with confidence.

Monte Carlo simulation forms the backbone of our approach, estimating risk by simulating millions of random market scenarios. This method captures the probabilistic behavior of portfolios under diverse conditions, addressing the limitations of traditional variance-covariance and historical simulation methods.

Financial analysts can use the system to assess portfolio risk and generate actionable insights for crafting investment strategies. Portfolio managers can leverage the calculated VaR and CVaR metrics to optimize asset allocation and ensure risk-adjusted returns. Additionally, risk management teams can utilize the framework to estimate necessary capital reserves and design effective risk mitigation strategies, thereby enhancing overall financial stability and resilience.

### Value at Risk (VaR)

Value at Risk (VaR) is a measure of investment risk that provides a reasonable estimate of the maximum probable loss in value of an investment portfolio over a particular period of time. A VaR of $1 million with a 5% probability over two weeks reasonably justifies that the portfolio stands only a 5% chance of losing more than $1 million in two weeks.

### Conditional VaR (CVaR)

Conditional Value at Risk (CVaR), sometimes known as expected shortfall, is a related investment risk metric that was recently proposed as a better alternative to VaR. CVaR uses the expected loss instead of a cutoff value to indicate the risk in a portfolio. A CVaR of $1 million with a 5% q-value over two weeks indicates that the average loss in the worst 5% of outcomes is $1 million.

## Background

### Terminology

We make use of the following specific terms related to the financial domain in this report:
- **Index**: An imaginary portfolio, often built to model market trends. For example, the NASDAQ Composite Index includes about 3,000 stocks and similar instruments listed in the New York Stock Exchange.
- **Market factor**: A value that can be used as an indicator of macro aspects of the financial climate at a particular time. Common examples include the value of an index, the GDP of the US, or the exchange rate between the dollar and the euro.

### Methods for Calculating VaR

Estimating VaR requires us to propose a model for how the portfolio functions and choosing the probability distribution its returns are likely to take. Institutions employ a variety of approaches for calculating VaR, all of which tend to fall under a few general methods:

- **Variance-Covariance**: Assumes instrument returns are normally distributed, allowing closed-form solutions to estimate losses.
- **Historical Simulation**: Uses historical data to estimate risk, extrapolating risk from historical performance.
- **Monte Carlo Simulations**: Simulates the portfolio performance under random conditions and estimates risk by sampling random variables.

## Proposed Method

### Data Collection and Cleaning

The historical financial data is collected using Python’s `yfinance` library, including columns like Date, Price, Adjusted Close, Close, High, Low, Open, and Volume. Missing values are handled using techniques like forward and backward filling.

### Determining Factor Weights

VaR is concerned with losses over a specific time horizon, not the absolute prices of instruments, but rather how those prices change. We calculate the 2-week returns of stocks and factors and use linear regression to model the stock return data based on factor return data.

### Sampling

To simulate market conditions, we generate random factor returns by selecting a probability distribution over factor return vectors and sampling from it. The multivariate normal distribution is used to account for correlations between factors.

### Running Trials

We parallelize the trials using Spark. Each trial involves sampling a set of risk factors, predicting the returns for each instrument, and summing them to calculate the trial loss.

### Portfolio Return Calculation

The total portfolio return for a trial is calculated by averaging the returns of all instruments assuming equal portfolio weights.

### Value at Risk (VaR) and Conditional Value at Risk (CVaR)

- **VaR**: The return that is expected to be underperformed 5% of the time.
- **CVaR**: The average return from the worst 5% of trials.

## Results

We evaluated the framework on datasets from major stock exchanges such as NYSE, NSE, HKSE, and LSE. The market factors include S&P 500, NASDAQ Composite, YYX (Treasury Yield 30 years), and FVX (Treasury Yield 5 years).

### Stock Exchange Data Overview

| Exchange | Size   | Symbols | Time Period   |
|----------|--------|---------|---------------|
| NYSE     | 1.1 GB | 2800    | 2000 to 2024  |
| NSE      | 870 MB | 2021    | 2000 to 2024  |
| HKSE     | 693 MB | 1800    | 2000 to 2024  |
| LSE      | 601 MB | 1720    | 2000 to 2024  |

### Market Factor Data Overview

| Index    | Size   | Time Period |
|----------|--------|-------------|
| S&P 500  | 660KB  | 2000 to 2024 |
| NASDAQ   | 640KB  | 2000 to 2024 |
| YYX      | 636KB  | 2000 to 2024 |
| FVX      | 644KB  | 2000 to 2024 |

### VaR and CVaR for Stock Exchanges

| Exchange | VaR   | CVaR  |
|----------|-------|-------|
| NYSE     | 2.73% | 4.35% |
| NSE      | -4.2% | 1.83% |
| HKSE     | 2.11% | 2.14% |
| LSE      | -3.73%| 1.66% |

### VaR of Famous Investors' Portfolios

| Investor            | VaR   |
|---------------------|-------|
| Warren Buffett      | 4.92  |
| Bill & Melinda Gates| 5.40  |
| George Soros        | 0.84% |

## Conclusion

Our framework enables accurate financial risk assessment using Monte Carlo simulations in a distributed environment. By leveraging Spark’s computing capabilities, the system can handle large-scale financial datasets efficiently, providing actionable insights for portfolio management, investment strategies, and risk mitigation.

