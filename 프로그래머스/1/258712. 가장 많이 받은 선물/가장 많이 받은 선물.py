def solution(friends, gifts):
    n = len(friends)
    m = len(gifts)
    answer = 0

    dic = {}
    for i in friends:
        dic[i] = [0,0]            
    give = [[0]*n for _ in range(n)]
    
    for gift in gifts:
        a, b = gift.split()
        dic[a][0] += 1
        dic[b][1] += 1
        
        x = friends.index(a)
        y = friends.index(b)
        give[x][y] += 1
    gift_cnt = [0]*n
    for i in range(n):
        gift_cnt[i] = dic[friends[i]][0] - dic[friends[i]][1]        
    
    res = [0] * n
    
    
    
    for i in range(n):
        for j in range(i):
            if give[i][j] > give[j][i]:
                res[i] += 1
            elif give[i][j] == give[j][i]:
                if gift_cnt[i] > gift_cnt[j]:
                    res[i] += 1
                elif gift_cnt[i] < gift_cnt[j]:
                    res[j] += 1
            else:
                res[j] += 1
    answer = max(res)

    
    return answer
