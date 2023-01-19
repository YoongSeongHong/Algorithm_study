# 1번 모험가 길드
import sys

N = int(sys.stdin.readline())
guild = list(map(int, sys.stdin.readline().split()))

# 정렬
guild.sort()
gps = 0  # 그룹 수
members = 0  # 그룹의 멤버 수
for i in range(N):
    members += 1
    if members >= guild[i]:  # 멤버 수가 가장 최근에 들어온 멤버의 공포도 보다 크거나 같으면
        gps += 1  # 그룹 결성
        members = 0

print(gps)
