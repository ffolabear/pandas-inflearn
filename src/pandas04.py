# JSON 다루기
import json

data = '{ "id":"01", "language": "Java", "edition": "third", "author": "Herbert Schildt" }'

# json 포맷 데이터를 dict 로 변환
dict_data = json.loads(data)
print(dict_data)
print(type(dict_data))

print()

# json 포맷 데이터를 문자열로 변환
str_date = json.dumps(dict_data, indent=2)
print(str_date)
print(type(str_date))


# json 데이터를 파일로 저장
with open('../data/text_to_json.json', 'w', encoding='utf-8-sig') as json_file:
    json_string = json.dump(dict_data, json_file, indent=2)


# json 피일을 읽기
with open('../data/US_category_id.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)
    print("keys : ", json_data.keys())
    for data in json_data['items']:
        print(data['kind'], data['snippet']['title'])
