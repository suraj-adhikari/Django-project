def triangle(a):
    b=a-1
    for i in range (a):
        for j in range(b):
            print(end = " ")
        b=b-1
        for j in range(0, i+1):
            print(" * ",end = "")
        print("\r")
n = 7
triangle(n)