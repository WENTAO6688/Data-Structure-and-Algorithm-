# coding: utf-8
class Point:
    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b

DIRECTIONS = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,-1),(-2,1)]

from collections import deque
class Solution:

    def shortestpath(self, grid, source, destination):
        queue = deque([(source.x, source.y)])
        distance = {(source.x, source.y) : 0}

        while queue:
            location_x, location_y = queue.popleft()
            if (location_x, location_y) == (destination.x, destination.y):
                return distance[(source.x, source.y)]

            for dx, dy in DIRECTIONS:
                next_x, next_y = location_x + dx, location_y + dy
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(grid, next_x, next_y):
                    continue

                distance[(next_x, next_y)] = distance[(source.x, source.y)] + 1
                queue.append((next_x, next_y))

        return -1

    def is_valid(self, grid, x, y):
        m,n = len(grid), len(grid[0])
        if x< 0 or x>m or y<0 or y>n:
            return False
        return not grid[x][y]

