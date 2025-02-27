class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.head = Node(0)  # Dummy head
        self.tail = Node(0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}  # key -> Node mapping

    def _add_node_after(self, prev_node, new_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            node.keys.remove(key)
            new_freq = node.freq + 1
            nxt = node.next
            if nxt == self.tail or nxt.freq != new_freq:
                nxt = Node(new_freq)
                self._add_node_after(node, nxt)
            nxt.keys.add(key)
            self.map[key] = nxt
            if not node.keys:
                self._remove_node(node)
        else:
            # Key doesn't exist; add to the first node (or create one)
            if self.head.next == self.tail or self.head.next.freq > 1:
                new_node = Node(1)
                self._add_node_after(self.head, new_node)
            else:
                new_node = self.head.next
            new_node.keys.add(key)
            self.map[key] = new_node

    def dec(self, key: str) -> None:
        if key not in self.map:
            return

        node = self.map[key]
        node.keys.remove(key)
        if node.freq == 1:
            del self.map[key]
        else:
            # Try to use the previous node or create one if needed
            if node.prev == self.head or node.prev.freq != node.freq - 1:
                new_node = Node(node.freq - 1)
                self._add_node_after(node.prev, new_node)
                target = new_node
            else:
                target = node.prev
            target.keys.add(key)
            self.map[key] = target

        if not node.keys:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        return "" if self.tail.prev == self.head else next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        return "" if self.head.next == self.tail else next(iter(self.head.next.keys))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()