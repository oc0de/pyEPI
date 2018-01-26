def dutch_flag_partition(colors, arr):
    smaller, equal, larger = 0, 0, len(arr)

    while equal < larger:
        if (arr[equal] == colors[0]) or (arr[equal] == colors[1]):
            arr[equal], arr[smaller] = arr[smaller], arr[equal]
            equal += 1
            smaller += 1
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]

    tmp = equal
    larger = equal
    smaller = 0
    equal = 0

    while equal < larger:
        if (arr[equal] == colors[0]):
            arr[equal], arr[smaller] = arr[smaller], arr[equal]
            equal += 1
            smaller += 1
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]

    smaller = tmp
    equal = tmp
    larger = len(arr)
    while equal < larger:
        if (arr[equal] == colors[2]):
            arr[equal], arr[smaller] = arr[smaller], arr[equal]
            equal += 1
            smaller += 1
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]



def main():
    arr = ["r","r","b","w","y","w","r","b","y","w"]
    colors = ["r","y","w","b"]
    dutch_flag_partition(colors, arr)
    print arr



if __name__ == '__main__':
    main()
