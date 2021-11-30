class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0] * n
        keys = [0]
        while len(keys) > 0:
            key = keys.pop()
            if visited[key] == 1:
                continue
            visited[key] = 1
            keys.extend(rooms[key])
        return sum(visited) == n