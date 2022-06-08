def digitSum(n):
    res = 0
    for digit in str(n):
        res += int(digit)
    return res
n, candidate, flag = int(input()), 0, False
while candidate < n:
    divsum = candidate + digitSum(candidate)
    if divsum == n:
        flag = True
        print(candidate)
        break
    candidate += 1
if not flag:
    print(0)
