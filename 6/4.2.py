def merge_two_array(a,n,b,m):
    a_idx = n-1
    b_idx = m-1
    write_idx = len(a)-1

    while a_idx >= 0 and b_idx >= 0:
        if a[a_idx] >= b[b_idx]:
            a[write_idx] = a[a_idx]
            a_idx -= 1
        else:
            a[write_idx] = b[b_idx]
            b_idx -= 1

        write_idx -= 1

    while b_idx >= 0:
        a[write_idx] = b[b_idx]
        b_idx -= 1
        write_idx -= 1

a = [6, 8, None, None, None]
b = [2, 3, 7]
merge_two_array(a, 2, b, 3)
print a
