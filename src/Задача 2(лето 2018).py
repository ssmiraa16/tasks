decode=input()
first=decode.index("@")
last=decode.rindex("@")
print(decode[0:first]+decode[last:first:-1]+decode[last:len(decode)])