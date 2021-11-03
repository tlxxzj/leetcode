# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def _generator(nestedList):
            #print(nestedList)
            for item in nestedList:
                if item.isInteger():
                    yield item.getInteger()
                else:
                    for i in _generator(item.getList()):
                        yield i
                
        self._generator = _generator(nestedList)
        self._next_val = next(self._generator, None)
    
    def next(self) -> int:
        next_val = self._next_val
        self._next_val = next(self._generator, None)
        return next_val
    
    def hasNext(self) -> bool:
        return self._next_val != None
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())