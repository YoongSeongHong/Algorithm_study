# 11404번 플로이드
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = int(1e9)  # 무한대 표현

# (n+1) * (n+1) 이차원 배열 생성, 값은 무한대로 초기화
graph = [[INF for _ in range(n+1)] for i in range(n+1)]
for i in range(m):
    # a는 시작점, b는 도착점, c는 비용
    a, b, c = map(int, sys.stdin.readline().split())
    # 같은 경로가 두번 입력되는 경우에는 최솟값을 저장
    if graph[a][b] != INF:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

# 시작점, 도착점 같을 때 비용은 0
for i in range(n+1):
    graph[i][i] = 0

# 플로이드워셜 - a에서 i를 거쳐 b로 가는 모든 경우의 최솟값으로 최신화
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        # 경로가 없어서 INF면 0 출력
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print('')

