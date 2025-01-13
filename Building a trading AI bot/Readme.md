## AI Trading bot
### Purpose
- In this project I wanted to create an AI trading bot that is ssensitive to real time events and news and allo us to interpret news events for us to make buy or sell orders in our tarades

I broke down this project into stages:
#### Data collection and Analysis
- Here I used langchain to load data from our web pages such as Forex Factory in order to collect data that may affect our currency pairs.This may not be ideal because the more reliable sources ar Bloomberg and Forbes.However,both of these services are paid subscription which in order to access their API you need to pay
- We collected our training data from the following websites:
1. [Investing.com](https://www.investing.com/)
2. [Forex Factory](https://www.forexfactory.com/)

#### LLM MODEL
- I created a logic part of the bot such that it executes our buy or sell orders depending on the users risk appetite. We a Langchain agent to perfrom the following:

##### 1. Automated Trading Signals
- LangChain can integrate with real-time market data feeds, parse complex data patterns, and generate actionable insights such as buy/sell signals.
By chaining multiple steps (like pre-processing data, generating trading signals, and sending them to a broker API), it forms a pipeline that reacts to changes in the market.

##### 2.Strategy Generation
- Traders can input specific conditions, and LangChain can help design or propose trading strategies by interpreting those conditions and backtesting them using historical data.
Example: A user might describe a strategy like “buy when RSI is below 30 and sell when RSI is above 70,” and LangChain could convert this into executable code.

##### 3. Risk Management
- LangChain models can be used to set and adjust stop-loss, take-profit levels, and position sizing dynamically, based on real-time data and risk analysis.
It can also monitor portfolio exposure and recommend rebalancing actions to minimize risk.

##### 4 . Natural Language Queries
- Users can ask questions like, "What is the impact of inflation on tech stocks?" or "Which sectors are showing bullish momentum?" and the LangChain model can provide relevant insights by analyzing historical data, news, or predefined metrics.

#### Trade execution
- Our bot will be able to automatically inteprete news from our desired data source and execute buy or sell orders.
- We used the [mt5plaform](https://www.mql5.com/en/docs/python_metatrader5)



