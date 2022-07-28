import json
import csv

#储存数据的字典
data = []

#读取csv文件，获取数据
filename = 'q1_uncomplete.csv'
with open(filename, "r") as f:
	reader = csv.DictReader(f)
	for row in reader:
    #储存到data字典中
		data.append(row)
f.close()

#处理补全数据
for row in data:
  jsonname = row['txn_hash'] + '.json'
  #读取json文件
  f = open(jsonname, encoding='utf-8')
  reader = json.load(f)
  logs = reader['logs']
  for log in logs:
    #解析log日志获得所需数据
    price_value = 0
    if log['data'] == '0x':
      address = log['address']
      token_id = int(log['topics'][-1], 16)
    else:
      to = '0x' + log['topics'][2][-40:]
      price_value += int(log['data'][-20:], 16) / pow(10, 18)
  f.close()
  #判断是否缺少数据，进行补充
  if row['address'] == '':
    row['address'] = address
  if row['token_id'] == '':
    row['token_id'] = token_id
  if row['to_'] == '':
    row['to_'] = to
  if row['price_value'] == '':
    row['price_value'] = price_value
  #currency解析方法为判断合约地址，并根据地址找到相对应的代币，由于网络问题无法完成，望谅解
  if row['price_currency'] == '':
    row['price_currency'] = 'ETH'
 
#将数据写入csv文件
filename = 'q1_uncomplete_Wang_Hongyu.csv'
header = ['', 'txn_hash', 'address', 'to_', 'token_id', 'price_value', 'price_currency']
out = open(filename, "w")
writer = csv.DictWriter(out,fieldnames=header) # 提前预览列名，当下面代码写入数据时，会将其一一对应。
writer.writeheader()  # 写入列名
writer.writerows(data) # 写入数据
out.close()









