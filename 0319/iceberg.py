import sys
from collections import deque

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    # 빙산 정보와 함께, 현재 빙산이 있는 좌표만 따로 set으로 관리 (탐색 속도 UP)
    arr = [list(map(int, input().split())) for _ in range(N)]
    ice_coords = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                ice_coords.append((r, c))

    year = 0

    while ice_coords:
        # --- 1. 덩어리 개수 체크 (BFS) ---
        if not ice_coords: break

        visited = set()
        q = deque([ice_coords[0]])  # 첫 번째 빙산부터 시작
        visited.add(ice_coords[0])

        check_count = 1
        while q:
            r, c = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in ice_coords and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    check_count += 1

        # 전체 빙산 개수와 BFS로 방문한 개수가 다르면 분리된 것
        if check_count != len(ice_coords):
            print(year)
            return

        # --- 2. 녹이기 (Melt) ---
        melt_info = []
        new_ice_coords = []

        for r, c in ice_coords:
            sea_cnt = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if arr[r + dr][c + dc] == 0:
                    sea_cnt += 1
            if sea_cnt > 0:
                melt_info.append((r, c, sea_cnt))

        # 녹은 결과 반영 및 살아남은 빙산 업데이트
        for r, c, m in melt_info:
            arr[r][c] = max(0, arr[r][c] - m)

        for r, c in ice_coords:
            if arr[r][c] > 0:
                new_ice_coords.append((r, c))

        ice_coords = new_ice_coords
        year += 1

    print(0)  # 끝까지 분리되지 않고 다 녹은 경우



    solve()