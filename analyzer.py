from gmgn import gmgn
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Initialize the gmgn instance.
    gm = gmgn()

    # Define the timeframes to aggregate results from.
    timeframes = ["1m", "5m", "1h", "6h", "24h"]
    data = []  # List to store token entries across timeframes

    # Iterate over each timeframe.
    for tf in timeframes:
        trending_tokens = gm.getTrendingTokens(timeframe=tf)
        # Extract tokens assuming the key is 'rank'
        tokens = trending_tokens.get("rank", [])
        for token in tokens:
            # Build a dictionary that includes an extra field for price change.
            # (The API returns "price_change_percent" in the token data.)
            data.append({
                "id": token.get("id"),
                "chain": token.get("chain"),
                "address": token.get("address"),
                "symbol": token.get("symbol"),
                "price": token.get("price"),
                "volume": token.get("volume"),
                "market_cap": token.get("market_cap"),
                "timeframe": tf,
                "price_change": token.get("price_change_percent")
            })

    # Convert the list of records into a pandas DataFrame.
    df = pd.DataFrame(data)

    # Group by token address and aggregate metrics.
    grouped = df.groupby("address").agg({
         "id": "first",           # Take the first observed id.
         "chain": "first",        # Assume chain remains the same.
         "symbol": "first",       # Assume token symbol is invariant.
         "price": "mean",         # Average price.
         "volume": "mean",        # Average volume.
         "market_cap": "median",  # Median market cap as a robust statistic.
         "timeframe": "nunique",  # Number of different timeframes the token appears in.
         "price_change": "mean"   # Average price change (if available).
    }).rename(columns={
         "timeframe": "consistency_count",
         "price": "avg_price",
         "volume": "avg_volume",
         "market_cap": "median_market_cap",
         "price_change": "avg_price_change"
    })

    # Apply filters:
    # 1. Only tokens that appear in at least 3 different timeframes.
    # 2. Only tokens with average volume and median market cap above given thresholds.
    volume_threshold = 1000      # Adjust threshold as needed.
    market_cap_threshold = 10000 # Adjust threshold as needed.
    filtered = grouped[
        (grouped["consistency_count"] >= 3) &
        (grouped["avg_volume"] >= volume_threshold) &
        (grouped["median_market_cap"] >= market_cap_threshold)
    ]

    # Sort by consistency count and then by average volume (both descending).
    filtered = filtered.sort_values(by=["consistency_count", "avg_volume"], ascending=False).reset_index()

    # Print the aggregated results in a grid format using tabulate.
    print(tabulate(filtered, headers='keys', tablefmt="grid", showindex=False))

    # Save the aggregated table to a CSV file.
    filtered.to_csv("trending_analysis.csv", index=False)
    print("\nSaved aggregated trending tokens to trending_analysis.csv.")

    # --- Visualization with matplotlib ---
    plt.figure(figsize=(12, 8))

    # Create a scatter plot:
    # - x-axis: median market cap (log scale)
    # - y-axis: average volume (log scale)
    # - Bubble size: consistency_count (scaled up for visibility)
    # - Color: average price change percentage.
    scatter = plt.scatter(filtered['median_market_cap'],
                          filtered['avg_volume'],
                          s=filtered['consistency_count'] * 100,  # scale bubble size
                          c=filtered['avg_price_change'],
                          cmap='coolwarm',
                          alpha=0.8)

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Median Market Cap")
    plt.ylabel("Average Volume")
    plt.title("Trending Tokens: Market Cap vs. Volume\n(bubble size = consistency count, color = avg price change)")

    cbar = plt.colorbar(scatter)
    cbar.set_label("Average Price Change (%)")

    # Annotate each point with the token's symbol.
    for idx, row in filtered.iterrows():
        plt.annotate(row["symbol"],
                     (row['median_market_cap'], row['avg_volume']),
                     fontsize=8,
                     alpha=0.75)

    plt.tight_layout()
    plt.savefig("trending_analysis_plot.png", dpi=300)  # Save the chart as an image.
    plt.show()

if __name__ == "__main__":
    main()