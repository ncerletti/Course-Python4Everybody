fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    x = line.split()
    for word in x:
        if word not in lst:
            lst.append(word)
lst.sort() 
print(lst)
