from itertools import combinations, permutations

def solution(user_id, banned_id):
    # 1. user_id에서 밴 개수만큼의 조합을 모두 구해서 밴 아이디와 비교
    
    n = len(banned_id)
    com = list(permutations(user_id, n))
    
    answer = []
    for li in com:
        flag = True
        for i in range(n):
            u = li[i]
            b = banned_id[i]
            if len(u) == len(b):
                for j in range(len(u)):
                    if b[j] == '*':
                        continue
                    if u[j] != b[j]:
                        flag = False
                        break
            else:
                flag = False
                break
                        
        if flag:
            if set(li) not in answer:
                answer.append(set(li))
    
    return len(answer)