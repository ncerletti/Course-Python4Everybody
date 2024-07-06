
score = input("Enter Score: ")

try:
    gscore=float(score)
except:
    print("Enter a valid number")
    quit()

if 1.0 >= gscore >= 0.0:
    if gscore >= 0.9:
        print("A")
    elif gscore >= 0.8:
        print("B")
    elif gscore >= 0.7: 
        print("C")
    elif gscore >= 0.6:
        print("D")
    elif gscore < 0.6:
        print("F")
else:
    print("Enter a number between 0.0 and 1.0")
    quit()