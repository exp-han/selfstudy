casenum = 1
resarr = []
while True:
    l, p, v = map(int, input().split())
    if l==0 and p==0 and v==0:
        break
    res = 0
    while v > 0:
        res += min(l, v)
        v -= p
    resarr.append(res)
for item in resarr:
    print("Case {}: ".format(casenum) + str(item))
    casenum += 1