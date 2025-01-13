## AI Trading bot
### Purpose
- In this project I wanted to create an AI trading bot that is ssensitive to real time events and news and allo us to interpret news events for us to make buy or sell orders in our tarades

I broke down this project into stages:
#### Data collection and Analysis
- Here I used langchain to load data from our web pages such as Forex Factory in order to collect data that may affect our currency pairs.This may not be ideal because the more reliable sources ar Bloomberg and Forbes.However,both of these services are paid subscription which in order to access their API you need to pay
- We collected our training data from the following websites:
1. [Investing.com](https://www.investing.com/)
   
![Investing.com_Screenshot](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/3039c4cdf00f3ac25676b78c8eadb312718fce9d/Building%20a%20trading%20AI%20bot/Forex%20Screenshot.jpg)

### Select the articles highlighted in yellow in the websites and copy paste them to the LLM Model
   
2. [Forex Factory](https://www.forexfactory.com/)

![Forex Factory](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/a3d23bc30a2e75e4f5264b42f5a50422ef728bc5/Building%20a%20trading%20AI%20bot/Forex%20Factory%20Screenshot.jpg)

### Select the articles highlighted in yellow in the websites and copy paste them to the LLM Model

#### LLM MODEL
- I created a logic part of the bot such that it executes our buy or sell orders depending on the users risk appetite. We used Langchain agent to perfrom the following:

##### 1. Automated Trading Signals
- LangChain can integrate with real-time market data feeds, parse complex data patterns, and generate actionable insights such as buy/sell signals.
By chaining multiple steps (like pre-processing data, generating trading signals, and sending them to a broker API), it forms a pipeline that reacts to changes in the market.

##### 2.Strategy Generation
- Traders can input specific conditions, and LangChain can help design or propose trading strategies by interpreting those conditions and backtesting them using historical data.
Example: A user might describe a strategy like “buy when RSI is below 30 and sell when RSI is above 70,” and LangChain could convert this into executable code.

![Strategy_Execution](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/df271df50aaf8401b101ede08858a3b4920704e5/Building%20a%20trading%20AI%20bot/Strategy_Execution.jpg)

##### 3. Risk Management
- LangChain models can be used to set and adjust stop-loss, take-profit levels, and position sizing dynamically, based on real-time data and risk analysis.
It can also monitor portfolio exposure and recommend rebalancing actions to minimize risk.

##### 4 . Natural Language Queries
- Users can ask questions like, "What is the impact of inflation on tech stocks?" or "Which sectors are showing bullish momentum?" and the LangChain model can provide relevant insights by analyzing historical data, news, or predefined metrics.
![System_prompt](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/b1a4dc13c445eea8c9490cd40fea7ab43407ba45/Building%20a%20trading%20AI%20bot/System%20prompt.jpg)

[langchain_code](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/1d2422d4df0cdca282d4c39e7077b3f29a11307a/Building%20a%20trading%20AI%20bot/langchain%20beta%20-%20Copy%20for%20github.ipynb)

#### Trade execution
- We used the [mt5plaform](https://www.mql5.com/en/docs/python_metatrader5) inorder to get the python code to execute trades automatically from the metatrader5 trading platform.



