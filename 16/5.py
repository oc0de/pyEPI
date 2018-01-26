def is_pattern_contained_in_grid(grid, pattern):
    def helper(x, y, offset):
        if offset == len(pattern): return True

        if (0 <= x < len(grid) and 0 <= y < len(grid[0]) and
                grid[x][y] == pattern[offset] and (x,y, offset) not in previous_attempts and
                    any(helper(x+a,y+b, offset+1) for a,b in ((1,0),(-1,0),(0,1),(0,-1)))):
            return True
        previous_attempts.add((x,y, offset))
        return False

    previous_attempts = set()
    return any(helper(x, y, 0) for y in range(len(grid[0])) for x in range(len(grid)))


grid = [[1,2,3],[3,4,5],[5,6,7]]
pattern = [1,3,4,6]
assert is_pattern_contained_in_grid(grid, pattern) == True
pattern = [1,2,3,4]
assert is_pattern_contained_in_grid(grid, pattern) == False
