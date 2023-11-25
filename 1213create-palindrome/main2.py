import collections
import sys

# CREATE PALINDROME
# 1. input hansoo's english name
# 2. and make palindrome with alphabet of hansoo's english name

hansoo_e_name = sys.stdin.readline().rstrip()
Alphabet = collections.Counter(hansoo_e_name)
# the number of alphabets of hansoo's english name
# 한수의 영어 이름 알파벳 개수를 세서 딕셔너리로 정리한다.

palindrome_string = ''
center_string = ''

for k, v in sorted(Alphabet.items()):
    if v%2!=0:
        if center_string=='':
            center_string = k
        else:
            print("I'm Sorry Hansoo")
            exit()
    # 알파벳의 개수가 홀수일 때 알파벳을 중앙에 하나 넣어준다.
    palindrome_string+=k*(v//2)

print(palindrome_string+center_string+palindrome_string[::-1])

