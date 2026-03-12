import sys
sys.stdin = open("bridge_input.txt", "r")
from collections import deque
def numbering(r,c,num):
    q = deque([(r,c)])
    visited[r][c] = num
    while q:
        cur_r, cur_c = q.popleft()
        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr, nc = dr+cur_r, dc+cur_c
            if 0 <= nr < N and 0<= nc < M:
                if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = num
                    q.append((nr,nc))
def make_bridge():











N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt_bridge = 0
island_num = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            numbering(i,j,island_num)
            island_num += 1



print(cnt_bridge)