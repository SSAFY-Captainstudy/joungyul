import sys
from collections import deque


# 파일 입력 (필요시)
# sys.stdin = open("input.txt", "r")

def solve(arr, si, sj):
    q = deque([(si, sj)])
    arr[si][sj] = 1  # 시작점 방문 처리 (벽으로 변경)

    # 상, 하, 좌, 우
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            # 범위 내에 있고 벽(1)이 아닐 때
            if 0 <= nr < 16 and 0 <= nc < 16 and arr[nr][nc] != 1:
                if arr[nr][nc] == 3:  # 도착!
                    return 1

                # 길(0)이면 방문 처리 후 큐에 삽입
                arr[nr][nc] = 1
                q.append((nr, nc))

    return 0  # 길을 못 찾았을 때


for _ in range(10):
    tc = input()
    # 문자열로 받아서 처리하면 map(int) 과정 없이 더 빠를 수 있음
    maze = [list(map(int, input())) for _ in range(16)]

    # 시작점 찾기 (리스트 컴프리헨션으로 간소화 가능하지만 가독성 위해 유지)
    si, sj = 0, 0
    for i in range(16):
        if 2 in maze[i]:
            si, sj = i, maze[i].index(2)
            break

    print(f'#{tc} {solve(maze, si, sj)}')