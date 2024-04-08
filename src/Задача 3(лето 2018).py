N = int(input())
an = list(map(int, input().split()))
an.sort()
res = 0
if N > 2:
    res += an[1] - an[0]
    res += an[-1] - an[-2]
    cc = [res]
    cn = [res]
    nc = [res]
    for i in range(2,N-1):
        cc.append(min(nc[i-2], cc[i-2]) - an[i-1] + an[i])
        cn.append(min(nc[i-2], cc[i-2]))
        nc.append(min(nc[i-3], cc[i-3], cn[i-3]) - an[i-1] + an[i])
    print(min(nc[-1], cc[-1], cn[-1]))
else:
    print(an[1] - an[0])