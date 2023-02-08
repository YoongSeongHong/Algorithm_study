# 25번 실패율
import sys


def solution(N, stages):
    stages.sort() # 먼저 정렬해서 그 단계 포함한 배열 끝까지의 원소(해당 단계를 클리어한 사람의 수)수를 저장하게 할 것임.
    answer = stages
    arr = [0] * (N+2) # arr 각 인덱스에는 같은 단계 이상의 사람 수를 저장
    for i in range(1, N+2):
        count = 0
        for j in stages: # 정렬 된 스테이지 돌면서 i단계인 사람 수 저장
            if j == i:
                count += 1
            if j > i:  # 시간 줄이기 위해 i 이상인 수 나오면 break. 정렬 돼있으므로 더 검사할 필요 없음
                break
        arr[i] = count  # 그러면 i번째에는 i단계인 사람의 수를 저장한다.
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j] # i단계 이상인 사람 수 저장
        if sum == 0:  # 클리어 못한 단계 있으면 0 저장
            arr[i] = [i, 0]
        else:  # i단계인 사람 수 / i단계 이상인 사람 수 = 실패율
            arr[i] = [i, arr[i] / sum]  # 2차원 배열로 각 단계와 실패율 저장
    arr.pop()  # 마지막 i는 마지막 단계를 클리어 한 사람 수 이므로 없애야 함.
    arr.pop(0)  # 0단계는 없으므로 없애야 함
    arr.sort(key=lambda x: (-x[1], x[0])) # 내림 차순으로 정렬하되, 같은 실패율끼리는 오름차순
    for i in range(len(arr)):
        arr[i] = arr[i][0] # 실패율만 다시 저장
    return arr


N = int(sys.stdin.readline())
stages = list(map(int, sys.stdin.readline().split()))
solution(N, stages)
