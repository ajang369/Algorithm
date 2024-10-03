def solution(topping):
    answer = []
    right_num, left_num = [], []
    right_set, left_set = set(), set()

    for idx, top in enumerate(topping):
        right_set.add(top)
        right_num.append(len(right_set))

        left_set.add(topping[len(topping) - 1 - idx])
        left_num.append(len(left_set))

    len_left = len(left_num)
    
    
    for i in range(len(right_num) - 1):
        if right_num[i] == left_num[len_left - i - 2]:    
            answer.append(i)

    return len(answer)