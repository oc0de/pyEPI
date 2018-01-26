def isReachable(arr):
    r, i, last_index = 0, 0, len(arr)-1

    while i <= r and r < last_index:
        r = max(r, i + arr[i])
        i += 1

    return r >= last_index

def main():
    arr = [3,3,1,0,2,0,1]
    print isReachable(arr)


if __name__ == '__main__':
    main()
