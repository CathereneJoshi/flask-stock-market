# Stock Market Analysis

As the stock market is extremely variable and indeterministic, predicting the uptrend and downtrend may be a complicated process. The stock market features a limitless number of aspects that regulate these directions and trends. 

The system demonstrates the utilization of Machine Learning and other algorithms in finance to analyze the past performance of the Index and thus predict the longer-term possibility. 

The web interface features a News Section Panel. Using BeautifulSoup, a Web Scraping tool, news articles is extracted from reliable websites such as India Infoline, EquityBulls, etc.  The trending news related to the stock market could aid the investor to develop trading strategies.

Stock markets tend to react very quickly to a lot of factors such as the news, earnings reports, etc. With the help of TextBlob a Python Library and twitter API, Sentiment Analysis is implemented to derive the opinion or attitude of news i.e the investor could determine whether a piece of writing is positive, negative, or neutral.

To analyze the price action of a the stocks an interactive candlestick chart pattern for one year time frame is displayed with the help of Bokeh library which provides high-performance interactive charts and plots.

To run the application:

1. Clone the repository
   ```git clone https://github.com/CathereneJoshi/flask-stock-market.git```

2. Download all the necessary libraries for this project
   ```pip3 install -r requirements.txt```
   
3. Run the flask project
