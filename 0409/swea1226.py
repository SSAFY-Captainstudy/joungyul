import sys
sys.stdin = open("input.txt", "r")
from collections import deque
def find_start(arr):
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return i, j
    return

def solve(arr,i,j):
    global anw
    q = deque([])
    q.append((i,j))
    visited = [[False]*16 for _ in range(16)]
    visited[i][j] = True
    while q:
        si, sj = q.popleft()
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        for k in range(4):
            ni, nj = si + dx[k], sj + dy[k]
            if 0<= ni <16 and 0<=nj<16 and not visited[ni][nj] and arr[ni][nj] != 1:
                if arr[ni][nj] == 0:
                    q.append((ni,nj))
                    visited[ni][nj] = True
                elif arr[ni][nj] == 3:
                    anw+= 1
                    return anw
    return anw

T = 10
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    # print(arr)
    anw = 0
    si, sj = find_start(arr)
    anw = solve(arr,si,sj)
    print(f'#{tc} {anw}')













