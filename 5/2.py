def plus_one(arr):
    carry = 1
    for i in reversed(range(len(arr))):
        arr[i] += carry
        carry = arr[i] / 10
        arr[i] %= 10

    if carry != 0:
        arr.insert(0,1)



def main():
    arr = [9,9,9,9,9]
    plus_one(arr)
    assert arr == [1,0,0,0,0,0]
    arr = [1,9,8,7,9]
    plus_one(arr)
    assert arr == [1,9,8,8,0]


if __name__ == '__main__':
    main()
