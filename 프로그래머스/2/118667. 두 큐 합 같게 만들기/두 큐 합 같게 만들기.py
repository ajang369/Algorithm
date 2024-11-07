from collections import deque

def solution(queue1, queue2):
    N1 = len(queue1)
    N2 = len(queue2)

    # 두 큐를 합친 덱
    q1 = deque(queue1 + queue2)
    q2 = deque(queue2 + queue1)

    # 큐의 합
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # 합이 홀 수인 경우는 불가능
    if (sum1 + sum2) % 2 != 0:
        return -1

    def check(q, N, total):
        st = 0
        en = N

        half = sum(q)//2

        cnt = 0
        while st < en:
            if total < half and en == (2*N-1):
                break
            if total == half:
                break
            elif total < half:
                total += q[en]
                en += 1
            else:
                total -= q[st]
                st += 1

            cnt += 1

        if total != half:
            return -1
        else:
            return cnt

    ans1 = check(q1, N1, sum1)
    # ans2 = check(q2, N2, sum2)

    return ans1
    