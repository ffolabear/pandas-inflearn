# 연습문제와 추가 문법으로 정리하는 pandas
import pandas as pd

# 1. 00_data/olist_customers_dataset.csv 파일 pandas dataframe 으로 읽어오기 (데이터프레임 변수 이름은 doc 로 하기로 함)
doc = pd.read_csv("../data/00_data/olist_customers_dataset.csv",encoding='utf-8-sig')
print(doc, '\n')

# 2. 처음 5개 열 확인하기
print(doc.head(5), '\n')

# 3. 전체 record 수(행 수) 확인하기
print(doc.info(), '\n')

# 4. 전체 열의 수 확인하기


# 5. 열의 이름 리스트로 가져오기
print(doc.columns, '\n')

# 6. 인덱스 확인하기
print(doc.index, '\n')

# 7. 다섯 숫자 요약(5 number summary) 확인하기


# 추가 문법 pandas.DataFrame.copy

# 8. customer_zip_code_prefix, customer_city, customer_state 컬럼만 가져오기 (데이터프레임 변수 이름은 doc2로 하기로 함)

# 9. customer_city 가 sao paulo 인 레코드(행)만 가져오기 (데이터프레임 변수 이름은 doc3 으로 하기로 함)
#   - 레코드(행) 수 확인도 해보기

# 10. customer_city 기준으로 행의 갯수를 확인해보세요
#   - doc2에 value_counts() 를 써보세요 (value_counts() 는 Series 에만 적용 가능합니다.)

# 11. doc 데이터프레임에서 customer_city 기준으로 행의 갯수를 확인해보세요
#   1. groupby 를 써서 customer_city 를 기준으로 행의 갯수를 count 하세요 (새로운 데이터프레임 변수 이름은 doc4로 하기로 함)
#   2. doc4를 통해 customer_city 수도 확인해보세요 (데이터프레임 레코드(행) 수를 확인해보면 됩니다.)

# 추가 문법 이해 (정렬, sort_values(), sort_index())

# 12. doc4에서 가장 레코드(행)의 수가 많은 customer_city 를 확인해보세요
#   1. doc4의 customer_id 를 기준으로 정렬하고, 가장 상단의 한 행만 출력하기

# 13. doc 에서 customer_city 를 인덱스로 만들고, 알파벳 순으로 인덱스를 정렬해보세요

# 14. doc2에서 customer_state 기준으로 행의 갯수를 확인해보세요
#   - doc2에 value_counts() 를 써보세요 (value_counts() 는 Series 에만 적용 가능합니다.)

# 15. doc2에서 customer_state 갯수를 확인해보세요

# 16. doc4에서 customer_city 갯수가 1000개 이상인 customer_city 갯수만 확인해보세요
#   202402 추가사항: 이상은 >= 이고, 초과는 > 입니다. 영상에서 > 으로 이상을 설명하는 실수가 있을 수 있어서 명시적으로 기재합니다.

# 17. doc4에서 customer_city 갯수가 1000개 이상인 customer_city 이름을 확인해보세요
# 202402 추가사항: 이상은 >= 이고, 초과는 > 입니다. 영상에서 > 으로 이상을 설명하는 실수가 있을 수 있어서 명시적으로 기재합니다.

# 18. doc에서 결측치가 각 컬럼에 있는지 확인해보세요

# 추가 문법 이해 (to_list())¶
# 19. doc에서 중복된 customer_city 를 가진 행을 삭제한 후, customer_city 이름만 가져와보세요


# 추가 문법 이해 (pivot_table)

# 20. doc_covid 에서 중복된 Country_Region 각각에 대해 Confirmed 를 모두 더한 값을 컬럼으로 갖는 데이터프레임을 피봇테이블로 만드세요
#   - 결측치는 0으로 만드세요

# 21. doc_covid 에서 중복된 Country_Region 각각에 대해 Confirmed 를 모두 더한 값을 컬럼으로 갖는 데이터프레임을 피봇테이블로 만들고, 총 값을 'Total' 을 인덱스 값으로 하는 record 로 추가하세요
#   - 결측치는 0으로 만드세요