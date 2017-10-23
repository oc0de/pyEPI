def dutch_flag_partition(pivot_index, arr):
    smaller, equal, larger = 0, 0, len(arr)
    pivot = arr[pivot_index]

    while equal < larger:
        if arr[equal] < pivot:
            arr[equal], arr[smaller] = arr[smaller], arr[equal]
            equal += 1
            smaller += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]


def main():
    arr = [-3,5,-1,1,-5,2,4,0]
    dutch_flag_partition(3, arr)

    print arr



if __name__ == '__main__':
    main()
