alist = [23, 56, 43, 26, 62, 22, 79, 93, 12, 44]

def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break
    return alist


print(insert_sort(alist))
