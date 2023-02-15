# 31번 금광
import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr2 = []
    # 가로 세로 그림 그대로 표현
    for j in range(0, m*n, m):
        arr2.append(arr[j:j+m])

    # 끝에서부터 최댓값 저장
    dp = [[0 for j in range(m)] for _ in range(n)]

    # 맨 마지막 열은 각각 자기 자신의 값을 가진다.
    for j in range(n):
        dp[j][m-1] = arr2[j][m-1]

    # 마지막에서 두번째 열의 dp는 이전값과 더했을때 가질 수 있는 최댓값 저장
    for j in range(m-2, -1, -1):
        for k in range(n):
            # 인덱스 맨 앞이나 끝은 벗어나지 않게 각각 예외처리
            if k - 1 < 0:
                dp[k][j] = max(dp[k][j+1] + arr2[k][j], dp[k+1][j+1] + arr2[k][j])
            elif k + 1 > n - 1:
                dp[k][j] = max(dp[k-1][j+1] + arr2[k][j], dp[k][j+1] + arr2[k][j])
            else:
                dp[k][j] = max(dp[k-1][j+1] + arr2[k][j], dp[k][j+1] + arr2[k][j], dp[k+1][j+1] + arr2[k][j])
    # mx는 dp[][0]의 최댓값 저장할 것
    mx = dp[0][0]
    for j in range(n):
        if mx < dp[j][0]:
            mx = dp[j][0]
    print(mx)

