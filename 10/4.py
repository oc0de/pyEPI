import heapq

class Star:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def distance(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def __lt__(self, rhs):
        return self.distance < rhs.distance

def find_closest_k_stars(k, stars):
    max_heap = []
    for i in stars:
        heapq.heappush(max_heap, (-i.distance,i))
        if len(max_heap) == k+1:
            heapq.heappop(max_heap)

    return [x[1] for x in heapq.nlargest(k, max_heap)]

stars = [
    Star(1, 2, 3), Star(5, 5, 5), Star(0, 2, 1), Star(9, 2, 1),
    Star(1, 2, 1), Star(2, 2, 1)]

closest_stars = find_closest_k_stars(3, stars)

assert len(closest_stars) == 3
assert closest_stars[0].distance == Star(0, 2, 1).distance
assert closest_stars[0].distance == Star(2, 0, 1).distance
assert closest_stars[1].distance == Star(1, 2, 1).distance
assert closest_stars[1].distance == Star(1, 1, 2).distance
