# 插入排序 时间复杂度O(n*n)


def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1  # j 指的是手里牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)


li = [3, 2, 4, 1, 5, 7, 9, 6, 8]
print(li)
insert_sort(li)