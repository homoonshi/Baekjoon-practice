# 이진검색 미적용, 시간초과

import collections

N=int(input())
req_budget=list(map(int,input().split()))
req_budget.sort()
total_budget=int(input())


def calculate_budget(N:int,B:list,T:int)->int:

    req_total=int(sum(B))
    B=collections.deque(B)
    pre_budget=0
    complete_budget_num=0

    if req_total<=T:
        return max(B)

    while complete_budget_num!=N:

        if complete_budget_num==0:
            standard_budget=int(T/N)

            while B[0]<=standard_budget:
                pre_budget+=B.popleft()
                complete_budget_num+=1

        else:
            standard_budget=int((T-pre_budget)/(N-complete_budget_num))

            if standard_budget < min(B):
                return standard_budget

            while B[0]<=standard_budget:
                pre_budget+=B.popleft()
                complete_budget_num+=1


print(calculate_budget(N,req_budget,total_budget))
