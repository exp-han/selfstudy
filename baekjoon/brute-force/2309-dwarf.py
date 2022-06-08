arr, res = [], []
for i in range(9):
    n = int(input())
    arr.append(n)
flag = False
for i in range(9):
    for j in range(i+1, 9):
        tmp = sum(arr) - arr[i] - arr[j]
        if tmp == 100:
            flag = True
            for k in range(9):
                if k != i and k != j:
                    res.append(arr[k])
            break
    if flag:
        break
res.sort()
for item in res:
    print(item)

