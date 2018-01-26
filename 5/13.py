def online_random_sample(it, k):
    sampling_results = it[:k]

    num_seen_so_far = k
    for x in it:
        num_seen_so_far += 1
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x

    return sampling_results
