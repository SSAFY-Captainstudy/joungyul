import sys

def solve(n, r, c):
    if n == 0:
        return 0
    
    half = 2**(n-1)
    # 각 사분면의 크기
    area = half * half
    
    # r, c 위치에 따라 어떤 사분면에 있는지 확인
    if r < half and c < half:
        return solve(n - 1, r, c)
    elif r < half and c >= half:
        return area + solve(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * area + solve(n - 1, r - half, c)
    else:
        return 3 * area + solve(n - 1, r - half, c - half)

n, r, c = map(int, sys.stdin.readline().split())
print(solve(n, r, c))