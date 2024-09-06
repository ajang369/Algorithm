def KMP_table(pattern):
    pl = len(pattern)
    table = [0]*pl

    pidx = 0 # 패턴의 인덱스 접근(접두사)
    for idx in range(1, pl): # 패턴의 인덱스 접근(접미사)

        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = table[pidx-1]

        # 값이 일치하는 경우, pidx +1, 그 값을 table에 저장
        if pattern[idx] == pattern[pidx]:
            pidx += 1
            table[idx] = pidx

    return table

def KMP(word, pattern):
    table = KMP_table(pattern)

    result = []
    pidx = 0

    for idx in range(len(word)):
        # 단어와 패턴이 일치하지 않으면, pidx를 변경
        while pidx > 0 and word[idx] != pattern[pidx]:
            pidx = table[pidx - 1]

        # 해당 인덱스에서 값이 일치 -> pidx +1
        if word[idx] == pattern[pidx]:
            # pidx가 패턴 끝까지 도달 -> 시작 인덱스 값 계산하여 추가
            if pidx == len(pattern)-1:
                result.append(idx - len(pattern)+1 +1)
                pidx = table[pidx] # 이후 pidx값 변경
            else:
                pidx += 1
    return result

W = input()
P = input()

res = KMP(W, P)
print(len(res))
print(*res)