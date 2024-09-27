import json
import os
from datetime import datetime

import pandas as pd

PATH = "../data/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"


def create_dataframe(filename):
    # 1. csv 파일 읽기
    doc = pd.read_csv(PATH + filename, encoding='utf-8-sig')

    # 2. 'Country_Region', 'Deaths' 두 개의 컬럼만 가져오기
    try:
        doc = doc[['Country_Region', 'Deaths']]
    except:
        doc = doc[['Country/Region', 'Deaths']]
        doc.columns = ['Country_Region', 'Deaths']

    # 3. 'Confirmed' 에 데이터가 없는 행 삭제하기
    doc = doc.dropna(subset=['Deaths'])

    # 4. 'Country_Region'의 국가명을 여러 파일에 일관되게 변경하기
    doc['Country_Region'] = doc.apply(convert_country, axis=1)

    # 5. 'Confirmed' 데이터 타입을 int64(정수) 로 변경
    doc = doc.astype({'Deaths': int})

    # 6. 'Country_Region' 를 기준으로 중복된 데이터를 합치기
    doc = doc.groupby('Country_Region').sum()

    # 7. 파일명을 기반으로 날짜 문자열 변환하고, 'Confirmed' 컬럼명 변경하기
    date_column = filename.split(".")[0].lstrip('0').replace('-', '/')
    doc.columns = [date_column]
    return doc


def convert_country(row):
    with open('../data/COVID-19-master/csse_covid_19_data/country_convert.json', 'r',
              encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)
    if row['Country_Region'] in json_data:
        return json_data[row['Country_Region']]
    return row['Country_Region']


def generate_dataframe_by_path(PATH):
    file_list = os.listdir(PATH)
    csv_list = list()
    result_doc = pd.DataFrame()

    for file in file_list:
        if file.split(".")[-1] == 'csv':
            csv_list.append(file)

    # 정렬
    csv_list.sort(key=lambda x: datetime.strptime(x, "%m-%d-%Y.csv"))

    first_doc = True
    # 병합
    for file in csv_list:
        doc = create_dataframe(file)
        if first_doc:
            final_doc, first_doc = doc, False
        else:
            final_doc = pd.merge(final_doc, doc, how='outer', left_index=True, right_index=True)

    return result_doc


def create_flag_link(row):
    flag_link = 'https://public.flourish.studio/country-flags/svg/' + row.lower() + '.svg'
    return flag_link


def convert_country_to_flag():
    pass


if __name__ == '__main__':
    df_confirmed = generate_dataframe_by_path(PATH)
    print(df_confirmed)

    # 8. 모든 컬럼을 정수로 변경
    df_confirmed = df_confirmed.astype('int64')

    # 9. 나라이름을 iso2 코드로 변경
    country_info = pd.read_csv("../data/COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv",
                               encoding='utf-8-sig',
                               keep_default_na=False,
                               na_values='')
    country_info = country_info[['iso2', 'Country_Region']]
    country_info = country_info.drop_duplicates(subset='Country_Region', keep='last')
    df_final = pd.merge(df_confirmed, country_info, how='left', on='Country_Region')
    print(country_info.columns)

    # # 나라 코드가 없는 컬럼 제거
    # df_final = df_final.dropna(subset=['iso2'])
    # df_final['iso2'] = df_final['iso2'].apply(create_flag_link)
    #
    # # 10. iso2 코드를 국기 이미지로 변경
    # cols = df_final.columns.tolist()
    #
    # cols.remove('iso2')
    # cols.insert(1, 'iso2')
    # cols[1] = 'Country_Flag'
    # df_final.columns = cols
    #
    # # csv 저장
    # df_final.to_csv("COVID-19-master/final_covid_data_for_graph.csv")