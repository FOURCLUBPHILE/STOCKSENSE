import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
import os
import sys

# --- CONFIGURATION ---
# This looks professional: defining paths at the top
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')
OUTPUT_DIR = os.path.join(CURRENT_DIR, '..', 'outputs')
LOG_DIR = os.path.join(CURRENT_DIR, '..', 'logs')

# Ensure directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Setup Logging (Writes to a file)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'system.log'),
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

class StockSense:
    def __init__(self):
        self.df = None
        logging.info("StockSense System Initialized.")

    def load_data(self):
        """Loads data from CSV. Concept: File I/O, Error Handling."""
        try:
            file_path = os.path.join(DATA_DIR, 'raw_inventory.csv')
            self.df = pd.read_csv(file_path)
            # Feature Engineering
            self.df['Total_Revenue'] = self.df['Units_Sold'] * self.df['Unit_Price']
            logging.info(f"Data loaded successfully. Shape: {self.df.shape}")
            print("✅ Data Loaded from CSV")
        except FileNotFoundError:
            logging.error("CSV file not found!")
            sys.exit("Error: raw_inventory.csv missing in /data folder")

    def analyze_sales(self):
        """Concept: Pandas Grouping, Aggregation"""
        print("\n📊 Sales Analysis (Top Products)")
        top_products = self.df.groupby('Product_Name')[['Units_Sold', 'Total_Revenue']].sum().sort_values(by='Total_Revenue', ascending=False)
        print(top_products)
        logging.info("Sales analysis performed.")

    def check_inventory(self):
        """Concept: Boolean Indexing, Business Logic"""
        print("\n⚠️ Low Stock Alert (Threshold < 10)")
        low_stock = self.df[self.df['Current_Stock'] < 10]
        
        if not low_stock.empty:
            print(low_stock[['Product_Name', 'Current_Stock']].to_string(index=False))
            logging.warning(f"Low stock detected for {len(low_stock)} items.")
        else:
            print("Inventory Healthy.")
            logging.info("Inventory check passed.")

    def generate_visuals(self):
        """Concept: Matplotlib Visualization"""
        print("\n📈 Generating Visual Report...")
        revenue_over_time = self.df.groupby('Date')['Total_Revenue'].sum()
        
        plt.figure(figsize=(10, 5))
        plt.plot(revenue_over_time.index, revenue_over_time.values, marker='o', color='green')
        plt.title("Daily Revenue Trends")
        plt.xlabel("Date")
        plt.ylabel("Revenue ($)")
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Save instead of show
        save_path = os.path.join(OUTPUT_DIR, 'revenue_trend.png')
        plt.savefig(save_path)
        plt.close()
        print(f"✅ Report saved to {save_path}")
        logging.info("Visualization report generated.")

if __name__ == "__main__":
    app = StockSense()
    app.load_data()
    app.analyze_sales()
    app.check_inventory()
    app.generate_visuals()