# 파일 읽기 (xml)
import requests
from bs4 import BeautifulSoup

data_file = open('../data/users.xml', 'r', encoding='utf-8-sig')
soup = BeautifulSoup(data_file, 'xml')
users = soup.select('user')
for user in users:
    print(user.select_one('name').text)
    print(user.select_one('age').text)


# 연습문제

keyword = '스마트폰'
google_related_keyword_api = 'http://suggestqueries.google.com/complete/search?output=toolbar&q=' + keyword
response = requests.get(google_related_keyword_api)       # 파일이 아니라, 데이터를 Open API 에서 가져오기 위한 함수
soup = BeautifulSoup(response.content, 'xml')             # requests.get() 의 리턴값은 객체
# 객체.content 에 가져온 데이터가 있음

datas1 = soup.select('suggestion')

for item in datas1:
    print(item['data'])
