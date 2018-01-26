
def compute_tower_hanoi(num_rings):
    def helper(num_rings, from_peg, to_peg, temp_peg):
        if num_rings > 0:
            helper(num_rings-1, from_peg, temp_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            print('Move peg from', from_peg, 'to_peg', to_peg)
            print('from_peg', pegs[from_peg], 'to_peg', pegs[to_peg])
            print
            helper(num_rings-1, temp_peg, to_peg, from_peg)


    NUM_PEGS = 3
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]


    helper(num_rings, 0, 1, 2)

num_rings = 3
compute_tower_hanoi(3)
