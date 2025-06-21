import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn theme
sns.set_theme(style="whitegrid")

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Clean columns
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# KPIs
total_revenue = df["total_sales"].sum()
best_region = df.groupby("region")["total_sales"].sum().idxmax()
best_product = df.groupby("product")["total_sales"].sum().idxmax()

# Print KPIs
print(f"📊 Total Revenue: ₹{total_revenue:,.2f}")
print(f"🌍 Top Region by Revenue: {best_region}")
print(f"🏆 Best-Selling Product: {best_product}")

# Revenue by Region
plt.figure(figsize=(10, 6))
region_sales = df.groupby("region")["total_sales"].sum().sort_values()
sns.barplot(x=region_sales.values, y=region_sales.index, palette="viridis")
plt.title("Revenue by Region", fontsize=14, fontweight='bold')
plt.xlabel("Total Sales (₹)")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig("revenue_by_region.png", dpi=300)
plt.show()

# Revenue by Product
plt.figure(figsize=(10, 6))
product_sales = df.groupby("product")["total_sales"].sum().sort_values()
sns.barplot(x=product_sales.values, y=product_sales.index, palette="magma")
plt.title("Revenue by Product", fontsize=14, fontweight='bold')
plt.xlabel("Total Sales (₹)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("revenue_by_product.png", dpi=300)
plt.show()
