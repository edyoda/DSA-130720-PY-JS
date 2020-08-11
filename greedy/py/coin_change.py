# Uses python3
# import sys

def get_change(m):
    # changes = [1,3,4]
    return_list = []
    while(m!=0):
        if m>=10:
            return_list.append(10)
            m-=10
        elif m>=5:
            return_list.append(5)
            m-=5
        elif m>=1:
            return_list.append(1)
            m-=1
    return len(return_list)

# if __name__ == '__main__':
    # m = int(sys.stdin.read())
    # m = int(input())
    # print(get_change(m))
