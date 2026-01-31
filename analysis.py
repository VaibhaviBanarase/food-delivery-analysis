import pandas as pd

df = pd.read_csv("final_food_delivery_dataset.csv")

print(df.head())
print(df.columns)
print(df.info())


df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)


print(df.isna().sum())

'''Which city has the highest total revenue (total_amount) from Gold members?'''
df_gold = df[df['membership'] == 'Gold']
df_gold.groupby('city')['total_amount'].sum().sort_values(ascending=False)


'''Which cuisine has the highest average order value across all orders?'''
df.groupby('cuisine')['total_amount'].mean().sort_values(ascending=False)

'''How many distinct users placed orders worth more than ₹1000 in total?'''
df.groupby('user_id')['total_amount'].sum().gt(1000).sum()

'''Which restaurant rating range generated the highest total revenue?'''
bins = [3.0, 3.5, 4.0, 4.5, 5.0]
labels = ['3.0–3.5','3.6–4.0','4.1–4.5','4.6–5.0']
df['rating_range'] = pd.cut(df['rating'], bins=bins, labels=labels, include_lowest=True)
df.groupby('rating_range')['total_amount'].sum().sort_values(ascending=False)

'''Among Gold members, which city has the highest average order value?'''
df_gold.groupby('city')['total_amount'].mean().sort_values(ascending=False)

'''During which quarter of the year is the total revenue highest?'''
df['quarter'] = pd.to_datetime(df['order_date'], dayfirst=True).dt.quarter
df.groupby('quarter')['total_amount'].sum().sort_values(ascending=False)


