def consecutive(lst):
    res, count = [], 1
    for i in range(len(lst)):
        if i+1 >= len(lst):
            res.append(count)
            break
        elif lst[i] == lst[i+1]:
            count += 1
        else:
            res.append(count)
            count = 1
    return max(res)

def horizontal(mat, i, j, newj):
    n = len(mat)
    mat[i][j], mat[i][newj] = mat[i][newj], mat[i][j]
    col1 = consecutive([mat[x][j] for x in range(n)])
    col2 = consecutive([mat[x][newj] for x in range(n)])
    return max(col1, col2)

def vertical(mat, i, j, newi):
    mat[i][j], mat[newi][j] = mat[newi][j], mat[i][j]
    row1, row2 = consecutive(mat[i]), consecutive(mat[newi])
    return max(row1, row2)

def swapCompare(mat, i, j):
    n = len(mat)
    left = horizontal(mat, i, j, j-1) if j > 0 else 0
    right = horizontal(mat, i, j, j+1) if j < n-1 else 0
    up = vertical(mat, i, j, i-1) if i > 0 else 0
    down = vertical(mat, i, j, i+1) if i < n-1 else 0
    return max(list([left, right, up, down]))

############################################################
n = int(input())
mat, maxnum, flag = [], float('-inf'), False
for _ in range(n):
    row = [char for char in map(str, input())]
    mat.append(row)

for i in range(n):
    for j in range(n):
        tmp = swapCompare(mat, i, j)
        if tmp > maxnum:
            maxnum = tmp
    #     if maxnum == n:
    #         flag = True
    #         print(maxnum)
    #         break
    # if flag:
    #     break
# if not flag:
print(maxnum)