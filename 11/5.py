from math import isclose as math_isclose

def square_root(x):
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    while not math_isclose(left, right):
        mid = 0.5 * (left+right)
        mid_squared = mid * mid
        if mid_squared > x:
            right = mid
        else:
            left = mid

    return left


print square_root(2.0)
# assert square_root(1.0) == math.sqrt(1.0)
# assert square_root(2.0) == math.sqrt(2.0)
# assert square_root(0.001) == math.sqrt(0.001)
# assert square_root(0.5) == math.sqrt(0.5)
# assert square_root(100000000.001) == math.sqrt(100000000.001)
