import pandas as pd

PATH = "../data/"
payments = pd.read_csv(PATH + "olist_order_payments_dataset.csv", encoding='utf-8-sig')
orders = pd.read_csv(PATH + "olist_orders_dataset.csv", encoding='utf-8-sig')

# 시계열 데이터 다루기

df = pd.DataFrame({'order': ['2020-01-01 07:10:00',
                             '2020-01-08 07:20:30',
                             '2020-02-20 11:20:00',
                             '2020-02-20 04:40:50',
                             '2020-02-28 12:10:20',
                             '2019-01-10 17:23:50',
                             '2019-06-20 22:27:50',
                             '2019-06-20 21:15:59',
                             '2019-12-10 21:15:59',
                             ]})

# 이상한 값이 있을경우 에러를 발생시킬 수 있음
df['order'] = pd.to_datetime(df['order'], format='%Y-%m-%d %H:%M:%S', errors='raise')
# print(df.info())  # 올바른 값을 넣었을 경우 datatime64 객체로 올바르게 변환함

orders = orders.dropna()
payments = payments.groupby('order_id').sum()
merged_order = pd.merge(orders, payments, on='order_id')
print(merged_order.info())              # 현재는 datetime 객체가 아닌 object 타입이므로 변환이 필요한 상황

