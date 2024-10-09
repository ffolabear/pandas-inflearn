# 테이블 데이터와 시계열 데이터
# 테이블 데이터: 엑셀과 같이 행과 열로 나타낸 데이터
# 시계열 데이터: 일정 시간 간격으로 배치된 데이터
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 시계열 데이터 시각화를 위한 사전 준비

# 하루 단위로 인덱스 생성
# 등분 : period 옵션
# 간격 : freq 옵션
# pd.date_range(start='2020-01-01', end='2020-12-31')
# pd.date_range(start='2020-01-01', end='2020-12-31', periods=3)
# pd.date_range(start='2020-01-01', end='2020-12-31', freq='3M')


date_index = pd.date_range('2020-05-01', periods=15)  # DatetimeIndex 객체
df = pd.DataFrame(data=range(len(date_index)), columns=['count'], index=date_index)
# print(df)

# 주로 사용되는 그래프 타입은 라인 그래프, 막대 그래프

# 상관관계를 확인하기 위해 주로 사용되는 그래프 타입
#   - heatmap 그래프
#   - 산점도(scatter) 그래프
doc = pd.read_csv("../data/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/04-01-2020.csv",
                  encoding='utf-8-sig')

# 데이터의 상관관계 파악
# print(doc.corr(numeric_only=True))

# 색상(colorscale) 변경
# https://plotly.com/python/reference/#heatmap-colorscale

# Heatmap 그래프
doc2 = doc.corr(numeric_only=True)
fig = go.Figure()
fig.add_trace(go.Heatmap(
    x=doc2.index,
    y=doc2.columns,
    z=doc2,
    colorscale='Reds',
))
# fig.show()

# Scatter 산점도 그래프
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=doc["Recovered"],
    y=doc["Confirmed"],
    mode='markers'
))
fig.show()

