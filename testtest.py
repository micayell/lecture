T=int(input())
for t in range(T):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    i,j=map(int,input().split())
    for _ in range(m):
        for k in range(n):
            if i < 1 or j >