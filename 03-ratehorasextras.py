hrs = input("Enter Hours: ")
h = float(hrs)
rate = input ("Enter rate per hour: ")
r = float (rate)

if h <= 40:
    print(str(h*r))
else:
    he=float(h-40)
    normrate= 40*r
    exrate= he*(1.5*r)
    totrate= float(normrate+exrate)
    print(str(totrate))
