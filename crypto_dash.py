import streamlit as st
import requests

st.set_page_config(page_title="Cyberpunk Crypto Tracker", layout="wide")
st.sidebar.title("🦾 Cyberpunk Crypto Tracker")
st.sidebar.write("Track cryptocurrency prices in a futuristic style.")


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
st.title("🦾 Cyberpunk Crypto Tracker")

# Sidebar - User Input
st.sidebar.header("Cryptocurrency Selection")
cryptocurrency = st.sidebar.selectbox("Select Cryptocurrency", ["bitcoin", "ethereum", "dogecoin"])
currency = st.sidebar.selectbox("Select Currency", ["usd", "eur", "gbp"])

# Fetch Cryptocurrency Data
def get_crypto_data(crypto, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    response = requests.get(url)
    return response.json()

if st.sidebar.button("Get Price"):
    crypto_data = get_crypto_data(cryptocurrency, currency)
    
    if cryptocurrency in crypto_data:
        price = crypto_data[cryptocurrency][currency]
        st.header(f"{cryptocurrency.capitalize()} Price")
        st.subheader(f"1 {cryptocurrency.capitalize()} = {price} {currency.upper()}")
    else:
        st.error("Error fetching cryptocurrency data. Please check your selection and try again.")

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
