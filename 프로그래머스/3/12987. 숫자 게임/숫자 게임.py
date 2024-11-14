def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    idx_a = 0
    idx_b = 0
    answer = 0
    for i in range(len(A)):
        if A[idx_a] < B[idx_b]:
            answer += 1
            idx_a += 1
            idx_b += 1
        else:
            idx_a += 1
    return answer

# 7 6 2 1
# 8 6 2 2

# 7 6 2 1
# 8 2 6 2