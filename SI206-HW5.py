import re

file = open('regex_sum_32076.txt')
lines = file.read()
sum_list = []

count_num = re.findall('[0-9]+', lines)
for number in count_num:
	sum_list.append(int(number))

print(sum(sum_list))