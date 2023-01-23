# 7번 럭키 스트레이트
import sys

N = int(sys.stdin.readline())
N = str(N)

#  N1에 앞부분, N2에 뒷부분 저장
N1 = N[0:len(N)//2]
N2 = N[len(N)//2:len(N)]

#  정수형 리스트 로 바꿔 줌
N1 = list(map(int, N1))
N2 = list(map(int, N2))

#  합이 같다면 LUCKY, 다르면 READY 출력
if sum(N1) == sum(N2):
    print('LUCKY')
else:
    print('READY')

