import json
import csv

data = []
#读取csv文件
filename = 'q1_uncomplete.csv'
with open(filename, "r") as f:
	reader = csv.DictReader(f)
	for row in reader:
		data.append(row)
f.close()
for row in data:
  jsonname = row['txn_hash'] + '.json'
  f = open(jsonname, encoding='utf-8')
  reader = json.load(f)

  logs = reader['logs']
  for log in logs:
    if log['data'] == '0x':
      address = log['address']
      token_id = int(log['topics'][-1], 16)
    else:
      price_value = int(log['data'][-20:], 16)
    print(address, token_id, price_value)








