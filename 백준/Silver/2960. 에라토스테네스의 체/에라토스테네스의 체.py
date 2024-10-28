N, K = map(int, input().split())

cnt = 0
visit = [True] * (N + 1)

# 2부터 N까지
for i in range(2, N + 1):
    # 배수를 모두 지운다
    for j in range(i, N + 1, i):
        # visit가 True이면 False로 바꿔줌
        if visit[j] != False:
            visit[j] = False
            # 지운 횟수 카운트
            cnt += 1
            # k번째이면 출력
            if cnt == K:
                print(j)
                break