def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # 让high游标左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        # 让low右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 当循环退出时，low==high
    alist[low] = mid_value

    # 使用递归对low左边的列表进行快速排序
    quick_sort(alist, first, low-1)     # 在递归的时候low-1给了last
    # 使用递归对low右边的列表进行快速排序
    quick_sort(alist, low+1, last)      # low+1给了first

if __name__ == "__main__":
    li = [12, 34, 22, 45, 63, 234, 21]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)