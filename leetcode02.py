'''
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
例：
输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
'''

class Solution:
    def setZero(self, matrix):

        length = len(matrix)
        for i in range(length):
            for j in matrix[i]:
                if j == 0:








list = [[1, 1, 0, 8],
        [2, 3, 4, 7],
        [5, 7, 9, 6]]


a = Solution()
a.setZero(list)
















