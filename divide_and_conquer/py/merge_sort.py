def merge_sort(A):
    n = len(A)
    if n==1:
        return A
    m = n//2
    print(A[:m]," * ",A[m:])
    B = merge_sort(A[:m])
    C = merge_sort(A[m:])
    A_dash = Merge(B,C)
    return A_dash


def Merge(B,C):
    D = []
    while len(B)!=0 and len(C)!=0:
        b=B[0]
        c=C[0]
        if b<=c:
            D.append(b)
            B.pop(0)
        else:
            D.append(c)
            C.pop(0)
    if len(B)!=0:
        D.extend(B)
    if len(C)!=0:
        D.extend(C)
    return D

print(merge_sort([7,2,5,3,7,13,1,6]))