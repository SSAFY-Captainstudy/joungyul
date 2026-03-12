def solve(N,r,c):
    if N == 0:
        return 0
    half = 2**(N-1) # 각 사분면의 크기
    area = half * half

    #r,c위치에 따라 어떤