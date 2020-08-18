def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def quick_sort(a, l, r):
    if l >= r:
        return
    m = partition2(a, l, r)
    quick_sort(a, l, m - 1)
    quick_sort(a, m + 1, r)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')