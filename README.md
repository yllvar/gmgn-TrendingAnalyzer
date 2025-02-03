# 🚀 GMGN Trending Token Analyzer

---

<img width="1138" alt="Screenshot 2025-02-03 at 19 11 42" src="https://github.com/user-attachments/assets/61dfce39-417d-47ef-b166-0b6c108fe815" />

A sophisticated tool for analyzing trending cryptocurrency tokens across multiple timeframes using the GMGN.ai wrapper. The analyzer aggregates data, filters tokens based on key metrics, and provides visual analytics along with expert analysis.

<img width="1360" alt="Screenshot 2025-02-03 at 19 19 18" src="https://github.com/user-attachments/assets/6bdcf69e-8c7f-4a0e-b6d4-f0d1b8501363" />

---

## 🔥 Features

- 📊 **Multi-timeframe token trend analysis** (1m, 5m, 1h, 6h, 24h)
- 📈 **Data aggregation and filtering** based on volume, market cap, and consistency
- 🎨 **Automated visualization generation**
- ⏳ **Continuous monitoring** with automated refresh

## 📌 Technical Analysis Components

### 🏷️ Token Analysis Logic
- Fetches trending tokens across multiple timeframes
- Collects key metrics:
  - 🆔 Token ID, 🔗 Chain, 🏠 Address
  - 🔤 Symbol, 💰 Price, 📊 Volume
  - 🌎 Market Cap, 📉 Price Change Percentage
- 🚨 Error handling for API requests
- 🔍 Validation of token data integrity

### 📊 Aggregation Logic
- Groups tokens by address
- Calculates key aggregated metrics:
  - 📈 Average price and volume
  - 📏 Median market cap
  - 🔀 Price change trends
  - 🔁 **Consistency count** (appearance across timeframes)
- **Filtering criteria:**
  - ✅ Minimum **volume threshold**: 1000
  - ✅ Minimum **market cap threshold**: 10000
  - ✅ Minimum **consistency count**: 3 timeframes

### 📉 Visualization Logic
- Generates **scatter plot visualization**:
  - 📍 X-axis: **Median Market Cap** (log scale)
  - 📍 Y-axis: **Average Volume** (log scale)
  - 🎈 Bubble size: **Consistency count**
  - 🎨 Color gradient: **Average price change**
- 🔤 Includes **token symbol annotations**
- 🖼️ Saves **high-resolution plot** (300 DPI)

## 🛠 Installation

1️⃣ Clone the repository:
```bash
git clone https://github.com/yllvar/gmgn-TrendingAnalyzer.git
cd gmgn-TrendingAnalyzer
```

2️⃣ Create and activate a **virtual environment** (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the analyzer:
```bash
python analyzer.py
```

The script will:
- 📡 Fetch trending tokens **every 60 seconds**
- 🧠 Generate **analysis and visualizations**
- 🖼️ Save plots as **'trending_analysis_plot.png'**
- 🖥️ Display token data and analysis in the **console**

To stop the script, press **Ctrl+C**.

## 📤 Output

The analyzer produces:
- 📑 **Tabulated token data** with key metrics
- 🔗 **List of token addresses** for easy reference
- 📊 **Visual plot saved** as `'trending_analysis_plot.png'`

## 📦 Dependencies

- 🐍 `pandas` – Data manipulation and analysis
- 📊 `matplotlib` – Data visualization
- 📜 `tabulate` – Console table formatting
- 🔑 `python-dotenv` – Environment variable management

## ⚠️ Notes

- 🌐 **Ensure a stable internet connection** for API calls
- 🚦 **Monitor API rate limits** to prevent errors
- 🔒 **Keep API keys secure** and never commit them to version control

---

