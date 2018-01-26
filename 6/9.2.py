def convert_int_to_roman(n):
    strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    res = ""
    for i,j in enumerate(nums):    
        res += (n // j) * strs[i]
        n %= j
        if n == 0: return res


print convert_int_to_roman(3549)
