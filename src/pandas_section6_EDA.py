import pandas as pd

# EDA - 탐색적 데이터 분석 과정
'''
탐색적 데이터 분석: 1. 데이터의 출처와 주제에 대해 이해

1. 데이터의 출처와 주제에 대해 이해
2. 데이터의 크기 확인
3. 데이터 구성 요소(feature)의 속성(특징) 확인
    - feature: 데이터 구성 요소를 의미함
    - 예: 어떤 초등학교에 학생 성적을 기록한 데이터가 있다면, 학생 이름, 과목별 성적등을 feature로 볼 수 있음
        (가볍게 field/column 이라고 봐도 무방함)
'''

# 탐색적 데이터 분석: 2. 데이터의 크기 확인

# pandas 로 csv 읽기
doc = pd.read_csv("../data/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/04-01-2020.csv",
                  encoding='utf-8-sig')
# 에러가 나는 데이터는 error_bad_lines=False 옵션으로 무시
print(doc, '\n')

# 데이터를 pandas로 읽은 후, 가장 먼저 하는 일

# 데이터 일부 확인하기
print('head : ', doc.head(n=10), '\n')
print('tail : ',doc.tail(n=10), '\n')    # 많이 사용하진 않음

# 데이터의 row, column 사이즈 확인
print("shape : ", doc.shape, '\n')

# 상세정보
print("상세정보 : ", doc.info(), '\n')

# --------------------------------------------------------------------

# 탐색적 데이터 분석: 3. 데이터 구성 요소(feature)의 속성(특징) 확인

print("columns : ", doc.columns, '\n')

# 상관관계 계산
'''
+1에 가까우면, 양의 선형 상관 관계 (1에 가까울 수록 선에 가까운 데이터가 많고, 한 변수값이 증가하면, 다른 변수값도 증가)
0에 가까우면 상관관계가 없고
-1에 가까우면 음의 선형 상관 관계를 가진다 (-1에 가까울 수록 선에 가까운 데이터가 많고, 한 변수값이 증가하면, 다른 변수값은 감소) 라고 해석됨
'''
print(doc.corr(numeric_only=True))


