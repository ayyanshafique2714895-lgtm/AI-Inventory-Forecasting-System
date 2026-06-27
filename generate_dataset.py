import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

products = [
    ("Polo Shirt", "Shirts", 35),
    ("Chino Pants", "Pants", 45),
    ("Oxford Shirt", "Shirts", 50),
    ("Cargo Pants", "Pants", 55),
    ("Linen Shirt", "Shirts", 40),
    ("Denim Jacket", "Outerwear", 80),
    ("Bomber Jacket", "Outerwear", 95),
    ("Crew Neck T-Shirt", "Essentials", 22),
    ("Henley Shirt", "Casual Wear", 38),
    ("Sweatshirt", "Casual Wear", 48),
    ("Hoodie", "Casual Wear", 55),
    ("Joggers", "Pants", 42),
    ("Shorts", "Pants", 30),
    ("Flannel Shirt", "Shirts", 44),
    ("Formal Shirt", "Shirts", 60),
]

start_date = datetime(2025, 1, 1)
days = 365

rows = []

for product, category, price in products:
    stock = np.random.randint(250, 500)
    base_demand = np.random.randint(8, 25)

    for i in range(days):
        date = start_date + timedelta(days=i)

        weekend_boost = 1.25 if date.weekday() >= 5 else 1.0
        holiday_boost = 1.4 if date.month in [11, 12] else 1.0
        summer_boost = 1.2 if category in ["Shirts", "Essentials"] and date.month in [6, 7, 8] else 1.0
        winter_boost = 1.3 if category == "Outerwear" and date.month in [10, 11, 12, 1, 2] else 1.0

        promotion = np.random.choice([0, 1], p=[0.85, 0.15])
        promo_boost = 1.3 if promotion == 1 else 1.0

        noise = np.random.normal(0, 3)

        units_sold = int(
            max(
                0,
                base_demand
                * weekend_boost
                * holiday_boost
                * summer_boost
                * winter_boost
                * promo_boost
                + noise
            )
        )

        if units_sold > stock:
            units_sold = stock

        stock -= units_sold

        if stock < 80:
            stock += np.random.randint(200, 400)

        revenue = units_sold * price

        rows.append({
            "Date": date.strftime("%Y-%m-%d"),
            "Product": product,
            "Category": category,
            "Units_Sold": units_sold,
            "Price": price,
            "Stock_Level": stock,
            "Revenue": revenue,
            "Promotion": promotion,
            "Day_Of_Week": date.weekday(),
            "Month": date.month
        })

df = pd.DataFrame(rows)

df.to_csv("sales_data.csv", index=False)

print("✅ Dataset created successfully!")
print(f"Rows created: {len(df)}")
print("File saved as: sales_data.csv")