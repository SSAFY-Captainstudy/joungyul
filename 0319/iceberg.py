# def melt(arr,cnt):
#     global ocean_cnt
#
#
#     for r in range(N):
#         for c in range(M):
#             if arr[r][c] != 0:
#                 for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                     nr, nc = r + dr, c + dc
#                     if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
#                         ocean_cnt += 1
#                 melt_count[r][c] = ocean_cnt
#                 melted_arr[r][c] = arr[r][c] - melt_count[r][c]
#                 if melted_arr[r][c] < 0:
#                     melted_arr[r][c] = 0
#                 ocean_cnt = 0
#
#
#     if not melted_arr:
#         return
#
#
#     melt(melted_arr,cnt+1)
#






















import sys
sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
melt_count = [[0]*M for _ in range(N)]
melted_arr = [[0]*M for _ in range(N)]
mass = [[0]*M for _ in range(N)]
ocean_cnt = 0
mass_cnt = 0

# melt(arr,0)
for r in range(N):
    for c in range(M):
        if arr[r][c] != 0:
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr, nc = r + dr, c+ dc
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                    ocean_cnt += 1
            melt_count[r][c] = ocean_cnt
            melted_arr[r][c] = arr[r][c] - melt_count[r][c]
            if melted_arr[r][c] < 0:
                melted_arr[r][c] = 0
            ocean_cnt = 0

for r in range(N):
    for c in range(M):





# print(melt_count)
print(melted_arr)
# print(arr)