n = 2
def hanoi(n, a, b, c):
    if n !=0:
        hanoi(n-1, a,c,b)
        print(a,"-",c)
        hanoi(n-1,b,a,c)

hanoi(n,"1","2","3")