class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = [{}]

    def set(self, index: int, val: int) -> None:
        self.snaps[-1][index] = val

    def snap(self) -> int:
        self.snaps.append({})
        return len(self.snaps)-2        

    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id, -1, -1):
            if index in self.snaps[i]:
                return self.snaps[i][index]
        return 0



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)