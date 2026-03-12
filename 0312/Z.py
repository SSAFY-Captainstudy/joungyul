def make_square(N,sr,sc):
    global V
    if N == 1:
        visited[sr][sc] = V
        visited[sr][sc + 1] = V + 1
        visited[sr + 1][sc] = V + 2
        visited[sr + 1][sc + 1] = V + 3
        V+=4
        return

    half = 2**(N-1)
    make_square(N - 1, sr, sc)
    make_square(N - 1, sr, sc + half)
    make_square(N - 1, sr + half, sc)
    make_square(N - 1, sr+ half, sc + half)


N, r, c = map(int, input().split())
visited = [[0]*(2**N) for _ in range(2**N)]
V = 0
make_square(N,0,0)
print(visited[r][c])






