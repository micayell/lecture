lst=[
['_','_','_','_','B','_','_',],
['_','_','_','_','_','_','_',],
['_','A','A','_','_','_','_',],
['_','_','_','_','_','_','_',],
['_','_','A','_','_','_','_',],
['_','#','#','_','B','_','_',],
['_','_','_','_','#','_','_',]]

# 7*7 배열
# A는 5칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# B는 3칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# '#'은 벽이다
# 벽 그리고 A,B 뒤로는 물풍선이 터지지 않는다.
# 물을 피할곳은 지도상 몇군데인가? - 16 -

def check(y,x):
    global lst

    directy=[0,0,-1,1]
    directx=[-1,1,0,0]
    n=0
    if lst[y][x]=='A':
        n=5
    elif lst[y][x]=='B':
        n=3
    for i in range(4):
        for j in range(1,n+1):
            dy=y+directy[i]*j
            dx=x+directx[i]*j
            if dy<0 or dx<0 or dy>6 or dx>6:continue
            if lst[dy][dx]!='@' and lst[dy][dx]!='_': break
            lst[dy][dx]='@'

for i in range(7):
    for j in range(7):
        if lst[i][j]=='A' or lst[i][j]=='B':
            check(i,j)

cnt=0
for i in range(7):
    for j in range(7):
        if lst[i][j]=='_':
            cnt+=1
print(cnt)

