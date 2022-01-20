"""
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

"""

class Solution:
    def compressString(self, S):
        if not S:
            return ""
        ant = S[0]
        ans = ""
        ch = 0

        for i in S:
            if i == ant:
                ch += 1
            else:
                ans += ant + str(ch)
                ant = i
                ch = 1
        ans += ant + str(ch)
        return ans if len(ans) < len(S) else S