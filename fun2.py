

def draw_1d(n,c):
    for loop in range (5):
        print(c*n)

def draw_2d(n,m,char1):
    for loop in range (n):
        print(m*char1)

def special_draw_2d (n,m,border,fill):
    print(border*m)
    for loop in range (n-2):
         print(border+fill*(m-2)+border)
    print(border*m)






def fib(5):
    cur = 1
    old = 1
    i = 1
    while (i < n):
        cur, old, i = cur+old, cur, i+1
    return cur

for i in range(10):
    print(fib(i))
