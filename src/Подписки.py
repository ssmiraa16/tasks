N=int(input())
numbers=list(map(int, input().split(" ")))

summ_even=0
summ_odd=0
min_even=101
min_ind=0
max_odd=1
max_ind=0

for i in range(0, N, 2):
    if numbers[i]<min_even:
        min_even=numbers[i]
        min_ind=i

for i in range(1, N, 2):
    if numbers[i]>max_odd:
        max_odd=numbers[i]
        max_ind=i

numbers[max_ind], numbers[min_ind]=numbers[min_ind], numbers[max_ind]

for i in range(0, N):
    if i%2==0:
        summ_even+=numbers[i]
    else:
        summ_odd+=numbers[i]

print(summ_even-summ_odd)