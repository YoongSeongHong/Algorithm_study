# 23번 국영수
import sys

N = int(sys.stdin.readline())
lst = []

# 배열에 이름, 국어, 영어, 수학 순으로 저장
for i in range(N):
    p = list(sys.stdin.readline().split())
    lst.append(p)

# 국어 영어 수학 점수를 정수형으로 변환
for i in range(N):
    for j in range(1, 4):
        lst[i][j] = int(lst[i][j])

# 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순 으로 정렬
lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(lst[i][0])
