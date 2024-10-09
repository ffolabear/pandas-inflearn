# 탐색적 데이터 분석: 1. 데이터의 출처와 주제에 대해 이해
import pandas as pd

#   전체 판매 프로세스
#   해당 쇼핑몰에 중소업체가 계약을 맺고
#   중소업체가 해당 쇼핑몰에 직접 상품을 올리고
#   고객이 구매하면, 중소업체가 Olist가 제공하는 물류 파트너를 활용해서 배송을 하고,
#   고객이 상품을 받으면, 고객에게 이메일 survey 가 전송되고,
#   고객이 이메일 survey 에 별점과 커멘트를 남겨서 제출하게 됨

# 데이터 출처
#   브라질에서 가장 큰 백화점의 이커머스 쇼핑몰 (https://olist.com/)
#   2016년도부터 2018년도 100k 개의 구매 데이터 정보
#   구매 상태, 가격, 지불수단, 물류 관련, 리뷰관련, 상품 정보, 구매자 지역 관련 정보


# 탐색적 데이터 분석: 2. 데이터의 크기 확인
products = pd.read_csv('../data/olist_products_dataset.csv')
print(products.head(), '\n')
print(products.info, '\n')
print(products.describe(), '\n')

order_items = pd.read_csv('../data/olist_order_items_dataset.csv')
print(order_items.info, '\n')

payments = pd.read_csv('../data/olist_order_payments_dataset.csv')
print(payments.info, '\n')

reviews = pd.read_csv('../data/olist_order_reviews_dataset.csv')
print(reviews.info, '\n')

seller = pd.read_csv('../data/olist_sellers_dataset.csv')
print(seller.info, '\n')

category = pd.read_csv('../data/product_category_name_translation.csv')
print(category.info, '\n')

customer = pd.read_csv('../data/olist_customers_dataset.csv')
print(customer.info, '\n')