import pandas as pd

PATH = "../data/"
payments = pd.read_csv(PATH + "olist_order_payments_dataset.csv", encoding='utf-8-sig')
orders = pd.read_csv(PATH + "olist_orders_dataset.csv", encoding='utf-8-sig')

# 월별 거래건수 확인하기

orders = orders.dropna()
merged_order = pd.merge(orders, payments, on='order_id')

merged_order_payment_date = merged_order[['order_purchase_timestamp', 'payment_value']].copy()

# order_purchase_timestamp 의 날짜 데이터를 기반으로 월별 계산을 해야 하므로 datetime 타입으로 변환
merged_order['order_purchase_timestamp'] = pd.to_datetime(merged_order['order_purchase_timestamp'],
                                                          format='%Y-%m-%d %H:%M:%S', errors='raise')

# 인덱스로 만들기
print(merged_order_payment_date.index)
# merged_order_payment_date = merged_order_payment_date.set_index('order_purchase_timestamp')
# merged_order_payment_date.index = pd.to_datetime(merged_order_payment_date.index)

merged_order_payment_date['order_purchase_timestamp'] = pd.to_datetime(merged_order_payment_date['order_purchase_timestamp'])
merged_order_payment_date = merged_order_payment_date.set_index('order_purchase_timestamp')

# 인덱스로 만들었기 때문에 컬럼을 쓰지 않아도 됨
merged_order_month_count = merged_order_payment_date.groupby(pd.Grouper(freq='ME')).count()
print(merged_order_month_count.head())