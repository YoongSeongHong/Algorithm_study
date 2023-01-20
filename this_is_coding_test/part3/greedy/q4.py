# 4번 만들 수 없는 금액
import sys

N = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))
coins.sort()

# 1부터 만들 수 있는 지 검사
t = 1
for i in range(N):
    if coins[i] > t:  # 다음 숫자가 이전 모든 숫자 더한 값 + 1 보다 크면 break
        break
    t += coins[i]
print(t)
