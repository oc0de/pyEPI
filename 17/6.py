
MPG = 20
def find_ample_city(gallons, distances):
    curr_gas, total_gas, start_city, remaining_gas = 0, 0, 0, 0
    for i in range(len(gallons)):
        curr_gas = gallons[i]*MPG - distances[i]
        if remaining_gas >= 0:
            remaining_gas += curr_gas
        else:
            remaining_gas = curr_gas
            start_city = i

        total_gas += curr_gas

    return start_city if total_gas >= 0 else -1


# gallons = (20, 15, 15, 15, 35, 25, 30, 15, 65, 45, 10, 45, 25)
# distances = (15, 20, 50, 15, 15, 30, 20, 55, 20, 50, 10, 15, 15)

gallons = [50,20, 5, 30, 25, 10, 10]
distances = [900, 600, 200, 400, 600, 200, 100]
assert find_ample_city(gallons, distances) == 3
