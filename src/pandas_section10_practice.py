# 연습문제와 추가 문법으로 정리하는 pandas
import pandas as pd

# 1. 00_data/olist_customers_dataset.csv 파일 pandas dataframe 으로 읽어오기 (데이터프레임 변수 이름은 doc 로 하기로 함)
doc = pd.read_csv("../data/00_data/olist_customers_dataset.csv", encoding='utf-8-sig')
print(doc, '\n')

# 2. 처음 5개 열 확인하기
print("처음 5개 열 : \n", doc.head(5), '\n')

# 3. 전체 record 수(행 수) 확인하기
print("전체 record 수 : ", doc.shape, '\n')

# 4. 전체 열의 수 확인하기
print("전체 열의 수 : ", doc.info, '\n')

# 5. 열의 이름 리스트로 가져오기
print("열의 이름 리스트 : ", doc.columns, '\n')

# 6. 인덱스 확인하기
print("인덱스 : ", doc.index, '\n')

# 7. 다섯 숫자 요약(5 number summary) 확인하기
print("다섯 숫자 요약 : ", doc.describe(), '\n')

# 추가 문법 pandas.DataFrame.copy

# 8. customer_zip_code_prefix, customer_city, customer_state 컬럼만 가져오기 (데이터프레임 변수 이름은 doc2로 하기로 함)
doc2 = doc[['customer_zip_code_prefix', 'customer_city', 'customer_state']].copy()
print("컬럼 가져오기 : ", doc2, '\n')

# 9. customer_city 가 sao paulo 인 레코드(행)만 가져오기 (데이터프레임 변수 이름은 doc3 으로 하기로 함)
#   - 레코드(행) 수 확인도 해보기
doc3 = doc2[doc2['customer_city'] == 'sao paulo']
print("sao paulo : ", doc, '\n')

# 10. customer_city 기준으로 행의 갯수를 확인해보세요
#   - doc2에 value_counts() 를 써보세요 (value_counts() 는 Series 에만 적용 가능합니다.)
print("행의 갯수를 확인 : ", doc2['customer_city'].value_counts(), '\n')

# 11. doc 데이터프레임에서 customer_city 기준으로 행의 갯수를 확인해보세요
#   1. groupby 를 써서 customer_city 를 기준으로 행의 갯수를 count 하세요 (새로운 데이터프레임 변수 이름은 doc4로 하기로 함)
#   2. doc4를 통해 customer_city 수도 확인해보세요 (데이터프레임 레코드(행) 수를 확인해보면 됩니다.)
doc4 = doc.groupby('customer_city').count()
print(doc4, '\n')
print(doc4.index, '\n')
print(doc4.shape, '\n')


# 추가 문법 이해 (정렬, sort_values(), sort_index())

# 12. doc4에서 가장 레코드(행)의 수가 많은 customer_city 를 확인해보세요
#   1. doc4의 customer_id 를 기준으로 정렬하고, 가장 상단의 한 행만 출력하기
doc4 = doc4.sort_values(by='customer_id', ascending=False)
print("가장 레코드(행)의 수가 많은 customer_city : ", doc4.head(1), '\n')

# 13. doc 에서 customer_city 를 인덱스로 만들고, 알파벳 순으로 인덱스를 정렬해보세요
doc = doc.set_index('customer_city').sort_index()
print("customer_city 를 인덱스로 : ", doc, '\n')


# 14. doc2에서 customer_state 기준으로 행의 갯수를 확인해보세요
#   - doc2에 value_counts() 를 써보세요 (value_counts() 는 Series 에만 적용 가능합니다.)
print("행의 갯수 : ", doc2['customer_state'].value_counts().shape, '\n')

# 15. doc2에서 customer_state 갯수를 확인해보세요
#  위와 동일

# 16. doc4에서 customer_city 갯수가 1000개 이상인 customer_city 갯수만 확인해보세요
#   202402 추가사항: 이상은 >= 이고, 초과는 > 입니다. 영상에서 > 으로 이상을 설명하는 실수가 있을 수 있어서 명시적으로 기재합니다.
doc4 = doc.groupby('customer_city').count()


# 17. doc4에서 customer_city 갯수가 1000개 이상인 customer_city 이름을 확인해보세요
# 202402 추가사항: 이상은 >= 이고, 초과는 > 입니다. 영상에서 > 으로 이상을 설명하는 실수가 있을 수 있어서 명시적으로 기재합니다.
doc5 = doc4[doc4['customer_id'] >= 1000]
print("customer_city 갯수가 1000개 이상 : ", doc5.index, '\n')

# 18. doc에서 결측치가 각 컬럼에 있는지 확인해보세요
print('결측치 : ', doc.isnull().sum(), '\n')

# 추가 문법 이해 (to_list())¶
# 19. doc에서 중복된 customer_city 를 가진 행을 삭제한 후, customer_city 이름만 가져와보세요
doc = pd.read_csv("../data/00_data/olist_customers_dataset.csv", encoding='utf-8-sig')
remove_dupl = doc.drop_duplicates(subset='customer_city', keep='last')['customer_city'].tolist()
print(remove_dupl)

# 추가 문법 이해 (pivot_table)

# 20. doc_covid 에서 중복된 Country_Region 각각에 대해 Confirmed 를 모두 더한 값을 컬럼으로 갖는 데이터프레임을 피봇테이블로 만드세요
#   - 결측치는 0으로 만드세요

# 21. doc_covid 에서 중복된 Country_Region 각각에 대해 Confirmed 를 모두 더한 값을 컬럼으로 갖는 데이터프레임을 피봇테이블로 만들고, 총 값을 'Total' 을 인덱스 값으로 하는 record 로 추가하세요
#   - 결측치는 0으로 만드세요
