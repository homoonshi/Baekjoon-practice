# 이진검색 적용

N=int(input())
req_budget=list(map(int,input().split()))
req_budget.sort()
total_budget=int(input())

def calculate_budget(N:int,B:list,T:int)->int:

    left=0
    right=N-1

    budget_mid=int(T/N)

    req_total=int(sum(B))
    pre_budget=0

    if req_total<=T:
        return max(B)

    while budget_mid>=min(B[left:right]):

        mid = int((left + right) / 2)

        if B[mid]>budget_mid:
            while B[mid]>budget_mid:
                mid=int((left+mid)/2)
                if B[mid]<=budget_mid:
                    pre_budget+=sum(B[left:mid+1])
                    left=mid+1
                    break
        else :
            pre_budget+=sum(B[left:mid+1])
            left=mid+1

        budget_mid=int((T-pre_budget)/(N-left))

        if left==right:
            return budget_mid

        if budget_mid<min(B[left:right]):
            return budget_mid

    if budget_mid<min(B[left:right]):
        return budget_mid


print(calculate_budget(N, req_budget, total_budget))
