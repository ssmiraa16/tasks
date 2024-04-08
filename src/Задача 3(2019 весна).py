## перевод в минуты
def convert_min(arr):
    return 1440*arr[0]+60*arr[1]+arr[2]
## перевод назад
def convert_back(number):
    arr=[0, 0, 0]
    arr[0]=number//1440
    arr[1]=(number-(1440*arr[0]))//60
    arr[2]=(number-(1440*arr[0])-(60*arr[1]))
    return arr

current=list(map(int, input().split(" ")))
current_new=convert_min(current)
if current_new>11518:
    current_new=current_new-1440*7

N=int(input())
arr=[]

for i in range(0, N):
    arr.append(convert_min(list(map(int, input().split(" ")))))

min_list=[]

for i in range(0, N):
    if arr[i]>current_new:
        min_list.append(arr[i])

print(" ".join(map(str, convert_back(min(min_list)))))