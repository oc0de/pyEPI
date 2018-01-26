def delete_duplicates(arr):
    no_dup_index = 0
    for i in range(1, len(arr)):
        if (arr[no_dup_index] != arr[i]):
            arr[no_dup_index+1] = arr[i]
            no_dup_index += 1

    return arr[:no_dup_index+1]

def main():
    arr = [2,3,5,5,7,11,11,11,13,13,14]
    arr = delete_duplicates(arr)
    print arr

if __name__ == '__main__':
    main()
