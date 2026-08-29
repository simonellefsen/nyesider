#!/usr/bin/env python3
"""Fetch 1-year price data from Yahoo Finance for the five candidate tickers."""

import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta
import time
import os

# Tickers with their expected data
TICKERS = {
    "NOVO-B.CO": {"currency": "DKK", "close_28aug": 295.50, "high52": 409.95, "low52": 224.25},
    "LULU": {"currency": "USD", "close_28aug": 120.81, "high52": 225.98, "low52": 104.44},
    "ZTS": {"currency": "USD", "close_28aug": 77.34, "high52": 155.38, "low52": 71.00},
    "RI.PA": {"currency": "EUR", "close_28aug": 63.20, "high52": 100.55, "low52": 58.60},
    "BMW.DE": {"currency": "EUR", "close_28aug": 62.64, "high52": 97.92, "low52": 56.40},
}

# ETFs/Indices for comparison
INDICES = {
    "^GSPC": {"name": "S&P 500", "currency": "USD"},  # S&P 500
    "^GDAXI": {"name": "DAX", "currency": "EUR"},     # DAX
    "^OMXC25": {"name": "OMXC25", "currency": "DKK"}, # Copenhagen
}

def fetch_yahoo_chart(ticker: str, range_str: str = "1y", interval: str = "1d"):
    """Fetch chart data from Yahoo Finance."""
    base_url = "https://query1.finance.yahoo.com/v8/finance/chart/"
    url = f"{base_url}{urllib.parse.quote(ticker)}?range={range_str}&interval={interval}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
            return data
    except urllib.error.HTTPError as e:
        print(f"HTTP Error for {ticker}: {e.code}")
        return None
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        return None

def parse_chart_data(data: dict) -> dict | None:
    """Parse Yahoo chart response into usable format."""
    if not data:
        return None
    
    try:
        result = data["chart"]["result"][0]
        timestamps = result["timestamp"]
        quote = result["indicators"]["quote"][0]
        
        closes = quote.get("close", [])
        highs = quote.get("high", [])
        lows = quote.get("low", [])
        
        # Filter out None values and build time series
        prices = []
        for i, ts in enumerate(timestamps):
            if closes[i] is not None:
                dt = datetime.fromtimestamp(ts)
                prices.append({
                    "date": dt.strftime("%Y-%m-%d"),
                    "close": round(closes[i], 2),
                    "high": round(highs[i], 2) if highs[i] else None,
                    "low": round(lows[i], 2) if lows[i] else None,
                })
        
        # Calculate 52-week high/low from the data
        valid_closes = [p["close"] for p in prices if p["close"]]
        high52 = max(valid_closes) if valid_closes else None
        low52 = min(valid_closes) if valid_closes else None
        
        return {
            "prices": prices,
            "high52_calc": high52,
            "low52_calc": low52,
            "currency": result.get("meta", {}).get("currency", "USD"),
        }
    except (KeyError, IndexError) as e:
        print(f"Parse error: {e}")
        return None

def main():
    output_dir = "content/aktier/issues/2026-08-nr1/data"
    os.makedirs(output_dir, exist_ok=True)
    
    all_data = {}
    
    # Fetch stock data
    for ticker, expected in TICKERS.items():
        print(f"Fetching {ticker}...")
        raw = fetch_yahoo_chart(ticker)
        parsed = parse_chart_data(raw)
        
        if parsed:
            all_data[ticker] = {
                **parsed,
                "expected": expected,
            }
            print(f"  Got {len(parsed['prices'])} data points, "
                  f"52w range: {parsed['low52_calc']:.2f}-{parsed['high52_calc']:.2f}")
        else:
            print(f"  FAILED - using synthetic data based on expected values")
            # Create synthetic data if fetch fails
            all_data[ticker] = create_synthetic_data(ticker, expected)
        
        time.sleep(1)  # Rate limiting
    
    # Fetch index data
    for ticker, info in INDICES.items():
        print(f"Fetching index {ticker} ({info['name']})...")
        raw = fetch_yahoo_chart(ticker)
        parsed = parse_chart_data(raw)
        
        if parsed:
            all_data[ticker] = {
                **parsed,
                "name": info["name"],
            }
            print(f"  Got {len(parsed['prices'])} data points")
        else:
            print(f"  FAILED")
        
        time.sleep(1)
    
    # Save all data
    output_file = os.path.join(output_dir, "yahoo_prices.json")
    with open(output_file, "w") as f:
        json.dump(all_data, f, indent=2)
    print(f"\nSaved to {output_file}")
    
    return all_data

def create_synthetic_data(ticker: str, expected: dict) -> dict:
    """Create synthetic price data when Yahoo fails, based on expected values."""
    import random
    random.seed(hash(ticker))
    
    prices = []
    current = expected["close_28aug"]
    high52 = expected["high52"]
    low52 = expected["low52"]
    
    # Work backwards from current price
    # Assume the high was ~6 months ago and we've declined since
    end_date = datetime(2026, 8, 28)
    start_date = end_date - timedelta(days=365)
    
    # Create a decline pattern
    num_days = 252  # Trading days in a year
    
    # Start near the high, decline to current
    start_price = high52 * 0.98  # Just under the high
    
    for i in range(num_days):
        date = start_date + timedelta(days=int(i * 365 / num_days))
        
        # Progress through the decline
        progress = i / num_days
        
        # Non-linear decline with volatility
        base_price = start_price - (start_price - current) * (progress ** 0.7)
        volatility = (high52 - low52) * 0.02
        noise = random.gauss(0, volatility)
        price = max(low52, min(high52, base_price + noise))
        
        prices.append({
            "date": date.strftime("%Y-%m-%d"),
            "close": round(price, 2),
        })
    
    return {
        "prices": prices,
        "high52_calc": high52,
        "low52_calc": low52,
        "currency": expected["currency"],
        "expected": expected,
        "synthetic": True,
    }

if __name__ == "__main__":
    import urllib.parse
    main()
