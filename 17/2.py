def minimum_total_waiting_time(service_times):
    service_times.sort()
    total_waiting_time, curr_waiting_time = 0, 0
    for t in service_times[:-1]:        
        curr_waiting_time += t
        total_waiting_time += curr_waiting_time

    return total_waiting_time


service_times = [2,5,1,3]
assert 10 == minimum_total_waiting_time([5, 1, 2, 3])
