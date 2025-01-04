import os
import yfinance as yf # type: ignore

ticker = os.getenv("TICKER") + ".NS"

start_date = "2000-01-01"
end_date = "2024-10-31"

data = yf.download(ticker, start=start_date, end=end_date)

if not data.empty:
    csv_file = f"stocks/{ticker}.csv"
    data.to_csv(csv_file)
    print(f"Historical data saved to {csv_file}")
