# 15번 특정 거리의 도시 찾기
import sys
from collections import deque


def bfs(graph, root, dist):
    dq = deque()
    dq.append(root)
    dist[root] = 0  # 시작 지점은 거리 0
    while dq:
        n = dq.popleft()
        if n in graph:
            for num in graph[n]: # n에서 갈 수 있는 노드 들이 num
                if dist[num] == -1:  # 그 중 에서도 방문 안 된 것만
                    dist[num] = dist[n] + 1  # n의 최단 경로에서 +1 한 값을 저장
                    dq.append(num)  # 데크에 추가


N, M, K, X = map(int, sys.stdin.readline().split())
graph = {}  # 그래프를 딕셔너리 형태로 저장
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if start not in graph:
        graph[start] = []
        graph[start].append(end)
    else:
        graph[start].append(end)

# 방문 안 한 지점은 -1로 저장
dist = {n+1: -1 for n in range(N)}
bfs(graph, X, dist)

check = 0
for i in dist.keys():
    if dist[i] == K:
        print(i)
        check = 1  # 최단 거리 K인 노드 존재 하면 -1 출력 x

if check == 0:  # 최단 거리 K인 노드 존재 안하면 -1 출력 o
    print(-1)
