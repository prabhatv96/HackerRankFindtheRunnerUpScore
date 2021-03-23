if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    lst = []
    for i in range(n):               
        if arr[i]<m:
            lst.append(arr[i])
    run = max(lst)
    print(run)
