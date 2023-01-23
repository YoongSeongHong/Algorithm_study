# 8번 문자열 재정렬
import sys

S = sys.stdin.readline().rstrip()
S = list(S)
S.sort()
i = 0
sum_num = 0

# 아스키 코드 48 ~ 57은 숫자 0부터 9를 나타 낸다.
while ord(S[i]) >= 48 and ord(S[i]) <= 57:
    sum_num += int(S[i])
    S.pop(0)
# 배열에 남은 알파벳 들 문자열 로 합치기
s = ''.join(S)

# 숫자 더한 값 더해 주기
s += str(sum_num)
print(s)
