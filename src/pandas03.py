# 파일 읽기 (xml)
from bs4 import BeautifulSoup

data_file = open('../data/users.xml', 'r', encoding='utf-8-sig')
soup = BeautifulSoup(data_file, 'xml')
users = soup.select('user')
for user in users:
    print(user.text)
