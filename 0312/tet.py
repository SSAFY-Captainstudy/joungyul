import sys
sys.stdin = open('tet_input.txt', 'r')
def tet_1():
    global max_sum

    for i in range(N):
        for j in range(M-3):
            current_sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i][j+3]
            if current_sum > max_sum:
                max_sum = current_sum


    for i in range(N-3):
        for j in range(M):
            current_sum = arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j]
            if current_sum > max_sum:
                max_sum = current_sum
    return



def tet_2():
    global max_sum
    for i in range(N-1):
        for j in range(M-1):
            current_sum = arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]
            if current_sum > max_sum:
                max_sum = current_sum
    return


def tet_3():
# def tet_4():
# def tet_5():

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0
can_anw = []
tet_1()
tet_2()
# tet_3()
# tet_4()
# tet_5()
print(max_sum)

# print(arr)











