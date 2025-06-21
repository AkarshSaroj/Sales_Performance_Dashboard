import pandas as pd
import numpy as np

np.random.seed(42)
n_rows = 5000
dates = pd.date_range(start='2022-01-01', end='2024-12-31', freq='D')
sample_dates = np.random.choice(dates, n_rows)
regions = ['North', 'South', 'East', 'West', 'Central']
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
units_sold = np.random.randint(1, 100, size=n_rows)
unit_price = np.random.uniform(50, 500, size=n_rows).round(2)

sales_data = pd.DataFrame({
    'Date': sample_dates,
    'Region': np.random.choice(regions, n_rows),
    'Product': np.random.choice(products, n_rows),
    'Units_Sold': units_sold,
    'Unit_Price': unit_price
})
sales_data['Total_Sales'] = (sales_data['Units_Sold'] * sales_data['Unit_Price']).round(2)
sales_data = sales_data.sort_values(by='Date').reset_index(drop=True)

sales_data.to_csv("sales_data.csv", index=False)
print("✅ sales_data.csv has been created successfully!")
