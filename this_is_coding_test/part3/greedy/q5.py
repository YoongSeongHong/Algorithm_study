# 5번 볼링공 고르기
import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
arr = [0] * 11
# arr 의 각 인덱스 는 그 숫자 무게의 볼링공 의 개수를 저장 한다.
for x in data:
    arr[x] += 1
result = 0

# A가 무게 1 공을 고르는 경우 부터 시작.
for i in range(1, M+1):
    N -= arr[i]  # 무게 i인 공의 수를 N에서 빼고,
    result += arr[i] * N  # 빼고 남은 수 * 무게 i인 공의 갯수 = A가 무게 i인 공을 고를 때의 경우의 수
print(result)

# N, M = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
# arr.sort()
# result = 0
# # 정렬 후 이중 for 문으로 인덱스 값이 클 때만 개수 +
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         if arr[i] < arr[j]:
#             result += 1
# print(result)