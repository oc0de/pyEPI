def find_largest_subarray_with_equal_elements(arr):
    dic = {}
    max_sub = 0
    for e in arr:
        dic[e] = dic.get(e, 0) + 1
        max_sub = max(max_sub, dic[e])

    return max_sub


def main():
    arr = [2,1,2,2,3,4,5,2,1,2,2,7,8,2]
    res = find_largest_subarray_with_equal_elements(arr)
    assert res == 7

    arr = [1,2,3,4]
    res = find_largest_subarray_with_equal_elements(arr)
    assert res == 1

if __name__ == '__main__':
    main()
