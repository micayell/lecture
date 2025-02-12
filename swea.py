T=int(input())
for t in range(1,T+1):
    # total=0
    # for j in range(len(arr)-n+1): #회문을 확인하는 구간의 첫 글자 인덱스
    #     for k in range(n//2): #회문의 길이 절반만큼 비교
    #         if arr[j+k] != arr[j+n-1-k]:
    #             break # 비교 글자가 다르면 현재구간 중지
    #     else: # break에 걸리지 않고 for 종료, 회문이면
    #         total+=1
    # print(total)


    text=input()
    n=len(text)
    mid=n//2
    total=0

    if n % 2 == 1:
        for i in range(n//2):
            if text[mid-i-1] != text[mid+i-1]:
                break
        else:
            total+=1

    print(f'#{t} {total}')



    # for i in range(len(t)-n+1):
    #     for j in range(n//2):
    #         if t[]
    #
    # for j in range(len(arr-n+1)):
    #     for k in range(n//2):
    #         if arr[j+k] != arr[j+n-1-k]:
    #             break
    #     else:
    #         total+=1


