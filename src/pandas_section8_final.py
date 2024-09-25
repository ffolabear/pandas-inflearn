import json
import os
from datetime import datetime

import pandas as pd

'''
1. csv 파일 읽기
2. 'Country_Region', 'Confirmed' 두 개의 컬럼만 가져오기
3. 'Confirmed' 에 데이터가 없는 행 삭제하기
4. 'Country_Region'의 국가명을 여러 파일에 일관되게 변경하기
5. 'Confirmed' 데이터 타입을 int64(정수) 로 변경
6. 'Country_Region' 를 기준으로 중복된 데이터를 합치기
7. 파일명을 기반으로 날짜 문자열 변환하고, 'Confirmed' 컬럼명 변경하기
'''

PATH = "../data/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"

with open('../data/COVID-19-master/csse_covid_19_data/country_convert.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)


def convert_country(row):
    if row['Country_Region'] in json_data:
        return json_data[row['Country_Region']]
    return row['Country_Region']


def create_dataframe(filename):
    doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')  # 1. csv 파일 읽기
    try:
        doc = doc[['Country_Region', 'Confirmed']]
    except:
        doc = doc[['Country/Region', 'Confirmed']]
        doc.columns = ['Country_Region', 'Confirmed']  # 2. 'Country_Region', 'Confirmed' 두 개의 컬럼만 가져오기

    doc = doc.dropna(subset=['Confirmed'])  # 3. 'Confirmed' 에 데이터가 없는 행 삭제하기
    doc['Country_Region'] = doc.apply(convert_country, axis=1)  # 4. 'Country_Region'의 국가명을 여러 파일에 일관되게 변경하기
    doc = doc.astype({'Confirmed': 'int64'})  # 5. 'Confirmed' 데이터 타입을 int64(정수) 로 변경
    doc = doc.groupby('Country_Region').sum()  # 6. 'Country_Region' 를 기준으로 중복된 데이터를 합치기

    # 7. 파일명을 기반으로 날짜 문자열 변환하고, 'Confirmed' 컬럼명 변경하기
    date_column = filename.split(".")[0].lstrip('0').replace('-', '/')
    doc.columns = [date_column]
    return doc


def generate_dateframe_by_path(PATH):
    # 관련 csv 파일 이름들 배열에 넣기
    file_list, csv_list = os.listdir(PATH), list()
    first_doc = True

    for file in file_list:
        # 파일 이름이 csv 로 끝나는 파일만 추가
        if file.split('.')[-1] == 'csv':
            csv_list.append(file)

    # 정렬
    csv_list.sort(key=lambda x: datetime.strptime(x, '%m-%d-%Y.csv'))

    # 병합
    for file in csv_list:
        doc = create_dataframe(file)
        if first_doc:
            final_doc, first_doc = doc, False
        else:
            final_doc = pd.merge(final_doc, doc, how='outer', left_index=True, right_index=True)
    final_doc = final_doc.fillna(0)
    return final_doc


def create_flag_link(row):
    flag_link = 'https://public.flourish.studio/country-flags/svg/' + row.lower() + '.svg'
    return flag_link


def convert_country_to_flag():
    df_confirmed = generate_dateframe_by_path(PATH)
    df_confirmed = df_confirmed.astype('int64')

    # 디폴트로 NA 값은 값이 없다는 뜻으로 해석하기 때문에 na_values 옵션으로 해당 기능 제거
    country_info = pd.read_csv("../data/COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv",
                               encoding='utf-8-sig',
                               keep_default_na=False,
                               na_values='')

    country_info = country_info[['iso2', 'Country_Region']]
    country_info = country_info.drop_duplicates(subset='Country_Region', keep='last')

    print("df_confirmed : ", df_confirmed, '\n')
    print("country_info : ", country_info, '\n')


if __name__ == '__main__':
    convert_country_to_flag()
