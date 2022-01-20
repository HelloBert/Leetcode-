import collections
s1 = "jhfshfskjafhsjsjk"
s2 = "jhfshfskjafhsjsjk"
#
# def CheckPer(s1, s2):
#     d = collections.defaultdict(int)
#     for c in s1: d[c] += 1
#     for c in s2: d[c] -= 1
#     for value in d.values():
#         if value:
#             return False
#         return True

def CheckPer(s1, s2):
    if collections.Counter(s1) == collections.Counter(s2):
        return True
    return False

print(CheckPer(s1, s2))