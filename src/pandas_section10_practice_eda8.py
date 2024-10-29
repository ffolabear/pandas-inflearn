import pandas as pd
import datetime as dt

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

# 평균 배송 시간은?
# print(orders.isnull().sum())

# 결측치가 있는행은 전부 삭제
orders = orders.dropna()
# print(orders.info())

# 배송시간 측정하는 컬럼 추가
orders['delivery_time'] = pd.to_datetime(orders['order_delivered_customer_date']) - pd.to_datetime(
    orders['order_purchase_timestamp'])
# print(orders['delivery_time'].describe())

# 데이터의 특이값을 제외
# 0 ~ 95% 데이터만 가져오는 것 의미 -> 특이값이 크다는 뜻
delivery_time_q95 = orders['delivery_time'].quantile(0.95)
# print(delivery_time_q95)

delivery_time_q90 = orders['delivery_time'].quantile(0.90)
# print(delivery_time_q90)

# 0~95 데이터만 가져오기
orders = orders[orders['delivery_time'] < delivery_time_q95]

# 월별 평균 배송시간 분석
orders_date = orders[['order_purchase_timestamp', 'delivery_time']].copy()

# 계산을 위해 datetime 으로 변환
orders_date['order_purchase_timestamp'] = pd.to_datetime(orders_date['order_purchase_timestamp'],
                                                         format='%Y-%m-%d %H:%M:%S')

# 계산하기 쉽게 나노초를 일반 초로 변환
orders_date['delivery_time'] = orders_date['delivery_time'].dt.total_seconds()
orders_date = orders_date.set_index('order_purchase_timestamp')

# 한달 단위로 그룹핑
orders_date = orders_date.groupby(pd.Grouper(freq='ME')).mean()

# 초를 하루로 변환
orders_date['delivery_time'] = orders_date['delivery_time'] / 86400
print(orders_date)
