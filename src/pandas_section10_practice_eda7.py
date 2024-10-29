import pandas as pd

PATH = "../data/"
products = pd.read_csv(PATH + "olist_products_dataset.csv", encoding='utf-8-sig')
customers = pd.read_csv(PATH + "olist_customers_dataset.csv", encoding='utf-8-sig')
geolocation = pd.read_csv(PATH + "olist_geolocation_dataset.csv", encoding='utf-8-sig')
order_items = pd.read_csv(PATH + "olist_order_items_dataset.csv", encoding='utf-8-sig')
payments = pd.read_csv(PATH + "olist_order_payments_dataset.csv", encoding='utf-8-sig')
reviews = pd.read_csv(PATH + "olist_order_reviews_dataset.csv", encoding='utf-8-sig')
orders = pd.read_csv(PATH + "olist_orders_dataset.csv", encoding='utf-8-sig')
sellers = pd.read_csv(PATH + "olist_sellers_dataset.csv", encoding='utf-8-sig')
category_name = pd.read_csv(PATH + "product_category_name_translation.csv", encoding='utf-8-sig')
orders = orders.dropna()
merged_order = pd.merge(orders, payments, on='order_id')
merged_order_payment_date = merged_order[['order_purchase_timestamp', 'payment_value']].copy()
merged_order_payment_date['order_purchase_timestamp'] = pd.to_datetime(
    merged_order_payment_date['order_purchase_timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')
merged_order_payment_date['year'] = merged_order_payment_date['order_purchase_timestamp'].dt.year
merged_order_payment_date['monthday'] = merged_order_payment_date['order_purchase_timestamp'].dt.day
merged_order_payment_date['weekday'] = merged_order_payment_date['order_purchase_timestamp'].dt.weekday
merged_order_payment_date['month'] = merged_order_payment_date['order_purchase_timestamp'].dt.month
merged_order_payment_date['hour'] = merged_order_payment_date['order_purchase_timestamp'].dt.hour
merged_order_payment_date['quarter'] = merged_order_payment_date['order_purchase_timestamp'].dt.quarter
merged_order_payment_date['minute'] = merged_order_payment_date['order_purchase_timestamp'].dt.minute

# 어떤 카테고리가 가장 많은 상품이 팔렸을까?

# 상품정보 영어로 보기 위해 데이터프레임 합치기
product_category = pd.merge(category_name, products, on='product_category_name')

# 주문 정보와 합치기
product_category_order = pd.merge(product_category, order_items, on='product_id')
print(product_category_order.columns)

# 카테고리별 거래 건수 확인하기
product_category_order = product_category_order.groupby('product_category_name_english').aggregate({'order_id' : 'count'}).rename(columns={'order_id': 'order_count'})

