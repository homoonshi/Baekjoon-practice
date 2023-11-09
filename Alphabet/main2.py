import sys

input=sys.stdin.readline

R,C=map(int,input().rstrip().split())

alphabet=[list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(R)]

t=[[-1,0],[0,1],[1,0],[0,-1]]

visit=[0]*26
visit[alphabet[0][0]]=1

result=0


def find_alphabet(m:int,n:int,count:int):

    global result

    if count>result:
        result=count

    for i in range(4):

        m1,n1=m+t[i][0],n+t[i][1]

        if m1<0 or n1<0 or m1>=R or n1>=C:
            continue

        num=alphabet[m1][n1]

        if visit[num]:
            continue

        visit[num]=1
        find_alphabet(m1,n1,count+1)
        visit[num]=0

    return


find_alphabet(0,0,1)
print(result)