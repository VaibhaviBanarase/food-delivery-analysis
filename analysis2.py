import pandas as pd

df = pd.read_csv("final_food_delivery_dataset.csv")

print(df.head())
print(df.columns)
print(df.info())

# Make sure date is parsed correctly
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

'''How many total orders were placed by users with Gold membership?'''

gold_orders = df[df['membership'] == 'Gold'].shape[0]
print("Total orders by Gold members:", gold_orders)

'''Total revenue generated from orders placed in Hyderabad city (rounded to nearest integer)'''
hyderabad_revenue = df[df['city'] == 'Hyderabad']['total_amount'].sum()
print("Total revenue in Hyderabad (rounded):", round(hyderabad_revenue))

'''How many distinct users placed at least one order?'''
distinct_users = df['user_id'].nunique()
print("Distinct users:", distinct_users)

'''Average order value for Gold members (rounded to 2 decimals)'''
avg_order_gold = df[df['membership'] == 'Gold']['total_amount'].mean()
print("Average order value for Gold members:", round(avg_order_gold, 2))

'''How many orders were placed for restaurants with rating ≥ 4.5?'''
high_rating_orders = df[df['rating'] >= 4.5].shape[0]
print("Orders with rating >= 4.5:", high_rating_orders)


'''How many orders were placed in the top revenue city among Gold members only?'''
gold_df = df[df['membership'] == 'Gold']
top_gold_city = gold_df.groupby('city')['total_amount'].sum().idxmax()
orders_top_gold_city = gold_df[gold_df['city'] == top_gold_city].shape[0]

print("Top Gold city:", top_gold_city)
print("Orders in top Gold city:", orders_top_gold_city)



