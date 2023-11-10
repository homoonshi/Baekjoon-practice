

n=int(input())
a=list(map(int,input().split()))
x=int(input())

result=0

a.sort()

c1=0
c2=n-1

while c1<c2:

    sum=a[c1]+a[c2]

    if sum==x:
        result+=1
        c1+=1
        c2-=1
        continue

    if sum>x:
        c2-=1
        continue

    if sum<x:
        c1+=1
        continue


print(result)