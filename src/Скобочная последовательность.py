def is_valid(string):
    depth = 0
    for i in range(len(string)):
        if string[i] == '(':
            depth += 1
        else:
            depth -= 1
            if depth < 0:
                return False
    if depth != 0:
        return False
    return True
def how_many(string):
    count=0
    if string.find('?') != -1:
        count += how_many(string.replace('?', '(', 1)) + how_many(string.replace('?', ')', 1))
    else:
        valid = is_valid(string)
        if valid:
            return count + 1
    return count

string = input()
print(how_many(string))