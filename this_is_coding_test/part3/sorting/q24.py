# 24번 안테나
import sys

# 해결 방안: 정렬 했을 때 무조건 가운데 있을 수록 거리 총 합은 짧은 점 이용
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
mn_index = 0
mid = N // 2

# N이 홀수면 딱 가운데 집이 거리 총 합 제일 짧음
if N % 2 == 1:
    sum = 0
    dist = 0
    for i in range(N):
        # 절댓값 따져서 총 거리 구하기
        if arr[mid] - arr[i] >= 0:
            dist = arr[mid] - arr[i]
        elif arr[mid] - arr[i] < 0:
            dist = arr[i] - arr[mid]
        sum += dist
    print(arr[mid])

# N이 짝수면 가운데 두 값 중 더 총 거리 더 짧은 집 출력
else:
    sum = 0
    sum2 = 0
    dist = 0
    dist2 = 0
    for i in range(N):
        # 절댓값 따져서 가운데 두 집 중 왼쪽 집의 총 거리 (sum)
        if arr[mid-1] - arr[i] >= 0:
            dist = arr[mid-1] - arr[i]
        elif arr[mid-1] - arr[i] < 0:
            dist = arr[i] - arr[mid-1]
        # 절댓값 따져서 가운데 두 집 중 오른쪽 집의 총 거리 (sum2)
        if arr[mid] - arr[i] >= 0:
            dist2 = arr[mid] - arr[i]
        elif arr[mid] - arr[i] < 0:
            dist2 = arr[i] - arr[mid]
        sum += dist
        sum2 += dist2
    # 두 집중 더 거리 짧은 집 출력
    if sum <= sum2:
        print(arr[mid-1])
    else:
        print(arr[mid])