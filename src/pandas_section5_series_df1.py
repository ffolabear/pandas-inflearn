import pandas as pd

# series 생성
series_data = pd.Series([70, 60, 90])
print(series_data)

# 인덱스 읽기
print(series_data.index)

# 값 읽기
print(series_data.values)

# 특정 인덱스 값 읽기
print(series_data[0])
print(series_data.iloc[0])  # pandas 에서 추천하는 방식

print()

# 데이터 삭제하기
del series_data[0]
print(series_data)

# 데이터 타입
'''
    - dtype 으로 불리며, 주요 데이터 타입은 다음과 같음
    - object 는 파이썬의 str 또는 혼용 데이터 타입 (문자열)
    - int64 는 파이썬의 int (정수)
    - float64 는 파이썬의 float (부동소숫점)
    - bool 는 파이썬의 bool (True 또는 False 값을 가지는 boolean)
    - 이외에 datetime64 (날짜/시간), timedelta[ns] (두 datatime64 간의 차) 도 활용됨
'''
series_data_object = pd.Series(['dave', 'alex', 'amir'])
print(series_data_object, '\n')

# ------------------------------------------------------------------

# dataframe 생성

df = pd.DataFrame({
    "미국": [2.1, 2.2, 2.3],
    "한국": [0.4, 0.5, 0.45],
    "중국": [10, 13, 15]}
)

print(df, '\n')

# 인덱스와 함께 생성

df_with_index = pd.DataFrame({
    "미국": [2.1, 2.2, 2.3],
    "한국": [0.4, 0.5, 0.45],
    "중국": [10, 13, 15]},
    index=[2000, 2010, 2020]
)

print(df_with_index, '\n')

# 인덱스 출력
print(df_with_index.index, '\n')

# 인덱스 변경
df_with_index.index = [2001, 2002, 2003]
print(df_with_index, '\n')

# 컬럼 출력
print(df_with_index.columns, '\n')

# 값 출력
print(df_with_index.values, '\n')

# 특정 컬럼 선택하기
df_without_index = pd.DataFrame({
    "년도": [2000, 2010, 2020],
    "미국": [2.1, 2.2, 2.3],
    "한국": [0.4, 0.5, 0.45],
    "중국": [10, 13, 15]
})


df_without_index = df_without_index.set_index('년도')
print(df_without_index, '\n')
print(df_without_index.index.name, '\n')


# 컬럼명 변경
df_without_index.index.name = '연도'
print(df_without_index, '\n')


# 인덱스로 지정한 컬럼 재설정
df_without_index = df_without_index.reset_index('연도')
print(df_without_index, '\n')
df_without_index = df_without_index.set_index('연도')


# 데이터프레임 데이터 접근하기
# iloc : index 를 통해서 값을 찾음
# loc : 인덱스 번호를 통해서 값을 찾음(0부터 시작)

# 특정 행 가져오기
print(df_without_index.loc[2000])
print(type(df_without_index.loc[2000]), '\n')


# 특정 열 가져오기
print(df_without_index['미국'])
print(type(df_without_index['미국']), '\n')


# 특정 열의 특정 셀 데이터 가져오기
print(df_without_index.loc[2000]['미국'])
print(df_without_index)
print(df_without_index.index, '\n')



# 인덱스를 문자열로 지정했을떄 인덱스가 object 타입이므로 접근도 문자열로 해줘야함
df_index_test = pd.DataFrame({
    "년도": ['2000', '2010', '2020'],
    "미국": [2.1, 2.2, 2.3],
    "한국": [0.4, 0.5, 0.45],
    "중국": [10, 13, 15]
})
df_index_test = df_index_test.set_index("년도")
print(df_index_test.index)
print(df_index_test.loc['2000']['미국'])