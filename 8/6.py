import collections
import sys
import random


# @include
def examine_buildings_with_sunset(it):
    BuildingWithHeight = collections.namedtuple('BuildingWithHeight',
                                                ('id', 'height'))
    candidates = []
    for building_idx, building_height in enumerate(reversed(it)):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))
    return [candidate.height for candidate in candidates]
# @exclude

it = [8, 7, 9, 12, 3, 16, 30, 2]
print examine_buildings_with_sunset(it)
