def bubble_sort(alist):
    """使用顺序表实现"""
    n = len(alist)
    # 外层循环控制到底要走多少次
    for j in range(n-1):
        # 考虑时间复杂度
        count = 0
        # 内层循环控制从头走到尾
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            return


if __name__ == "__main__":
    li = [12, 34, 22, 45, 63, 234, 21]
    bubble_sort(li)
    print(li)