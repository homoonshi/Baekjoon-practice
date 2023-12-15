# N = 블로그 한 날짜
# X = X일 동안 가장 많이 들어온 방문자 수 구하기
# 출력 : 가장 많이 들어온 방문자 수와 기간

N, X=map(int,input().split())
blog_meet=list(map(int,input().split()))
blog_meet_log=[]

for i in range(N):

    meet=blog_meet[i]

    if i==0:
        blog_meet_log.append(meet)
        continue

    if X<=i:
        meet-=blog_meet[i-X]

    blog_meet_log.append(blog_meet_log[i-1]+meet)

max_meet_num=max(blog_meet_log)

if max_meet_num!=0:
    print(max_meet_num)
    print(blog_meet_log.count(max_meet_num))
else:
    print("SAD")

