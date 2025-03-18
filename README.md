# Bitcoin Risk Management Using Binance API

## Overview

This project provides a foundation for analyzing Bitcoin price data and simulating potential future price movements using a Monte Carlo simulation. The goal is to assess the risk of significant price drops and provide insights for managing Bitcoin-related financial risks.

## Features

- **Data Collection**: Fetch historical Bitcoin price data from the Binance API.
- **Data Processing**: Clean and preprocess the raw data, adding features such as moving averages and volatility.
- **Monte Carlo Simulation**: Simulate future Bitcoin price movements based on historical drift and volatility.
- **Risk Assessment**: Calculate the probability of a significant price drop (e.g., >20%) over a given time horizon.


## How It Works

1. **Data Collection**:
   - Historical Bitcoin price data is fetched from the Binance API using `fetch_data.py`.
   - The data includes fields such as `timestamp`, `open`, `high`, `low`, `close`, and `volume`.

2. **Data Processing**:
   - The raw data is cleaned and processed using `process_data.py`.
   - Features such as 7-day and 30-day moving averages (`moving_avg_7`, `moving_avg_30`) and volatility (`volatility_7`, `volatility_30`) are added.

3. **Monte Carlo Simulation**:
   - The `stochastic_model.py` script simulates future Bitcoin price movements using a Geometric Brownian Motion (GBM) model.
   - Parameters such as drift (`mu`) and volatility (`sigma`) are calculated from historical data.
   - The simulation generates multiple price paths and calculates the probability of a significant price drop.

4. **Risk Assessment**:
   - The simulation results are analyzed to estimate the likelihood of a >20% price drop over a 30-day horizon.


## Example Output

Example Output
Monte Carlo Simulation:
Simulated price paths for the next 30 days.
Probability of a >20% price drop.


## Dependencies

Python 3.8+
pandas
numpy
matplotlib
seaborn
requests
python-dotenv

## Future Work

-Build a Streamlit app to make the simulation interactive.
-Extend the simulation to include additional risk metrics (e.g., Value at Risk, Expected Shortfall).
-Integrate real-time data for live risk assessment.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Binance API for providing the data.
Inspiration from financial modeling techniques like Geometric Brownian Motion.