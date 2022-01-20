def replaceSpace(s, len):
    s12 = s[:len]
    s1 = s12.replace(" ", "%20")
    return s1

s = "Mr John Smith    "
print(replaceSpace(s, 13))
