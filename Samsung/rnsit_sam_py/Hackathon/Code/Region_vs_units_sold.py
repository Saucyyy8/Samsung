import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\SIC\Desktop\retail_store_inventory.csv")

print(df.columns)

product_name = df.iloc[:10, 4]
units_sold = df.iloc[:10,6]

plt.figure(figsize=(10, 6))
plt.bar(product_name, units_sold, color='y')

plt.xlabel('Region')
plt.ylabel('Units Sold')
plt.title("Region vs Units sold")

plt.xticks(rotation=90)

plt.show()