import chart_studio.plotly as py
import cufflinks as cf
import numpy as np
import pandas as pd

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
df.iplot(kind='bar', colors=['rgba(255, 153, 51, 1.0)', 'rgba(0, 204, 204, 1.0)'])
print()