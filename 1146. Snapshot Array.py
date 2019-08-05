import copy
class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [0] * length
        self.snaps = [{}]
        

    def set(self, index: int, val: int) -> None:
        self.snaps[-1][index] = val

    def snap(self) -> int:
        self.snaps.append(copy.deepcopy(self.snaps[-1]))
        return len(self.snaps) - 2
        

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id].get(index, self.arr[index])


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)