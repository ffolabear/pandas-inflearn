import pandas as pd
import json

PATH = "../data/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"

doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')
try:
    doc = doc[['Province_State', 'Country_Region', 'Confirmed']]  # 1. 특정 컬럼만 선택해서 데이터프레임 만들기
except:
    doc = doc[['Province/State', 'Country/Region', 'Confirmed']]  # 1. 특정 컬럼만 선택해서 데이터프레임 만들기
    doc.columns = ['Province_State', 'Country_Region', 'Confirmed']
doc = doc.dropna(subset=['Confirmed'])  # 2. 특정 컬럼에 없는 데이터 삭제하기
doc = doc.astype({'Confirmed': 'int64'})  # 3. 특정 컬럼의 데이터 타입

with open('../data/COVID-19-master/csse_covid_19_data/country_convert.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)


def change_country(row):
    if row['Country_Region'] in json_data:
        print(f"{row['Country_Region']} ----------- {json_data[row['Country_Region']]}")
        row['Country_Region'] = json_data[row['Country_Region']]
    return row


doc = doc.apply(change_country, axis=1)
doc.head()
