name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        emails = words[1]
        for email in emails:
            counts[email] = counts.get(email,0) + 1

prosender = None
mostsent = None
for sender, count in counts.items():
    if mostsent is None or count > mostsent:
        count = mostsent
        prosender = email

print(prosender, mostsent)