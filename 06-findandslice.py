text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
num = pos + 4
#print(num)
a_num = text[num + 1 :]
i_num= float(a_num)
print(i_num)