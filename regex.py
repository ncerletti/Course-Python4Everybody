import re
hand = open('py4e-data.dr-chuck.net_regex_sum_1669038.txt')
numlist= list()
for line in hand:
    line = line.rstrip()
    stuff= re.findall('[0-9]+', line)
    for number in stuff:
        num = float(number)
        numlist.append(num)

sum = sum(numlist)
print(sum)
