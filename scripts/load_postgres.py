import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://admin:password123@localhost:5432/ecommerce_source')

# Load sample transactional tables
df_orders = pd.read_csv('data/bronze/olist_orders_dataset.csv')
df_orders.to_sql('orders', engine, if_exists='replace', index=False)

df_items = pd.read_csv('data/bronze/olist/olist_order_items_dataset.csv')
df_items.to_sql('order_items', engine, if_exists='replace', index=False)

print("✅ Data loaded to Postgres")