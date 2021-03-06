def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2

    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__ == "__main__":
    li = [12, 34, 22, 45, 63, 234, 21]
    shell_sort(li)
    print(li)
