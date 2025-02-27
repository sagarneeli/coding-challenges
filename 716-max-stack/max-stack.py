from sortedcontainers import SortedDict

class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MaxStack:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = SortedDict()
        
    def push(self, x: int) -> None:
        node = Node(x)
        self._add_node(node)
        
        if x in self.map:
            self.map[x].append(node)
        else:
            self.map[x] = [node]


    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1

        node = self.tail.prev
        self._remove_node(node)
        node_list = self.map[node.val]
        node_list.remove(node)

        if not node_list:
            del self.map[node.val]

        return node.val
        

    def top(self) -> int:
        if self.head.next == self.tail:
            return -1
        return self.tail.prev.val
        

    def peekMax(self) -> int:
        if not self.map:
            return -1
        return self.map.peekitem(-1)[0]
        

    def popMax(self) -> int:
        if not self.map:
            return -1

        max_val, node_list = self.map.peekitem(-1)
        node = node_list.pop()
        if not node_list:
            del self.map[max_val]
        
        self._remove_node(node)
        return node.val

    
    def _add_node(self, node: Node) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    

    def _remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()