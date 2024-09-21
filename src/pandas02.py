import csv

# 파일 읽기 (csv)

data_file = open('../data/USvideos.csv', 'r', encoding='utf-8-sig')

data_lines = csv.reader(data_file, delimiter=',')
for data_line in data_lines:
    print(data_line)
data_file.close()

# -------------------------------------------------------

# 파일 쓰기 (csv)
# window 에서 자동 공백 추가 문제를 해결하기 위해 newline 옵션줘야함
data_file_write = open('../data/csv_data_write.csv', 'w', encoding='utf-8-sig', newline='')
data_write = csv.writer(data_file_write, delimiter=',')
data_write.writerow(['1', '2', '3'])
data_file_write.close()

# with 구문 사용
with open('../data/csv_data_write.csv', 'w', encoding='utf-8-sig', newline='') as writer_csv:
    writer = csv.writer(writer_csv, delimiter=',')
    writer.writerow(['love'] * 3 + ['banana'])
    writer.writerow(['apple', 2])
    writer.writerow(['apple', 'Lovely spam', 'Wonderful spam'])

# csv 파일 쓰기 - 딕셔너리로
with open('../data/csv_data_write_dict.csv', 'w', encoding='utf-8-sig', newline='') as writer_csv:
    field_name = ['First Name', 'Last Name']  # 플드명 정의
    writer = csv.DictWriter(writer_csv, fieldnames=field_name)
    writer.writeheader()
    writer.writerow({'First Name': 'Dave', 'Last Name': 'Lee'})
    writer.writerow({'First Name': 'Tony', 'Last Name': 'Stark'})
    writer.writerow({'First Name': 'Steve', 'Last Name': 'Rogers'})
