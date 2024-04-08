code=input()
decode=[""*i for i in range(len(code))]
j=0
k=len(code)//2
for i in range(0, len(decode)):
    if (i%2!=0):
        decode[i]=code[j]
        j+=1
    if (i%2==0):
        decode[i]=code[k]
        k+=1
print(''.join(decode))