import numpy as np
import pandas as pd
import plotly.graph_objects as go

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6],
    'C': [1, 2, 3, 4, 5, 100]
})

# describe 함수로 평균, 표준편차 등등 확인가능
# 50% 는 중간값 의미
# 원소의 갯수가 짝수일 경우 가운데 두개를 더하고 2로 나눈 값이 중간값
print(df.describe())

# 데이터의 종류

# 1. 수치형 데이터
#   - 연속형 데이터 : 특정한 범위 안에 어떤 값(정수와 부동소숫점)이든 가질 수 있는 데이터
#   - 이산 데이터 : 횟수와 같은 정수만 가질 수 있는 데이터

# 2. 범주형 데이터
#   - 명목형 데이터 : 카테고리, 타입, 항목등 데이터 분류를 위해 이미 정해진 값이 있는 데이터, 데이터가 가질 수 있는 값을 수준이라고 부름
#       - 이진 데이터: True or False, 0 or 1 과 같이 이미 정해진 두 값만 있는 데이터
#   - 순서형 데이터: 이미 정해진 값 사이의 순서 관계가 있는 데이터

# 수치형 데이터는 5가지 수치를 확인
# - 최소값, 제1사분위수(25%), 중간값=제2사분위수, 제3사분위수(75%), 최대값 확인

# boxplot 이 이것들을 판단하기 좋음
fig = go.Figure()
fig.add_trace(
    go.Box(y=df['A'], name='A'),
)
fig.add_trace(
    go.Box(y=df['C'], name='C'),
)

# fig.show()

# 수치형 데이터 분포 확인을 위한 히스토그램
df1 = pd.DataFrame(np.random.rand(100000, 1), columns=['A'])
df.head()

fig2 = go.Figure()
fig2.add_trace(
    go.Histogram(
        x=df1['A'], name='A',
        xbins=dict(  # bins used for histogram
            start=0,
            end=1.0,
            size=0.05       # 자르는 단위
        ),
        marker_color='#F50057'
    )
)

fig2.update_layout(
    title_text='Sampled Results',  # title of plot
    xaxis_title_text='Value',  # xaxis label
    yaxis_title_text='Count',  # yaxis label
    bargap=0.1,  # gap between bars of adjacent location coordinates

)
fig2.show()
