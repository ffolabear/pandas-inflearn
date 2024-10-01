import chart_studio.plotly as py
import plotly.express as px
from plotly import graph_objects as go
import cufflinks as cf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cf.go_offline(connected=True)


# 두개의 쌍으로 된 숫자 5개 생성 = 행렬
print(np.random.rand(5, 2), '\n')

# 데이터프레임 생성
df = pd.DataFrame(np.random.rand(10, 2), columns=['A', 'B'])
print(df.head(), '\n')

# 데이터프레임으로 그래프 그리기

# 도움말 얻기
# print(cf.help('bar'))

# 바 그래프 그리기
# df.plot(kind='bar')
# plt.show()
fig = px.line(df, x='A', y='B')
fig.
fig.show()

# bar 그래프 테스트
