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
df.columns = ['Column 1', 'Column 2']
print(df.head(), '\n')

# 데이터프레임으로 그래프 그리기

# 도움말 얻기
# print(cf.help('bar'))

# 바 그래프 그리기
# fig = px.bar(df, x='A', y='B')
# fig.show()
# df.plot(kind='bar')
# plt.show()


# 누적 그래프 생성
# df.plot(kind='bar', stacked=True)
# plt.show()

# 가로 바 그래프 생성
# df.plot(kind='barh', stacked=True)
# plt.show()

# 라인 그래프 그리기
df.plot(kind='scatter', x='Column 1', y='Column 2', fill=True)
plt.plot(df['Column 1'], color='green')
plt.plot(df['Column 2'], color='blue')
plt.show()
