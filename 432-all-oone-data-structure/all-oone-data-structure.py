class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.map = defaultdict(Node)
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            if node.next != self.tail and node.next.freq == node.freq + 1:
                node.next.keys.add(key)
                self.map[key] = node.next
            else:
                new_node = Node(node.freq + 1)
                new_node.keys.add(key)
                self.map[key] = new_node
                self._add_node_after(node, new_node)

            node.keys.remove(key)
            if not node.keys:
                self._remove_node(node)
        else:
            first = self.head.next
            if first == self.tail or first.freq > 1:
                new_node = Node(1)
                new_node.keys.add(key)
                self.map[key] = new_node
                self._add_node_after(self.head, new_node)
            else:
                first.keys.add(key)
                self.map[key] = first

    def dec(self, key: str) -> None:
        if key not in self.map:
            return

        node = self.map[key]
        if node.freq == 1:
            del self.map[key]   
        else:
            if node.prev != self.head and node.prev.freq == node.freq - 1:
                node.prev.keys.add(key)
                self.map[key] = node.prev
            else:
                new_node = Node(node.freq - 1)
                new_node.keys.add(key)
                self.map[key] = new_node
                self._add_node_after(node.prev, new_node)

        node.keys.remove(key)
        if not node.keys:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        return "" if self.tail.prev == self.head else next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        return "" if self.head.next == self.tail else next(iter(self.head.next.keys))

    def _add_node_after(self, node: Node, new_node: Node) -> None:
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()