# # class Solution:
# #     def rotate(self, matrix: list[list[int]]) -> None:
#
# print(6 // 1.3)
#
#
list = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
#
# # list3 = [[]]
#
# list2 = [[7, 4, 1],
#          [8, 5, 2],
#          [9, 6, 3]]
# # print(list)


class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        # 先在纵向上进行上下翻转
        # 切片会创建新的对象进而开辟新地址
        matrix[:] = matrix[::-1]
        print(matrix)
        # 然后沿对角线翻转
        for i in range(length):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

                # matrix[0][1], matrix[1][0] = matrix[1][0], matrix[0][1]
                # i = 1, j = 0
                # [[7, 8, 9],
                #  [4, 5, 6],
                #  [1, 2, 3]]

                # [[7, 4, 1],
                #  [8, 5, 2],
                #  [9, 6, 3]]

                # [[1, 2, 3],
                #  [4, 5, 6],
                #  [7, 8, 9]]

                # i = 2, j = 0, 1
                # matrix[0][2], matrix[2][0] = matrix[2][0], matrix[0][2]
                # matrix[1][2], matrix[2][1] = matrix[2][1], matrix[1][2]

                # i = 3, j = 0, 1, 2
                # matrix[0][3], matrix[3][0] = matrix[3][0], matrix[0][3]


a = Solution()
a.rotate(list)
print(list)
