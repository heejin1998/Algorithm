import sys
n = int(sys.stdin.readline())

vocabs = []

for i in range(n):
    vocabs.append(sys.stdin.readline())
vocabs = set(vocabs)
#길이가 짧은 것부터, 길이가 같으면 사전순
answer =[]

for vocab in vocabs:
    answer.append((len(vocab),vocab))
answer.sort()

for str_len, vocab in answer:
    print(vocab, end='')