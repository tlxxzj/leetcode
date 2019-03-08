class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = [0]
        used_keys = set()
        used_keys.add(0)
        while len(keys) > 0:
            k = keys.pop()
            for key in rooms[k]:
                if key not in used_keys:
                    used_keys.add(key)
                    keys.append(key)
        return len(used_keys) == len(rooms)