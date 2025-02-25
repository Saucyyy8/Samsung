import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\SIC\Desktop\retail_store_inventory.csv")

print(df.columns)

product_name =[
    "Gulab Jamun",
    "Jalebi",
    "Ladoo",
    "Barfi",
    "Rasgulla",
    "Kheer",
    "Halwa",
    "Peda",
    "Mysore Pak",
    "Sandesh"
]
units_sold = df.iloc[:10, 7]

plt.figure(figsize=(10, 6))
plt.bar(product_name, units_sold)

plt.xlabel('Product Name')
plt.ylabel('Number of items sold in a day')
plt.title('Product vs Units Sold')

plt.xticks(rotation=90)

plt.show()
