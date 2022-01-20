alist = [23, 56, 43, 26, 62, 22, 79, 93, 12, 44]

def select_sort(alist):
    """选择排序"""
    n = len(alist)

    for j in range(n-1):
        min_index = j
        for i in range(1+j, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
    return alist


print(select_sort(alist))