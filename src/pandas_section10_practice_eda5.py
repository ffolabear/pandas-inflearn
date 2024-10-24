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

merged_order_payment_date['order_purchase_timestamp'] = pd.to_datetime(
    merged_order_payment_date['order_purchase_timestamp'])
merged_order_payment_date = merged_order_payment_date.set_index('order_purchase_timestamp')

# 월별 분석
monthly_merged_order_month_count = merged_order_payment_date.groupby(pd.Grouper(freq='ME')).count()
# print(monthly_merged_order_month_count.head(), '\n')

# 일별 분석
daily_merged_order_month_count = merged_order_payment_date.groupby(pd.Grouper(freq='D')).count()
# print(daily_merged_order_month_count.head(), '\n')

# 시간별 분석
merged_order_payment_date = merged_order[['order_purchase_timestamp', 'payment_value']].copy()
# print(merged_order_payment_date.head(), '\n')

# 관련 함수 찾기
# print(dir(merged_order_payment_date['order_purchase_timestamp'].dt))

# 분기 추출
# print(merged_order_payment_date['order_purchase_t imestamp'].dt.quarter)

# 각종 일자별 정보 추출
merged_order_payment_date['year'] = merged_order_payment_date['order_purchase_timestamp'].dt.year
merged_order_payment_date['monthday'] = merged_order_payment_date['order_purchase_timestamp'].dt.day
merged_order_payment_date['weekday'] = merged_order_payment_date['order_purchase_timestamp'].dt.weekday
merged_order_payment_date['month'] = merged_order_payment_date['order_purchase_timestamp'].dt.month
merged_order_payment_date['hour'] = merged_order_payment_date['order_purchase_timestamp'].dt.hour
merged_order_payment_date['quarter'] = merged_order_payment_date['order_purchase_timestamp'].dt.quarter
merged_order_payment_date['minute'] = merged_order_payment_date['order_purchase_timestamp'].dt.minute

# print(merged_order_payment_date)


# 연도별 분석
merged_order_payment_year = merged_order_payment_date[['year', 'payment_value']].copy()
merged_order_payment_year = merged_order_payment_year.groupby('year').sum()
# print(merged_order_payment_year)

# 요일별 분석
# 0 부터 일요일, 6은 토요일
merged_order_payment_weekday = merged_order_payment_date[['weekday', 'payment_value']].copy()
merged_order_payment_weekday = merged_order_payment_weekday.groupby('weekday').sum().reset_index()

# 요일 딕셔너리 생성
weekday_map = {
    0: 'Sun',  # 일요일
    1: 'Mon',  # 월요일
    2: 'Tue',  # 화요일
    3: 'Wed',  # 수요일
    4: 'Thu',  # 목요일
    5: 'Fri',  # 금요일
    6: 'Sat'  # 토요일
}

merged_order_payment_weekday['weekday'] = merged_order_payment_weekday['weekday'].map(weekday_map)
merged_order_payment_weekday = merged_order_payment_weekday.set_index('weekday')
# print(merged_order_payment_weekday)

# 계절별 분석

merged_order_payment_quarter = merged_order_payment_date[['quarter', 'payment_value']].copy()
merged_order_payment_quarter = merged_order_payment_quarter.groupby('quarter').sum().reset_index()
# print(merged_order_payment_quarter)

# 분기 딕셔너리 생성
quarter_map = {
    1: '1Q',  # 월요일
    2: '2Q',  # 화요일
    3: '3Q',  # 수요일
    4: '4Q',  # 목요일
}

merged_order_payment_quarter['quarter'] = merged_order_payment_quarter['quarter'].map(quarter_map)
merged_order_payment_quarter = merged_order_payment_quarter.set_index('quarter')
# print(merged_order_payment_quarter)

# 시간별 분석
merged_order_payment_hour = merged_order_payment_date[['hour', 'payment_value']].copy()
merged_order_payment_hour = merged_order_payment_hour.groupby('hour').sum().reset_index()
# print(merged_order_payment_hour)

# 분 단위 분석
merged_order_payment_minute = merged_order_payment_date[['minute', 'payment_value']].copy()
merged_order_payment_minute = merged_order_payment_minute.groupby('minute').sum().reset_index()
# print(merged_order_payment_minute)


