# 3번 문자열 뒤집기
import sys

S = list(sys.stdin.readline().rstrip())
zero_series = 0  # 계속 되는 0 그룹 수
one_series = 0  # 계쏙 되는 1 그룹 수

# 다음 숫자가 다른 값이 나오면 연속이 끊기는 경우 이므로 S[i] 그룹 수를 늘린다.
for i in range(len(S)-1):
    if int(S[i]) == 0:
        if int(S[i+1]) == 1:
            zero_series += 1
    else:
        if int(S[i+1]) == 0:
            one_series += 1
# 마지막에 나오는 숫자 그룹을 하나 더 추가
if int(S[-1]) == 0:
    zero_series += 1
elif int(S[-1]) == 1:
    one_series += 1

# 0들만 뒤집 거나 1들만 뒤집는 경우 중 작은 값이 최적의 해
print(min(zero_series, one_series))