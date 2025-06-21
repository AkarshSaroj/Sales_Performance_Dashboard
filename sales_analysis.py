import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("sales_data.csv", parse_dates=['Date'])
df['Month'] = df['Date'].dt.to_period('M')

sns.set(style="whitegrid")

# Plot 1: Total Sales by Region
plt.figure(figsize=(8, 5))
region_sales = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
sns.barplot(x=region_sales.values, y=region_sales.index, palette='Blues_d')
plt.title('Total Sales by Region')
plt.xlabel('Sales in ₹')
plt.ylabel('Region')
plt.tight_layout()
plt.savefig("revenue_by_region.png")  # 🔥 Save as PNG
plt.show()

# Plot 2: Monthly Sales Trend
plt.figure(figsize=(12, 5))
monthly_sales = df.groupby('Month')['Total_Sales'].sum()
monthly_sales.index = monthly_sales.index.astype(str)
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')
plt.xticks(rotation=45)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales in ₹')
plt.tight_layout()
plt.savefig("monthly_sales_trend.png") # 🔥 Save as PNG
plt.show()

# Plot 3: Top 5 Products by Total Sales
plt.figure(figsize=(8, 5))
product_sales = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(5)
sns.barplot(x=product_sales.values, y=product_sales.index, palette='Greens_d')
plt.title('Top 5 Best-Selling Products')
plt.xlabel('Sales in ₹')
plt.ylabel('Product')
plt.tight_layout()
plt.savefig("revenue_by_product.png")  # 🔥 Save as PNG
plt.show()
