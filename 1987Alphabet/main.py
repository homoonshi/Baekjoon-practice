import collections
import heapq

R,C=map(int,input().split())

alphabet=[]

for i in range(R):
    alphabet.append(input())

e=collections.defaultdict(int)

result=[]
tem=[[0,1],[1,0],[0,-1],[-1,0]]

def find_alphabet(m:int,n:int,sum:int)->int:

    e[alphabet[m][n]]+=1
    sum+=1
    res=0

    for i in range(0,4):

        m1=m+tem[i][0]
        n1=n+tem[i][1]

        if m1<0 or n1<0 or m1>=R or n1>=C:
            continue

        if e[alphabet[m1][n1]]>0:
            continue

        if find_alphabet(m1,n1,sum)>0:
            res+=1

    if res==0:
        if result and sum<result[0][1]:
            sum-=1
            return 1
        heapq.heappush(result,(-sum,sum))
        e[alphabet[m][n]]=0
        sum-=1
        return 1

    if m==0 and n==0:
        return result[0][1]

    e[alphabet[m][n]]=0
    return 1

print(find_alphabet(0,0,0))