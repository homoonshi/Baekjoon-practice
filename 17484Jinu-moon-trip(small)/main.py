# 진우의 달 여행
# 지구와 우주 사이 = N X M 행렬
# 각 원소의 값 = 우주선이 그 공간을 지날 때 소모되는 연료의 양
# 우주선은 왼쪽아래, 아래, 오른쪽아래 로 움직일 수 있다.
# 전에 움직인 방향으로 움직일 수 없다. (같은방향 두번 연속 이동x)
# 연료를 최대한 아끼며 달의 어느 위치든 착륙하는 것이 목표
import collections
import sys

N,M=map(int,input().split())
maps=[]

direct_go=((1,-1),(1,0),(1,1))
direct_str=("l","f","r")

for i in range(N):
    maps.append(list(map(int,input().split())))

stack=collections.deque()
min_fuel=sys.maxsize

for i in range(M):

    current_fuel=maps[0][i]
    stack.append((0,i,"n",current_fuel))

    while stack:
        n,m,direct,c_fuel=stack.pop()

        for j in range(3):
            if direct=="l" and j==0:
                continue
            if direct=="f" and j==1:
                continue
            if direct=="r" and j==2:
                continue

            go_n=n+direct_go[j][0]
            go_m=m+direct_go[j][1]

            if go_m>=0 and go_m<M:

                current_fuel=c_fuel+maps[go_n][go_m]

                if current_fuel>min_fuel:
                    continue
                else:
                    if go_n==N-1:
                        min_fuel=current_fuel
                        continue
                    else:
                        stack.append((go_n,go_m,direct_str[j],current_fuel))


print(min_fuel)

