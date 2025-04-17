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
        def flatten(n_list):
            for item in n_list:
                if item.isInteger():
                    self.flattened_list.append(item.getInteger())
                else:
                    flatten(item.getList())
            
        self.flattened_list = []
        flatten(nestedList)
        self.iterator_position = -1

    
    def next(self) -> int:
        self.iterator_position += 1
        index = self.iterator_position
        return self.flattened_list[index]
        
    
    def hasNext(self) -> bool:
         return self.iterator_position + 1 < len(self.flattened_list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())