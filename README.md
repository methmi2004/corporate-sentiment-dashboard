# 📊 AI-Driven Corporate Finance & Data Analytics Intelligence Dashboard

An interactive, multi-dimensional web application built using **Python**, **Streamlit**, and **Natural Language Processing (NLP)**. This platform bridges quantitative equity evaluation frameworks with qualitative market sentiment indicators, providing investment professionals and corporate data teams with an automated asset intelligence workflow.

🔗 **Live Deployment Link:** [View Live Application](https://corporate-sentiment-dashboard-kh5pcruh3eyghyvqu3ezxc.streamlit.app/)

---

## 🚀 Technical Features

* **Real-Time Data Pipeline:** Ingests streaming market parameters from global equity databases via the `yfinance` API wrapper to extract balance sheet, income statement, and valuation variables.
* **NLP Sentiment Parsing Engine:** Processes streaming corporate headlines using the `NLTK (VADER)` lexicon model, calculating mathematical polarity vectors to classify market consensus.
* **Interactive Candlestick Analytics:** Renders 30-day technical asset price trends via high-fidelity, responsive `Plotly` graphical objects containing Open-High-Low-Close (OHLC) multi-dimensional arrays.
* **Defensive Error Handling:** Built with robust try-except architectural layers and nested dictionary lookups to handle structural data shifts in upstream market APIs safely.

---

## 🏛️ Corporate Finance Frameworks & Core Metrics Explained

The dashboard computes and visualizes five critical pillars of fundamental corporate health, functioning as a real-time equity research tool:

### 1. Market Capitalization (Equity Value)
* **Mathematical Definition:** $\text{Total Shares Outstanding} \times \text{Current Market Price per Share}$
* **Financial Significance:** Represents the total market value of a company's outstanding equity capital. In corporate development, this acts as the baseline for calculating a firm's **Enterprise Value (EV)** when adjusting for debt and cash net positioning. It classifies the asset class scale (Large-cap vs. Mid-cap vs. Small-cap), driving corporate risk parameters.

### 2. Forward Price-to-Earnings (Forward P/E) Multiples
* **Mathematical Definition:** $\frac{\text{Current Market Price per Share}}{\text{Projected Earnings Per Share (EPS) over next 12 Months}}$
* **Financial Significance:** A forward-looking relative valuation multiple indicating how many dollars investors are willing to pay today for every $\$1.00$ of projected future corporate earnings. 
  * A **high Forward P/E** implies aggressive market expectations of exponential top-line growth (common in technology sectors).
  * A **low Forward P/E** signals potential undervaluation, mature stable cash flows, or a contraction in market confidence.

### 3. Return on Equity (ROE)
* **Mathematical Definition:** $\frac{\text{Net Income}}{\text{Shareholders' Equity}}$
* **Financial Significance:** The ultimate metric for measuring management's operational efficiency. ROE gauges how many dollars of net profit a firm generates with every dollar of capital provided by its shareholders. It acts as the core anchor point for **DuPont Analysis**, breaking down corporate profitability, asset turnover efficiency, and financial leverage ratios.

### 4. Debt-to-Equity (D/E) Ratio
* **Mathematical Definition:** $\frac{\text{Total Liabilities}}{\text{Total Shareholders' Equity}}$
* **Financial Significance:** A leverage metric evaluating a company's capital structure and structural solvency risk. It illustrates how much of the company's asset base is funded via credit and obligations versus equity capital injections. High D/E ratios indicate high financial leverage, increasing the firm's vulnerability to macroeconomic interest rate shocks.

### 5. Net Profit Margin
* **Mathematical Definition:** $\frac{\text{Net Income}}{\text{Total Revenue}} \times 100$
* **Financial Significance:** A margin efficiency ratio showing the percentage of revenue that converts into clean net income after deducting all operating costs, interest payments, overheads, and corporate tax provisions. Higher, expanding profit margins demonstrate robust corporate pricing power and strong structural cost-control mechanisms.

---

## 🤖 Data Analysis & Engineering Workflow

This application implements a complete, end-to-end Data Analysis Lifecycle, making it an enterprise-grade case study for Data Analysis internship roles:

### 1. Data Ingestion & API Pipelines
* Implemented dynamic data collection from unstructured web endpoints using the `yfinance` financial API wrapper.
* Built automated data pipelines that parse raw, multi-layered JSON payload configurations into analytical subsets inside seconds.

### 2. Defensive Data Cleaning & Validation
* Designed robust, structural data validation mechanisms using Python dictionary methods (`.get()`) to handle missing data fields, null corporate returns, and `N/A` anomalies without stopping runtime processes.
* Coded nested structural parsing to adapt seamlessly to external changes in vendor data schemas.

### 3. Feature Engineering & Normalization
* **Macro Data Processing:** Converted raw corporate valuations into human-readable scaled strings with commas (e.g., transforming `1000000000` to `$1,000,000,000` via text formatting expressions).
* **Ratio Transmutation:** Transformed raw fractional float metrics into localized percentage points (multiplying values by 100 and capping at 2 decimal points) to create uniform, standardized KPIs.

### 4. Qualitative NLP Sentiment Modeling
* Applied Natural Language Processing text preprocessing techniques to corporate headlines using the `NLTK` library.
* Converted raw qualitative strings into a normalized quantitative **Compound Score Vector** range ($[-1.0, +1.0]$) using the semi-strong form of the **Efficient Market Hypothesis (EMH)** to mathematically calculate market mood.
  * **Compound Score ($\ge 0.05$):** Signals a **Bullish** macroeconomic consensus, indicating positive pricing momentum.
  * **Compound Score ($\le -0.05$):** Signals a **Bearish** consensus, warning analysts of potential downside volatility or credit/reputational risk exposures.

### 5. Data Visualization & Executive Storytelling
* Built interactive **Plotly Candlestick** objects containing explicit Open-High-Low-Close (OHLC) multi-dimensional arrays, replacing flat historical tables with clean visual trends.
* Converted complex analytical computations into an interactive, functional web application dashboard using **Streamlit** to facilitate rapid executive business decision-making.

---

## 📦 Tech Stack Used

* **Language:** Python 3.13
* **Framework:** Streamlit
* **Data Processing & Manipulation:** Pandas
* **Financial APIs:** Yahoo Finance (`yfinance`)
* **Natural Language Processing:** NLTK (`vader_lexicon`)
* **Data Visualization:** Plotly Graph Objects

---

## 🔧 Installation & Local Setup

### 1. Clone the repository:
```bash
git clone https://github.com
cd corporate-sentiment-dashboard
```

### 2. Install the production dependencies:
```bash
pip install -r requirements.txt
```

### 3. Boot up the Streamlit host engine:
```bash
streamlit run App.py
```

---

## 📈 Future Enhancements Planned

* Implement historical sentiment time-series overlays to plot the exact statistical correlation between news sentiment scores and historical price fluctuations.
* Upgrade predictive capacity by implementing an LSTM (Long Short-Term Memory) recurrent neural network module to forecast future cash flows.

