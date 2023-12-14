# 서류심사, 면접시험 둘 중 적어도 하나가 다른 지원자보다 떨어지지 않으면 선발
# = A가 B보다 서류심사, 면접시험 둘 다 떨어지면 탈락
# 첫째 줄 테스트케이스 (1<=T<=20)
# 테스트 케이스 첫째 줄 지원자 숫자 N(1<=N<=100000)
# 서류심사순위, 면접성적순위 순서로 받음
# 두 성적 순위는 1위부터 N위까지 동석차 없이 결정
# 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수 구하기

import sys

T = int(input())

new_cruit=[]

for i in range(T):

    N=int(input())
    applicant=[]
    new_cruit_num=0
    docu_min=0
    inte_min=0

    for j in range(N):

        document,interview=map(int,sys.stdin.readline().rstrip().split())

        if document==1:
            inte_min=interview
            new_cruit_num+=1
            continue
        if interview==1:
            docu_min=document
            new_cruit_num+=1
            continue

        applicant.append((document,interview))

    applicant=sorted(applicant,key=lambda x:x[0],reverse=True)

    while applicant:

        document, interview = applicant.pop()

        if docu_min<document:
            continue

        if inte_min>interview:
            inte_min=interview
            new_cruit_num+=1

    new_cruit.append(new_cruit_num)

for i in range(T):
    print(new_cruit[i])


