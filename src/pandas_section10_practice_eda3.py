import pandas as pd

# pd.options.display.max_rows = None
# pd.options.display.max_columns = None

PATH = "../data/"

order_items = pd.read_csv(PATH + "olist_order_items_dataset.csv", encoding='utf-8-sig')
payments = pd.read_csv(PATH + "olist_order_payments_dataset.csv", encoding='utf-8-sig')
orders = pd.read_csv(PATH + "olist_orders_dataset.csv", encoding='utf-8-sig')

# 주요 질문(탐색하고자 하는 질문 리스트)
#   얼마나 많은 고객이 있는가?
#   고객은 어디에 주로 사는가?
#   고객은 주로 어떤 지불방법을 사용하는가?
#   평균 거래액은 얼마일까?
#   일별, 주별, 월별 판매 트렌드는?
#   어떤 카테고리가 가장 많은 상품이 팔렸을까?


#   평균 거래액은 얼마일까?

# 없는 데이터 삭제하기
orders = orders.dropna()

# orders 와 payment 사이즈 비교
# print(payments.info, '\n')
# print(orders.info)

# print(orders['order_id'].value_counts().max())              # 1
# print(payments['order_id'].value_counts().max())            # 29 -> 중복된 값 다수 존재

# 총 지불금액 합치기
# merge 시 없는 값은 NaN 처리
merged_order = pd.merge(orders, payments, on='order_id', how='left')                # 데이터 전처리 완료
print(merged_order)

