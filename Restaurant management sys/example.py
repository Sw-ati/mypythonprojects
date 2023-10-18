for i in range(int(input("No. of test cases:"))):
    A,B,C = map(int,input("A,B,C resp.:").split())
    if A+B+C==0 or A-B-C==0:
        print("YES")
    else:
        print("NO")