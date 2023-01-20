# 2번 곱하기 혹은 더하기
import sys

S = list(sys.stdin.readline().rstrip())
print(S)
result = 0
for num in S:
    # 피연산자가 2보다 작으면 무조건 더해야 커지고 그 외는 곱해야 커짐
    if result < 2 or int(num) < 2:
        result += int(num)
    else:
        result *= int(num)
print(result)
