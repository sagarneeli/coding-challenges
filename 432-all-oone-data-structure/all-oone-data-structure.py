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

    def _add_node_before(self, next_node, new_node):
        new_node.next = next_node
        new_node.prev = next_node.prev
        next_node.prev.next = new_node
        next_node.prev = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq
            nxt = node.next
            new_freq = freq + 1
            
            node.keys.remove(key)
            if nxt == self.tail or nxt.freq != new_freq:
                nxt = Node(new_freq)
                self._add_node_after(node, nxt)

            nxt.keys.add(key)
            self.map[key] = nxt
            if not node.keys:
                self._remove_node(node)
        else:
            first = self.head.next
            if first == self.tail or first.freq > 1:
                first = Node(1)
                self._add_node_after(self.head, first)
            first.keys.add(key)
            self.map[key] = first

    def dec(self, key: str) -> None:
        if key not in self.map:
            return

        node = self.map[key]
        node.keys.remove(key)
        if node.freq == 1:
            del self.map[key]
        else:
            prev = node.prev
            freq = node.freq
            new_freq = freq - 1
            if prev == self.head or prev.freq != new_freq:
                prev = Node(new_freq)
                self._add_node_before(node, prev)
            prev.keys.add(key)
            self.map[key] = prev

        if not node.keys:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()