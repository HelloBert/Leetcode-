
def canPermutePalindrome(s: str):
    a = set()
    for i in s:
        if i in a:
            a.remove(i)
        else:
            a.add(i)
    return len(a) < 2

s = "tactcoadsfas"
print(canPermutePalindrome(s))