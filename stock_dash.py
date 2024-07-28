import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="Cyberpunk Stock Dashboard", layout="wide")
st.sidebar.title("🦾 Cyberpunk Stock Dashboard")
st.sidebar.write("Navigate the futuristic stock market in style.")


# Cyberpunk-themed CSS
cyberpunk_css = """
<style>
body {
    background-color: #0f0f0f;
    color: #00ff00;
    font-family: 'Courier New', Courier, monospace;
}
header {
    background: #000000;
}
.sidebar .sidebar-content {
    background: #1a1a1a;
}
.sidebar .sidebar-content, .sidebar .sidebar-content a {
    color: #00ff00;
}
h1, h2, h3, h4, h5, h6 {
    color: #00ff00;
}
footer {
    background: #000000;
    color: #00ff00;
}
</style>
"""

st.markdown(cyberpunk_css, unsafe_allow_html=True)

# App Title
st.title("🦾 Cyberpunk Stock Dashboard")

# Sidebar - User Input
st.sidebar.header("Stock Selection")
stock_symbol = st.sidebar.text_input("Enter Stock Symbol", value="AAPL")
start_date = st.sidebar.date_input("Start Date", value=datetime.now() - timedelta(days=30))
end_date = st.sidebar.date_input("End Date", value=datetime.now())

# Fetch Stock Data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Plotting the Stock Data
fig = go.Figure()
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close Price'))
fig.update_layout(
    title=f"Stock Prices for {stock_symbol.upper()}",
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    template='plotly_dark',
    paper_bgcolor='#0f0f0f',
    plot_bgcolor='#0f0f0f',
    font=dict(color='#00ff00')
)

st.plotly_chart(fig)

# Footer
st.markdown(
    """
    <footer>
        <div style="text-align: center; padding: 10px;">
            © 2024 Cyberpunk Inc. All rights reserved.
        </div>
    </footer>
    """,
    unsafe_allow_html=True
)