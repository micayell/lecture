T=int(input())
for t in range(1,T+1):
    n,m=map(int, input().split())
    stone=list(map(int,input().split()))

    for _ in range(m):
        i,j=map(int,input().split())

        for r in range(1, j+1):
            if i-r-1 < 0 or i+r-1 > n-1: continue
            if stone[i-r-1] == 1 and stone[i+r-1] == 1:
                stone[i-r-1], stone[i+r-1] = 0, 0
            elif stone[i-r-1] == 0 and stone[i+r-1] == 0:
                stone[i-r-1], stone[i+r-1] = 1, 1

    print(f'#{t}', *stone)








    # total=0
    # for x in range(i,len(arr)):
    #     for y in range(j):
    #         if arr[]
