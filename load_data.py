import pandas as pd

# Load CSV file
orders = pd.read_csv("orders.csv")

# Show first 5 rows
print(orders.head())

users = pd.read_json("users.json")

#Load SQL File

import re

with open("restaurants.sql", "r", encoding="utf-8") as f:
    sql_text = f.read()

pattern = r"INSERT INTO restaurants VALUES\s*\((.*?)\);"
rows = re.findall(pattern, sql_text)

restaurants_data = []
for row in rows:
    parts = [p.strip().strip("'") for p in row.split(",")]
    restaurants_data.append(parts)

restaurants = pd.DataFrame(
    restaurants_data,
    columns=["restaurant_id", "restaurant_name", "cuisine", "rating"]
)

restaurants["restaurant_id"] = restaurants["restaurant_id"].astype(int)
restaurants["rating"] = restaurants["rating"].astype(float)

print(restaurants.head())
#MERGE ALL DATA (LEFT JOIN)
final_df = orders.merge(users, on="user_id", how="left")
final_df = final_df.merge(restaurants, on="restaurant_id", how="left")

print(final_df.head())
#FINAL CSV

final_df.to_csv("final_food_delivery_dataset.csv", index=False)
print("Final dataset created successfully!")


#
df_merged = orders.merge(users, on="user_id", how="left")

# Merge the above with restaurants on restaurant_id
df_final = df_merged.merge(restaurants, on="restaurant_id", how="left")

# Check number of rows
print("Total rows in final dataset:", df_final.shape[0])
