# import sys
# sys.stdin = open("1486_input.txt", "r")
def janghoon(current_sum,start):
    global dif_height

    print(current_sum,start)
    if current_sum >= B:
        if current_sum - B < dif_height:
            dif_height = current_sum - B
        return

    for i in range(start,len(arr)):
        janghoon(current_sum+arr[i],i+1)


T = int(input())
for tc in range(1,1+T):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    dif_height = float("inf")
    janghoon(0,0)
    print(f'#{tc} {dif_height}')








