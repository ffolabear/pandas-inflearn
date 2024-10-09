import pandas as pd

# pd.options.display.max_rows = None
# pd.options.display.max_columns = None

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

# 주요 질문(탐색하고자 하는 질문 리스트)
#   얼마나 많은 고객이 있는가?
#   고객은 어디에 주로 사는가?
#   고객은 주로 어떤 지불방법을 사용하는가?
#   평균 거래액은 얼마일까?
#   일별, 주별, 월별 판매 트렌드는?
#   어떤 카테고리가 가장 많은 상품이 팔렸을까?

# print(customers.head())


#   얼마나 많은 고객이 있는가?

# customer_id 와 customer_unique_id 차이점 찾기
# print(customers['customer_unique_id'].value_counts().max())  # 17 = 중복된 값 다수 존재
# print(customers['customer_id'].value_counts().max())  # 1 이 나왔다는 것은 중복된 값이 없다는 뜻

# nunique(): unique 한 값의 갯수를 알려줌
# print(customers['customer_id'].nunique())  # 실제 고객의 수
# print(customers['customer_unique_id'].nunique())

# =====================================================================

#   고객은 어디에 주로 사는가?

# customer_id 가 유일한 값이기 때문에 카운팅 용도로 사용
# customers_location = customers.groupby('customer_city').count().sort_values(by='customer_id', ascending=False)
# 다른 방법
#
top20_customers_location = customers.groupby('customer_city')['customer_id'].nunique().sort_values(ascending=False)
# print(top20_customers_location.head())

# 리스트로 출력
# print(top20_customers_location.index.tolist())

# =====================================================================

#   고객은 주로 어떤 지불방법을 사용하는가?
print(payments['payment_type'].unique())

# 의미 없는 데이터삭제하기
payments = payments[payments['payment_type'] != 'not_defined']

# 결제 방법별 카운트
payments_type = payments.groupby('payment_type')['order_id'].nunique().sort_values(ascending=False)
print(payments_type)

