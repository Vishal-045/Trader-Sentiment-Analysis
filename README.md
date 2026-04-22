📊 Trader Performance vs Market Sentiment

📌 Objective

The goal of this project is to analyze how market sentiment (Fear vs Greed) affects trader performance and behavior. The analysis is based on trading data and sentiment data to understand patterns and suggest better trading strategies.

📂 Project Structure

Trader Performance vs Market Sentiment.ipynb → Main notebook with full analysis

historical_data.csv → Trader data

fear_greed_index.csv → Market sentiment data

app.py → Streamlit dashboard for interactive analysis

README.md → Project summary

⚙️ Setup

Make sure you have Python installed (Python 3.8+ recommended).

Install required libraries:

pip install pandas matplotlib seaborn streamlit

▶️ How to Run
🔹 Run Notebook

Download or clone the repository

Navigate to the project folder

Open Jupyter Notebook:

jupyter notebook

Open and run:

Trader Performance vs Market Sentiment.ipynb

🔹 Run Streamlit Dashboard

Run the following command: streamlit run app.py

👉 This will open an interactive dashboard in your browser.

📊 Key Features

Data cleaning and preprocessing

Feature engineering (PnL, win rate, trade frequency, leverage proxy)

Sentiment-based analysis (Fear vs Greed)

Visualization of performance and behavior

Trader segmentation (leverage, frequency, consistency)

Interactive dashboard using Streamlit

Strategy recommendations

📈 Output

The project provides:

PnL comparison across sentiment

Trade frequency analysis

Leverage impact visualization

Long-short ratio analysis

Interactive dashboard for exploring results

Summary tables and insights

📝 Summary

From the analysis, it is clear that trader performance and behavior change based on market sentiment. During Fear, traders tend to earn higher profits but also face higher risk. During Greed, performance is more stable and controlled. The Streamlit dashboard helps in exploring these patterns interactively, making it easier to understand and analyze trader behavior.
