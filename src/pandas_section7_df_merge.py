import pandas as pd

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "customer_id": [1, 2, 3],
    "customer_name": ["Robert", "Peter", "Dave"]}
    ,columns=["id", "customer_id", "customer_name"]
)

df2 = pd.DataFrame({
    "id": [1, 2, 4],
    "order_id": [100, 200, 300],
    "order_date": ['2021-01-21', '2021-02-03', '2021-10-01']},
    columns=["id", "order_id", "order_date"]
)

print(df1, '\n')
print(df2, '\n')

# 데이터 프레임 합치기 : concat
# 디폴트가 위 아래로 붙이는 것
print(pd.concat([df1, df2]), '\n')
print(pd.concat([df1, df2], axis=1), '\n')          # 오른쪽에 붙히기


# 데이터 프레임 합치기 (병합하기) : merge
'''
merge(데이터프레임1, 데이터프레임2, how=결합방법)

결합방법
 - inner : 내부 조인 - SQL의 INNER JOIN 과 동일 - 디폴트
 - outer : 완전 외부 조인 - SQL의 OUTER JOIN 과 동일
 - left : 왼쪽 우선 외부 조인 - SQL의 LEFT OUTER JOIN 과 동일
 - right : 오른쪽 우선 외부 조인 - SQL의 RIGHT OUTER JOIN 과 동일
'''
# 조인 방식은 how 옵션이 줄 명시할 수 있음

#  inner : 내부 조인 - SQL의 INNER JOIN 과 동일 (디폴트)
print("inner join : ", pd.merge(df1, df2), '\n')             # 다른것은 제거하고 공통인 것만 병합
print(pd.merge(df1, df2, on='id'), '\n')    # 기준 컬럼을 명시할 수 있음

# outer : 완전 외부 조인 - SQL의 OUTER JOIN 과 동
# 모든 데이터를 다 가져오는
print("outer join : ", pd.merge(df1, df2, how="outer"), '\n')

# left : 왼쪽 우선 외부 조인 - SQL의 LEFT OUTER JOIN 과 동일
# 왼쪽에 있는것을 무조건 자겨오고 매칭 되어있는 것에 추가하는 방식

# right : 오른쪽 우선 외부 조인 - SQL의 RIGHT OUTER JOIN 과 동일
# left 의 반대
print("left join : ", pd.merge(df1, df2, how="left"), '\n')
print("right join : ", pd.merge(df1, df2, how="right"), '\n')

# 인덱스를 기준으로 병합
df1 = df1.set_index('id')
df2 = df2.set_index('id')
print(df1.index)
print(df2.index, '\n')

print(pd.merge(df1, df2, left_index=True, right_index=True), '\n')
print(pd.merge(df1, df2, left_index=True, right_index=True, how="outer"), '\n')
