# 9번 문자열 압축

def solution(s):
    # 문제 에서 입력에 쌍 따옴표 까지 같이 포함 돼서 지워 버림
    s = s.replace('"', '')
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):  # i는 자르는 단위
        check = s[0:i]
        result = ""  # i개 씩 합쳐서 볼 때 결과
        count = 1  # 겹치는 문자열 수
        # check 에 0부터 i 까지 문자열 을 저장 하고, i + i 부터 검사
        for j in range(i, len(s), i):
            if check == s[j:j+i]:
                count += 1
            else:  # 개수가 2 이상 이면 숫자 붙여서 출력
                if count >= 2:
                    result += str(count) + str(check)
                else:  # 1이면 생략
                    result += str(check)
                check = s[j:j+i]
                count = 1
        result += str(count) + check if count >= 2 else check
        print(result, len(result))
        if len(result) < answer:
            answer = len(result)
    return answer


s = input()
print(solution(s))