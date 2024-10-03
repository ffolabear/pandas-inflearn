import plotly.graph_objects as go


# 테스트

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[1, 2, 3],
))
fig.show()

# 패턴 코드로 라인 그래프 그리기

# 1. fig = go.Figure() 로 기본 객체를 만들고
# 2. fig.add_trace() 에 그래프 객체(예: go.Scatter()) 를 추가 (여러 데이터의 경우, add_trace 여러번 호출)
# 3. fig.update_layout() 으로 레이아웃 변경
#   fig.update_annotation() 으로 annotation 필요시 업데이트
#   데이터는 사전 형태로 넣는 것이 가장 쉬움
#       각 필드 확인: https://plotly.com/python/reference/
# fig.show() 로 그래프를 보여줌

