
def unique_word(s):
    if s == "":
        return True
    li = list(s)
    n = len(li)
    for j in range(n):
        for i in range(j+1, n):
            if li[j] == li[i]:
                return False
            else:
                continue
        if j == n-1:
            return True
s = ""

print(unique_word(s))



#for i in range(li):
#    print(i)
