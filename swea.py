T=int(input())
for t in range(1,T+1):
    n, m = map(int, input().split())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))

    if n > m:
        n, m = m, n
        A, B = B, A

    Max=0
    for i in range(m-n+1):
        case=0
        for j in range(i,i+n):
            case += A[j-i]*B[j]
        if Max < case:
            Max = case

    print(f'#{t} {Max}')
