"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
"""

# def oneRditAway(s1, s2):
#     m = len(s1)
#     n = len(s2)
#
#     if abs(m-n) > 1:
#         return False
#     for i in range(min(m, n)):
#         if s1[i] == s2[i]:
#             continue
#         else:
#             return s1[i+1:] == s2[i:] or s1[i:] == s2[i+1:] or s1[i+1] == s2[i+1]
#     return False
#
# a = "pale"
# b = "ple"
#
# print(oneRditAway(a, b))
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1: return False
        if len(first) > len(second): first, second = second, first
        for i in range(len(first)):
            if first[i] == second[i]: continue
            else:
                return first[i:] == second[i+1:] or first[i+1:] == second[i+1:]
        return True
