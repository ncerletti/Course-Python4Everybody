# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
num2 = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(':')
    num = line[pos+2 :]
    count = count + 1 
    num1= float(num)
    num3= num1 + num2
    num2 = float(num3)
average = num2 / count
print('Average spam confidence:', average)
