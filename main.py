import pandas as pd
import matplotlib.pyplot as plt

# Sales dataset
data = {
    "Product": ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse"],
    "Sales": [150, 200, 120, 90, 60]
}

df = pd.DataFrame(data)

print("Sales Dataset:")
print(df)

# Total Sales
total_sales = df["Sales"].sum()

# Average Sales
average_sales = df["Sales"].mean()

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)

# Top selling product
top_product = df.loc[df["Sales"].idxmax()]

print("Top Selling Product:")
print(top_product)

# Bar Graph
plt.bar(df["Product"], df["Sales"])
plt.title("Product Sales Bar Graph")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# Line Graph
plt.plot(df["Product"], df["Sales"], marker='o')
plt.title("Product Sales Line Graph")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()