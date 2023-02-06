# 18번 괋호 변환
from collections import deque


def balanced(p):
    left_count = 0
    right_count = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_count += 1
        elif p[i] == ')':
            right_count += 1
        if left_count == right_count:
            return i


def correct(p):



def solution(p):
    answer = ''
    if p == answer:
        return answer
    cut = balanced(p)
    u = p[:cut+1]
    v = p[cut+1:]
    print(u, v)


p = input()
solution(p)