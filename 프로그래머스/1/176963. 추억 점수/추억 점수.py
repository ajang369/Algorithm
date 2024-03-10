def solution(name, yearning, photo):
    n = len(name)
    m = len(photo)

    answer = []
    for i in range(m):
        res = 0
        for j in photo[i]:
            if j in name:
                idx = name.index(j)
                res += yearning[idx]
        answer.append(res)
    
    return answer