import collections

# CREATE PALINDROME
# 1. input hansoo's english name
# 2. and make palindrome with alphabet of hansoo's english name

hansoo_e_name = input()
Alphabet=collections.Counter(hansoo_e_name)
# the number of alphabets of hansoo's english name
# 한수의 영어 이름 알파벳 개수를 세서 딕셔너리로 정리한다.

Alphabet=dict(sorted(Alphabet.items(),reverse=True))
# 알파벳을 사전의 역순으로 정리해준다.

Odd = 0

for Alphabet_num in (Alphabet.values()):
    if(Alphabet_num%2!=0):
        Odd+=1
        if Odd>=2:
            print(Odd)
            print("I'm Sorry Hansoo")
            exit()
# 알파벳의 개수가 홀수인 알파벳이 2개 이상인지 확인한다.

palindrome_string=[]
value_num_sum=0
# 지금까지 만들어진 팰린드롬의 개수가 몇개인지 확인한다.
# 개수가 홀수인 알파벳을 중앙에 넣을 때 어느 위치에 넣어야 하는지 확인하기 위한 수

for k, v in Alphabet.items():
    if v%2==0:
        for n in range(int(v/2)):
            palindrome_string.append(k)
            palindrome_string.insert(0,k)
            value_num_sum+=2
    # 알파벳의 개수가 짝수라면 양 끝에 넣어준다.
    else :
        value_num_sum=int(value_num_sum/2)
        palindrome_string.insert(value_num_sum,k)
        # 알파벳의 개수가 홀수일 때 알파벳을 중앙에 하나 넣어준다.
        for n in range(int((v-1)/2)):
            palindrome_string.append(k)
            palindrome_string.insert(0,k)
        # 알파벳의 개수가 홀수이면서 3개이상일 때 나머지 알파벳을 가장자리에 넣어준다.

palindrome_string=''.join(map(str,palindrome_string))
# 리스트로 정리된 팰린드롬을 string 변수로 바꿔준다.

print(palindrome_string)

