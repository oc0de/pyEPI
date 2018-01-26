def delete_specific_duplicate(arr, key):
    last_index, i = len(arr), 0

    while i < last_index:
        if arr[i] == key:
            arr[i] = arr[last_index-1]
            last_index -= 1
        else:
            i += 1

    return i

def main():
    arr = [2, 3, 5, 5, 7, 11, 11, 11, 13, 13]
    result = delete_specific_duplicate(arr, 11)
    assert result == 7


if __name__ == '__main__':
    main()
