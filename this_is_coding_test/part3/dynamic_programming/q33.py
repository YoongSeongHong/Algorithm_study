# 33번 퇴사
import sys

N = int(sys.stdin.readline())
consult = []
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    consult.append(lst)

# dp[i]는 i번째 날로부터 마지막 날까지 낼 수 있는 최대 이익
dp = [0] * (N+1)
# mx는 뒤에서부터 계산할 때, 현재까지의 최대 상담 금액에 해당하는 변수
mx = 0

# 마지막 날부터 dp 진행
for i in range(N-1, -1, -1):
    # time 변수에는 i일차와 그 날 잡힌 상담의 소요예상일 합 저장
    time = consult[i][0] + i
    # time이 N보다 작거나 같아야 그 상담은 진행 가능
    if time <= N:
        dp[i] = max(mx, consult[i][1] + dp[time]) # i번째 날 상담을 안했을 때 이후의 최댓값과 i번째 날 상담을 할 때의 누적 금액 비교
        mx = dp[i]  # 최대 누적값 최신화
    # time이 N보다 크면 어차피 그 상담은 진행 불가이므로 그 dp엔 전까지의 최댓값 저장
    else:
        dp[i] = mx

print(mx)