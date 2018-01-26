

def find_closest_elements_in_sorted_arrays(sorted_array):
    min_distance_so_far = float('inf')
    i, j, k = 0, 0, 0

    while (i < len(sorted_array[0]) and
            j < len(sorted_array[1]) and
                k < len(sorted_array[2])):

        min_value = min(sorted_array[0][i], sorted_array[1][j], sorted_array[2][k])
        max_value = max(sorted_array[0][i], sorted_array[1][j], sorted_array[2][k])

        if max_value - min_value < min_distance_so_far:
            min_distance_so_far = max_value - min_value
            res = (i,j,k)

        if max_value - min_value == 0: break

        if sorted_array[0][i] == min_value: i += 1
        elif sorted_array[1][j] == min_value: j += 1
        elif sorted_array[2][k] == min_value: k += 1

    return [sorted_array[i][a] for i, a in enumerate(res)]


sorted_array = [[5,10,15],[3,6,9,12,15],[8,16,24]]
print find_closest_elements_in_sorted_arrays(sorted_array)
