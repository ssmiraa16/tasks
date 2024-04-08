code=input()
decode=""
sign=['.', '!', '?', ' ', ',', '-']
alpha=[chr(i) for i in range(97, 123)]
counter=0
max_counter=0
for i in range(0, len(code)):
    if code[i] not in sign:
        counter+=1
    else:
        if counter>max_counter:
            max_counter=counter
        counter=0
max_counter=max(max_counter, counter)
for j in range(0, len(code)):
    if code[j] in sign:
        decode+=code[j]
    else:
        decode+=alpha[alpha.index(code[j])-(26-max_counter)]
print(decode)