def solution(board, skill):
    N = len(board) + 1
    M = len(board[0]) + 1

    answer = 0
    tmp = [[0] * M for _ in range(N)]
    for dmg in skill:
        flag = dmg[0]
        st_y = dmg[1]
        en_y = dmg[3] + 1
        st_x = dmg[2]
        en_x = dmg[4] + 1
        dgree = dmg[5]

        if flag == 1:
            tmp[st_y][st_x] -= dgree
            tmp[en_y][en_x] -= dgree
            tmp[st_y][en_x] += dgree
            tmp[en_y][st_x] += dgree
        else:
            tmp[st_y][st_x] += dgree
            tmp[en_y][en_x] += dgree
            tmp[st_y][en_x] -= dgree
            tmp[en_y][st_x] -= dgree

    # 누적합 계산 (왼 -> 오른쪽)
    for y in range(N):
        for x in range(1, M):
            tmp[y][x] += tmp[y][x-1]

    # 누적합 계산 (위 -> 아래쪽)
    for x in range(M):
        for y in range(1, N):
            tmp[y][x] += tmp[y-1][x]

    # 최종 board 값 계산 및 조건 검사
    for i in range(N-1):
        for j in range(M-1):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer