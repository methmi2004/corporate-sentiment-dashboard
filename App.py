import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon for sentiment analysis
nltk.download('vader_lexicon', quiet=True)

def fetch_financial_data(ticker):
    """Fetches core corporate finance metrics dynamically using yfinance."""
    stock = yf.Ticker(ticker)
    info = stock.info if stock.info else {}
    
    metrics = {
        "Company Name": info.get("longName", ticker),
        "Market Cap": info.get("marketCap", 0),
        "Forward P/E": info.get("forwardPE", "N/A"),
        "Return on Equity (ROE)": info.get("returnOnEquity", "N/A"),
        "Debt to Equity": info.get("debtToEquity", "N/A"),
        "Profit Margin": info.get("profitMargins", "N/A"),
    }
    
    # Updated structure to safely parse Yahoo Finance's new nested news layout
    news = stock.news
    headlines = []
    if news:
        for item in news[:5]:
            if 'content' in item and 'title' in item['content']:
                headlines.append(item['content']['title'])
            elif 'title' in item:
                headlines.append(item['title'])
    
    # Extract historical market prices for visualization
    hist = stock.history(period="1mo")
    
    return metrics, headlines, hist

def analyze_sentiment(headlines):
    """Calculates directional compound sentiment scores utilizing NLTK VADER."""
    sia = SentimentIntensityAnalyzer()
    if not headlines:
        return 0, "No Active News Data"
        
    scores = [sia.polarity_scores(txt)['compound'] for txt in headlines]
    avg_score = sum(scores) / len(scores)
    
    if avg_score >= 0.05:
        return avg_score, "Bullish (Positive) 🚀"
    elif avg_score <= -0.05:
        return avg_score, "Bearish (Negative) 📉"
    else:
        return avg_score, "Neutral ⚖️"

# --- Streamlit Corporate Dashboard UI Construction ---
st.set_page_config(page_title="Corporate Intelligence Dashboard", layout="wide")
st.title("📊 AI-Driven Corporate Finance & Sentiment Dashboard")

ticker_input = st.text_input("Enter Corporate Ticker Symbol (e.g., AAPL, MSFT, TSLA):", "AAPL").upper()

if st.button("Run Financial Analysis"):
    with st.spinner("Executing live market API pipelines and NLP processing..."):
        try:
            metrics, headlines, hist = fetch_financial_data(ticker_input)
            avg_score, sentiment_label = analyze_sentiment(headlines)
            
            # Divide interface layout into structural tracking columns
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader(f"🏢 {metrics['Company Name']} Key Financials")
                
                # Format large corporate valuations cleanly with comma separators
                market_cap = metrics.get('Market Cap', 0)
                market_cap_display = f"${market_cap:,}" if market_cap else "N/A"
                st.write(f"**Market Cap:** {market_cap_display}")
                
                st.write(f"**Forward P/E Ratio:** {metrics.get('Forward P/E', 'N/A')}")
                
                # Explicit check preventing nested string manipulation breaks
                roe_val = metrics.get('Return on Equity (ROE)', 'N/A')
                roe_display = f"{roe_val * 100:.2f}%" if isinstance(roe_val, (int, float)) else "N/A"
                st.write(f"**Return on Equity (ROE):** {roe_display}")
                
                st.write(f"**Debt to Equity Ratio:** {metrics.get('Debt to Equity', 'N/A')}")
                
                margin_val = metrics.get('Profit Margin', 'N/A')
                margin_display = f"{margin_val * 100:.2f}%" if isinstance(margin_val, (int, float)) else "N/A"
                st.write(f"**Net Profit Margin:** {margin_display}")
                
                st.subheader("🤖 NLP Media Sentiment Engine")
                st.metric(label="Overall Corporate Sentiment", value=sentiment_label, delta=f"Score: {avg_score:.2f}")
                
            with col2:
                st.subheader("📈 30-Day Stock Price Trend")
                if not hist.empty:
                    fig = go.Figure(data=[go.Candlestick(
                        x=hist.index, 
                        open=hist['Open'], 
                        high=hist['High'], 
                        low=hist['Low'], 
                        close=hist['Close']
                    )])
                    fig.update_layout(xaxis_rangeslider_visible=False, height=350, margin=dict(l=20, r=20, t=20, b=20))
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Historical pricing data unavailable for this ticker asset class.")
                
            st.subheader("📰 Recent Corporate Headlines Analyzed")
            if headlines:
                for h in headlines:
                    st.markdown(f"- {h}")
            else:
                st.info("No recent news found for this corporate entity.")
                
        except Exception as e:
            st.error(f"Error compiling analytical layers for ticker '{ticker_input}': {str(e)}")
