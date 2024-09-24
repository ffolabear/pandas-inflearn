import pandas as pd

PATH = "../data/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"
doc = pd.read_csv(PATH + "04-01-2020.csv", encoding='utf-8-sig')
print(doc.head(), '\n')

# 필요한 컬럼만 가져오기
try:
    doc = doc[['Province_State', 'Country_Region', 'Confirmed']]
except:
    doc = doc[['Province/State', 'Country/Region', 'Confirmed']]
    doc.columns = ['Province_State', 'Country_Region', 'Confirmed']

doc = doc.dropna(subset=['Confirmed'])  # 특정 컬럼에 없는 데이터 삭제하기
doc = doc.astype({'Confirmed': 'int64'})  # 특정 컬럼에 없는 데이터 타입 변경하기
print(doc.head(), '\n')

# 국가에 맞는 국기 이미지 가져오기
country_info = pd.read_csv("../data/COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv",
                           encoding='utf-8-sig')
print("country_flag_info : ", country_info.head(), '\n')

print("===============================================================================================================")

# 테이블 합치기
test_df = pd.merge(doc, country_info, how='left', on='Country_Region')
# print("info : ", test_df.info(), '\n')
# print(test_df.isnull().sum(), '\n')
# print(test_df)

# null 정보 확인하기
nan_rows = test_df[test_df['iso2'].isnull()]
print(nan_rows)

# 중복된 데이터 합치기 - 국가별 확진자 구하기
# groupby 와 mean (평균) , sum(합) 사용
