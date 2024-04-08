import re
n, q=map(int, input().split(" "))

domains=[]
clients=[]

for i in range(0, n):
    domains.append(input())

for j in range(0, q):
    clients.append(input())

for req in clients:
    first, second=req.split(" ")
    reg_exp=fr"{first}+(.)+{second}"
    print(len(list(filter(lambda x: re.search(reg_exp, x), domains))))