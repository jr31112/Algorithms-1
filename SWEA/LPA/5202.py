T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])
    tmp = arr[0][1]
    count = 1
    for time in arr:
        if time[0] >= tmp:
            tmp = time[1]
            count += 1
    print('#{} {}'.format(t, count))
