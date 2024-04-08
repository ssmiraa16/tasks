pswd=input()
dict1=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
      "V", "W", "X", "Y", "Z"]
dict2=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
dict3=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
if len(pswd)<8:
    print("NO")
else:
    if (any(n in pswd for n in dict1)):
        if (any(n in pswd for n in dict2)):
            if (any(n in pswd for n in dict3)):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")