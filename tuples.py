name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

date= list()
counts = dict()
hour= list()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        hour.append(words[5])

for num in hour:
   date.append(num[0:2])
        
for hours in date:
    counts[hours] = counts.get(hours,0) + 1

tmp = list()
for k,v in counts.items():
    tmp.append((k,v))
    
tmp = sorted(tmp)
for k,v in tmp:
    print(k,v)
