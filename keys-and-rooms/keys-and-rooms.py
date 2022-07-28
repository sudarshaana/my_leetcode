class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque
        size = len(rooms)

        visited = set()
        #visited.add(0)
        keys = set()
        keys.add(0)

        while keys:
            key = keys.pop()
            visited.add(key)
            new_keys = rooms[key]
            for k in new_keys:
                if k not in visited:
                    keys.add(k)


        return len(visited) == size