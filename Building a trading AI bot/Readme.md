## AI Trading bot
### Purpose
In this project the main objective was to create an AI trading bot that is sensitive to real time events and news and allow us to interpret news events for us to make buy or sell orders in our trades.The purpose of this project is to give direction to the AI model on the best entry point for a trader in terms of selling and buying currency pairs

Here is a break down of this project into stages:
#### (i) Data collection and Analysis
We used langchain to load data from our web pages such as Forex Factory in order to collect data that may affect our currency pairs. These data includes:
  
a)  Support it refers to a price level at which a financial asset tends to stop falling and bounce back up due to increased buying interest.

b)  Resistance It refers to a price level where a financial asset tends to face selling pressure, preventing it from rising further

c)  Bid  it is the highest price a buyer is willing to pay for an asset

d)  Ask it is the lowest price a seller is willing to accept for an asset
  
1. [Investing.com](https://www.investing.com/)
   
![Investing.com_Screenshot](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/3039c4cdf00f3ac25676b78c8eadb312718fce9d/Building%20a%20trading%20AI%20bot/Forex%20Screenshot.jpg)

### Select the articles highlighted in yellow in the websites and copy paste them to the LLM Model
   
2. [Forex Factory](https://www.forexfactory.com/)

![Forex Factory](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/a3d23bc30a2e75e4f5264b42f5a50422ef728bc5/Building%20a%20trading%20AI%20bot/Forex%20Factory%20Screenshot.jpg)

### Select the articles highlighted in yellow in the websites and copy paste them to the LLM Model

#### (ii) LLM MODEL
- It is a type of machine learning model designed to understand and generate human-like text.These models are trained on vast amounts of text data, enabling them to perform a wide range of natural language processing (NLP) tasks.
- We used Langchain to interact with the LLM Model inorder to get feedback.It provides a pipeline to the LLM Model that helps us retrive feedback from the LLM Model


![Strategy_Execution](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/df271df50aaf8401b101ede08858a3b4920704e5/Building%20a%20trading%20AI%20bot/Strategy_Execution.jpg)

##### 4 . Natural Language Queries
- It refer to using everyday, human language to ask questions or retrieve information from a database, search engine, or system, without requiring complex programming or query syntax. The Langchain framework converts the data we have into a numerical represenation in a vector form through a proocess called embedding. The LLM Model performs a similarity search with the numerical representation and it is able to retrieve our answer.
  
- Users can ask questions like, "What is the impact of inflation on tech stocks?" or "Which sectors are showing bullish momentum?". These type of texts are embedded and set to the LLM model which performs a similarity search where similar texts that have the same vector representation and then retrieved back as an output.

##### Trading bot Flowchart
![Trading_bot_Flowchart](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/2aa59608b1a83a752c53eee9d9ad9ec45e82f6d0/Building%20a%20trading%20AI%20bot/Trading%20bot%20flow%20chart.jpg)

![System_prompt](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/b1a4dc13c445eea8c9490cd40fea7ab43407ba45/Building%20a%20trading%20AI%20bot/System%20prompt.jpg)

[langchain_code](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/1d2422d4df0cdca282d4c39e7077b3f29a11307a/Building%20a%20trading%20AI%20bot/langchain%20beta%20-%20Copy%20for%20github.ipynb)


#### Trade execution
- We used the [mt5plaform](https://www.mql5.com/en/docs/python_metatrader5) inorder to get the python code to execute trades automatically from the metatrader5 trading platform.

![Trade Execution](https://github.com/JORDANGAMBA99/Data-Science-Projects/blob/afe9174b71da863798cf95f224c33c9ae751fbd7/Building%20a%20trading%20AI%20bot/Trade%20executed.jpg)


##### Challenges
- Reliable sources such as Bloomberg and Forbes are paid subscription that require payment.
- The bot is hampered with the information that is provided in that very instance. Therefore it is hampered and provides advise based on the current information provided.If the data is not retrieved it can be problematic as it will not provide the most accurate assessment of the currency pair you want analyzed.
