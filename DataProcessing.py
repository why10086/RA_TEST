import json
import csv

#读取csv文件
filename = './question_1/q1_uncomplete.csv'
with open(filename, "r") as f:
	reader = csv.DictReader(f)
	for row in reader:
		print(row)




