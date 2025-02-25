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
]
units_sold = df.iloc[14:22,10]

plt.figure(figsize=(10, 6))
plt.bar(product_name, units_sold, color='g')

plt.xlabel('Product')
plt.ylabel('Price in dollars')
plt.title("Product and prices")

plt.xticks(rotation=90)

plt.show()
