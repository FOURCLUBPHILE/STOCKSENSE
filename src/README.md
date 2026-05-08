StockSense – Smart Inventory Analyzer

A production-grade Python application for analyzing sales data and monitoring inventory health.

🏗 Project Structure

The project follows a modular directory structure to separate source code, data, logs, and output reports.


StockSense/├── src/               
# Source code├── data/              # Input CSV datasets├── outputs/           # Generated visual reports├── logs/              # System execution logs└── requirements.txt   # Dependencies


🚀 Tech Stack
Python: Core application logic.
Pandas: Data analysis (Grouping, Aggregation) and CSV parsing.
NumPy: Underlying numerical operations.
Matplotlib: Report generation (Revenue trends).
Logging Module: System monitoring and error tracking.


📋 Features
CSV Data Ingestion: Robust file handling to load external sales data.
Automated Analysis: Calculates top-selling products and revenue totals.
Inventory Monitoring: Dynamic alerts for stock levels below threshold.
Logging System: Automatically tracks application actions and errors to logs/system.log.
Reporting: Generates and saves professional revenue trend charts




🛠 Installation
Clone the repository.
Install dependencies:
bash
pip install -r requirements.txt

Run the analyzer:
bash

python src/analyzer.py

View the generated chart in outputs/ and logs in logs/.
text


View the generated chart in outputs/ and logs in logs/.

