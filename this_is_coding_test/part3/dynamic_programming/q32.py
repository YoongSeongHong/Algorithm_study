# 32번 정수 삼각형
import sys

n = int(sys.stdin.readline())
arr = []
# 층 별로 이차원 배열 형태로 저장
for i in range(n):
    arr2 = list(map(int, sys.stdin.readline().split()))
    arr.append(arr2)

# dp는 하삼각행렬 형태로 저장할 것임.
dp = [[0 for j in range(n)] for i in range(n)]
dp[n-1] = arr[n-1]  # 1층은 미리 지정

# dp[i][j]에는 arr[i][j]에 밑에서 부터 오는 경로의 수 합의 최댓값 저장 -> 자연스럽게 마지막 층에는 원하는 답이 나온다.
for i in range(n-2, -1, -1):
    for j in range(i+1):
        dp[i][j] = max(dp[i+1][j]+arr[i][j], dp[i+1][j+1]+arr[i][j])
print(dp[0][0])

