import collections

word=input()

word=word.upper()

def mostwordstudy(w:str)->str:

    if len(w)==1:
        return w

    num=collections.Counter(w)

    if len(num)==1:
        return num.most_common(1)[0][0]

    most=num.most_common(2)

    if most[0][1]==most[1][1]:
        return "?"
    else:
        return num.most_common(1)[0][0]

print(mostwordstudy(word))
