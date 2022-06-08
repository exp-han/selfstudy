n, l = map(int, input().split())
pipes = list(map(int, input().split()))
pipes.sort()
res, pipedistance = 1, 0
for i in range(n):
    if i+1 >= n:
        break
    curdist = pipes[i+1] - pipes[i]
    if pipedistance + curdist < l:
        pipedistance += curdist
    else:
        res += 1
        pipedistance = 0
print(res)