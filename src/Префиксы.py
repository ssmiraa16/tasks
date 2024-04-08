import re
n, q =map(int, input().split(" "))

employees=[]
request=[]

for i in range(0, n):
    employees.append(input())

for j in range(0, q):
    request.append(input().split(" "))
    request[j][0]=int(request[j][0])

for req in request:
    k, prefix=req
    employee_pref=list(filter(lambda x: re.match(prefix, x), employees))
    employee_pref.sort()
    if k<=len(employee_pref):
        print(employees.index(employee_pref[k-1])+1)
    else:
        print(-1)