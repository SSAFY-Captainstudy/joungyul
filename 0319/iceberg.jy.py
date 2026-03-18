import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans_years = 0

while True:
    visited = [[0]*M for _ in range(N)]
    mass_count = 0

    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0 and not visited[r][c]:
                mass_count += 1
                q = deque([(r,c)])
                visited[r][c] = 1
                while q:
                    tr, tc = q.popleft()
                    for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                        nr, nc = tr+dr, tc+dc
                        if 0 <= nr < N and 0 <= nc < M:
                                if arr[nr][nc] > 0 and not visited[nr][nc]:
                                    visited[nr][nc] = 1
                                    q.append((nr,nc))
    if mass_count >= 2:
        print(ans_years)
        break
    if mass_count == 0:
        print(0)
        break

    melt_count = [[0]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                ocean_cnt = 0
                for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr, nc = r +dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                        ocean_cnt +=1
                melt_count[r][c] = ocean_cnt
    for r in range(N):
        for c in range(M):
            arr[r][c] -= melt_count[r][c]
            if arr[r][c] < 0:
                arr[r][c] = 0
    ans_years += 1


