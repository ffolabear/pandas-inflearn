import pandas as pd

PATH = '../data/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/'

# Series 로 feature를 보다 상세하게 탐색하기
doc = pd.read_csv(PATH + "04-01-2020.csv", encoding='utf-8-sig')

# head 출력해보기
print(doc.head(), '\n')

# 데이터프레임에서 Series 추출하기
countries = doc['Country_Region']
print(countries, '\n')

# 사이즈 반환
print(doc.size, '\n')

# 데이터가 없는 경우를 뺸 사이즈 반환
print(countries.count(), '\n')

# 중복 제거
print(countries.unique(), '\n', len(countries.unique()), '\n')

# 필요한 컬럼들만 선택하기
column_select = doc[['Confirmed', 'Deaths', 'Recovered']]
print(column_select, '\n')

# 특정 조건에 맞는 row 검색하기
doc_us = doc['Country_Region'] == "US"
print(doc_us, '\n')

# 없는 데이터 처리하기
# 없는 데이터 - 결측치 확인하기
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')
print(doc.isnull().sum(), '\n')

# 없는 데이터 처리하기 - 결측치
# 결측치를 가진 행을 모두 삭제
# 강의에는 데이터가 있는 행만 출력되나 현재는 없는 행도 함께 출력
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')
doc = doc.dropna()
print(doc.head(), '\n')

# 특정 컬럼만 결측치가 있을 경우 삭제
doc = doc.dropna(subset=['Confirmed'])
print(doc.head(), '\n')

# 특정 데이터를 일괄 변경하기
# 결측치 = null
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')
doc = doc.fillna(-22)
print(doc, '\n')

# 특정 컬럼에 대해 특정 값으로 변경
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')
nan_date = {'Deaths': -123, 'Recovered': -456}
doc = doc.fillna(nan_date)
print(doc, '\n')

# ---------------------------------------------------------------

# 특정 키값을 기준으로 데이터 합치기
doc = pd.read_csv(PATH + "04-01-2020.csv", encoding='utf-8-sig')
print(doc, '\n')

# groupby 하면 인덱스가 변경됨
doc = doc.groupby('Country_Region').sum()
print(doc, '\n')
print('column : ', doc.columns, '\n')
print('index : ', doc.index, '\n')

# 특정 Dataframe 만 보고싶을때
doc = doc[doc.index == 'US']
print("us doc : ", doc, '\n')

# 컬럼 타입 변경하기
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')
doc = doc[['Country/Region', 'Confirmed']]  # 가져올 컬럼 리스트
doc = doc.dropna(subset=['Confirmed'])  # 없는 데이터는 삭제
doc = doc.astype({'Confirmed': 'int64'})
print(doc.info(), '\n')
print(doc)

# 데이터프레임 컬럼명 변경하기
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')
doc = doc[['Country/Region', 'Confirmed']]  # 가져올 컬럼 리스트

print("before : ", doc.columns, '\n')
doc.columns = ['Country_Region', 'Confirmed']
print("after : ", doc.columns, '\n')

# 데이터프레임 중복 행 확인/제거하기
doc = pd.read_csv("../data/COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv", encoding='utf-8-sig')
doc = doc[['iso2', 'Country_Region']]
print(doc, '\n')

# 중복 여부를 True / False 로 알려줌
print(doc.duplicated(), '\n')
print(doc[doc.duplicated()], '\n')              # 중복된 것만들 출력하기


# 중복 제거
# keep 은 중복 된것을 삭제하고 중복된 것중 첫번째 혹은 마지막중 어떤것을 삭제할지 정하는 것
doc = doc.drop_duplicates(subset=['Country_Region'], keep='last')
print(doc, '\n')