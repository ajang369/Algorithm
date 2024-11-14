def solution(lottos, win_nums):
    answer = []

    lottos.sort(reverse=True)
    win_nums.sort(reverse=True)

    cnt = 0
    zero = 0
    for i in lottos:
        if i != 0:
            if i in win_nums:
                cnt += 1
        if i == 0:
            zero += 1

    answer.append(cnt)
    answer.append(cnt + zero)
    
    ans = []
    for i in answer:
        if i == 6:
            ans.append(1)
        elif i == 5:
            ans.append(2)
        elif i == 4:
            ans.append(3)
        elif i == 3:
            ans.append(4)
        elif i == 2:
            ans.append(5)
        else:
            ans.append(6)
    ans.sort()
    return ans
