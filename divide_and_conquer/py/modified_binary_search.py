def binary_search(A,n,x,first_occurence):
    low = 0
    high = n-1
    result = -1
    while(low<=high):
        mid = (low+high)//2
        if(A[mid]==x):
            result = mid
            if first_occurence == True:
                high = mid-1
            else:
                low = mid+1
        elif(x<A[mid]):
            high = mid-1
        else:
            low = mid+1
    return result

A = [5,6,7,7,7,7,9]
n = len(A)
x = 7

first_index = binary_search(A,n,x,True)
last_index = binary_search(A,n,x,False)

print("first index is ",first_index)
print("last index is ",last_index)

print("the count of the element",x,"is ",last_index-first_index+1)