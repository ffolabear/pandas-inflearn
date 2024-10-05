import numpy as np
import pandas as pd
import plotly.graph_objects as go

# 테스트

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[1, 2, 3],
))
# fig.show()

# 라인 그래프 테스트
df = pd.DataFrame(np.random.rand(10, 2), columns=['A', 'B'])
print(df)

# 패턴 코드로 라인 그래프 그리기

# 1. fig = go.Figure() 로 기본 객체를 만들고
# 2. fig.add_trace() 에 그래프 객체(예: go.Scatter()) 를 추가 (여러 데이터의 경우, add_trace 여러번 호출)
# 3. fig.update_layout() 으로 레이아웃 변경
#   fig.update_annotation() 으로 annotation 필요시 업데이트
#   데이터는 사전 형태로 넣는 것이 가장 쉬움
#       각 필드 확인: https://plotly.com/python/reference/
# fig.show() 로 그래프를 보여줌

fig = go.Figure()
fig.add_trace(  # 그래프가 그려진 상태
    go.Scatter(
        x=df.index, y=df['A']
    )
)

# 옵션은 딕셔너리로 넣는게 가장 쉬움
fig.update_layout(
    {
        "title": {
            "text": "Graph with go.Scatter",
            "font": {
                "size": 15
            }
        },
        "showlegend": True,
        "xaxis": {
            "title": "random number"
        },
        "yaxis": {
            "title": "A"
        }
    }
)

# 복합 라인그래프

# 라인 추가
fig.add_trace(
    go.Scatter(
        # 가장 많이 쓰이는 옵션
        x=df.index, y=df['B'], mode='lines+markers+text', name='B', text=df.index, textposition='top center'
    )
)

# fig.show()

# 바그래프 그리기

fig2 = go.Figure()
fig2.add_trace(go.Scatter())

# textposition='auto' 는 그래프 안에 값 넣는 옵션

fig2.add_trace(
    go.Bar(
        x=df.index, y=df['A'], name='A', text=df['A'], textposition='auto', texttemplate='%{y:.2f}'
    )
)
fig2.add_trace(
    go.Bar(
        x=df.index, y=df['B'], name='B', text=df['B'], textposition='auto', texttemplate='%{y:.2f}'
    )
)
fig2.update_layout(
    {
        "title": {
            "text": "Graph with <b>go.Bar</b>",
            "x": 0.5,
            "y": 0.9,
            "font": {
                "size": 20
            }
        },
        "showlegend": True,
        "xaxis": {
            "title": "random number",
            "showticklabels": True,
            "dtick": 1

        },
        "yaxis": {
            "title": "A"
        },
        "autosize": False,
        "width": 800,
        "height": 340
    }
)
fig2.show()
