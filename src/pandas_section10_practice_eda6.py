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

# 요일/시간간 거래액 상관관계 알아보기

# 요일, 시간별 거래액
merged_order_payment_hour_weekday = merged_order_payment_date[['weekday', 'hour', 'payment_value']].copy()

# 멀티 인덱스
week_hour_sales_sum = merged_order_payment_hour_weekday.groupby(['weekday', 'hour']).sum()


# 인덱스 이름 바꾸기

def func(row):
    if row['weekday'] == 0:
        row['weekday'] = 'Sun'
    elif row['weekday'] == 1:
        row['weekday'] = 'Mon'
    elif row['weekday'] == 2:
        row['weekday'] = 'Tue'
    elif row['weekday'] == 3:
        row['weekday'] = 'Wed'
    elif row['weekday'] == 4:
        row['weekday'] = 'Thu'
    elif row['weekday'] == 5:
        row['weekday'] = 'Fri'
    elif row['weekday'] == 6:
        row['weekday'] = 'Sat'

    return row


merged_order_payment_hour_weekday = merged_order_payment_hour_weekday.reset_index()
merged_order_payment_hour_weekday = merged_order_payment_hour_weekday.apply(func, axis=1)
print(merged_order_payment_hour_weekday)

# 정렬
merged_order_payment_hour_weekday['weekday'] = pd.Categorical(
    merged_order_payment_hour_weekday['weekday']
    , categories=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    , ordered=True)
print(merged_order_payment_hour_weekday)
