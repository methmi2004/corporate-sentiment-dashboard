\# 📊 AI-Driven Corporate Finance \& Sentiment Intelligence Dashboard



An interactive, multi-dimensional web application built using \*\*Python\*\*, \*\*Streamlit\*\*, and \*\*Natural Language Processing (NLP)\*\*. This tool bridges the gap between quantitative corporate financial analysis and qualitative market sentiment tracking, providing investment analysts with real-time, end-to-end stock intelligence.



\---



\## 🚀 Key Features



\* \*\*Live Financial Data Pipeline:\*\* Dynamically hooks into market data using the `yfinance` API to extract core equity research metrics such as Market Capitalization, Forward P/E Ratio, Return on Equity (ROE), Debt-to-Equity, and Net Profit Margin.

\* \*\*NLP Media Sentiment Analysis Engine:\*\* Uses the `NLTK (VADER)` sentiment analyzer to process recent corporate news headlines, calculating programmatic scoring vectors to determine if the prevailing market sentiment is \*\*Bullish\*\*, \*\*Bearish\*\*, or \*\*Neutral\*\*.

\* \*\*Advanced Market Visualization:\*\* Renders interactive 30-day structural asset price trends using high-fidelity `Plotly` Candlestick charts to assist in technical analysis.

\* \*\*Defensive Engineering Architecture:\*\* Programmed with robust exception handling and fallback dictionary parsing logic to guarantee fluid performance even amidst volatile external API structure shifts.



\---



\## 🛠️ Project Architecture Explained (Financial \& Data Science Theories)



1\. \*\*Efficient Market Hypothesis (EMH):\*\* The app operates on the principle that new public information immediately impacts asset prices. By running real-time sentiment analysis on the latest headlines, it captures immediate shifts in market psychology before they are fully priced in.

2\. \*\*Forward P/E Valuation Multiples:\*\* Evaluates market price relative to forward-looking earnings projections ($1 of future profit vs. price paid today), indicating corporate growth expectations and over/undervaluation.

3\. \*\*Data Storytelling \& Visualization:\*\* Converts complex, multi-layered financial API returns into structured layouts using `Streamlit` grids, giving corporate decision-makers (CEOs/CFOs) actionable insights inside seconds.



\---



\## 📦 Tech Stack Used



\* \*\*Language:\*\* Python 3.13

\* \*\*Framework:\*\* Streamlit

\* \*\*Data Processing \& Manipulation:\*\* Pandas

\* \*\*Financial APIs:\*\* Yahoo Finance (`yfinance`)

\* \*\*Natural Language Processing:\*\* NLTK (`vader\_lexicon`)

\* \*\*Data Visualization:\*\* Plotly Graph Objects



\---



\## 🔧 Installation \& How to Run Locally



\### 1. Clone the repository to your local machine:

```bash

git clone https://github.com

cd corporate-sentiment-dashboard

```



\### 2. Install the necessary library bundles:

```bash

pip install yfinance pandas nltk streamlit plotly

```



\### 3. Initialize and launch the local Streamlit host server:

```bash

streamlit run App.py

```



\---



\## 📈 Future Enhancements Planned



\* Implement historical sentiment time-series overlays to plot the exact statistical correlation between news sentiment scores and historical price fluctuations.

\* Upgrade predictive capacity by implementing an LSTM (Long Short-Term Memory) recurrent neural network module to forecast future cash flows.



