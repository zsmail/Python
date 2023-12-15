import yfinance as yf
from datetime import datetime

# This script fetches and prints the latest stock prices for selected tech stocks.
# It uses yfinance, a popular library for accessing financial data, and displays
# the current price along with the daily percentage change.

# Define the stock tickers for major tech companies.
tickers = ["AAPL", "AMZN", "META"]

# Get the current date in YYYY-MM-DD format.
current_date = datetime.now().strftime("%Y-%m-%d")

# Start the print content with the date and a header for clarity.
print_content = f"{current_date} | Tech Stocks (NYSE):\n"

# Fetch stock prices and append to the print content.
for ticker in tickers:
    stock = yf.Ticker(ticker)  # Create a Ticker object for the stock.
    stock_info = stock.info    # Fetch stock information.

    # Extract the current price, previous close, and currency from the stock info.
    current_price = stock_info.get('currentPrice', 'N/A')
    prev_close = stock_info.get('previousClose', 'N/A')
    currency = stock_info.get('currency', 'N/A')

    # Calculate the percentage change from the previous close and determine the emoji.
    # Emoji is 🔼 for positive change and 🔽 for negative change.
    if current_price != 'N/A' and prev_close != 'N/A' and prev_close != 0:
        change_percent = ((current_price - prev_close) / prev_close) * 100
        change_emoji = "🔼" if change_percent > 0 else "🔽"
    else:
        change_percent = 'N/A'
        change_emoji = ''

    # Append each stock's info to the print content in a readable format.
    print_content += f"${ticker}: {current_price} {currency} {change_emoji} ({change_percent:.2f}%)\n"

# Print the final content with all the stock information.
print(print_content)
