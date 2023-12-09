# 우선순위
# 1.자주나오는단어
# 2.길이가긴단어
# 3.사전순으로앞에있는단어
# 문제조건
# M보다짧은길이안외움 M'이상'만외운다
# 영어지문에나오는단어개수N
import collections
import sys


N, M = map(int, input().split())
word_list = []

for i in range(0, N):

    word = sys.stdin.readline().rstrip()

    if len(word) < M:
        continue

    word_list.append(word)


word_count=collections.Counter(word_list)

word=sorted(word_count.items(), key=lambda x : (-x[1],-len(x[0]),x[0]))
voca_list=[ key for key,value in word]

for i in range(len(voca_list)):

    print(voca_list[i])