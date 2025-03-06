from collections import defaultdict
from threading import RLock


class Node:
    def __init__(self, freq: int):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None


class AllForOne:
    def __init__(self):
        self.map = defaultdict(Node)
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lock = RLock()

    def incrementKey(self, key: str) -> None:
        with self.lock:
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

    def decrementKey(self, key: str) -> None:
        with self.lock:
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
        with self.lock:
            return (
                "" if self.tail.prev == self.head else next(iter(self.tail.prev.keys))
            )

    def getMinKey(self) -> str:
        with self.lock:
            return (
                "" if self.head.next == self.tail else next(iter(self.head.next.keys))
            )

    def _add_node_after(self, node: Node, new_node: Node) -> None:
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev


obj = AllForOne()

obj.incrementKey("foo")
obj.incrementKey("foo")
obj.incrementKey("foo")
obj.incrementKey("foo")
obj.incrementKey("bar")
obj.incrementKey("bar")
obj.incrementKey("bar")
obj.incrementKey("bar")
# print(obj.key_count)

print(obj.getMaxKey())  # "foo" or "bar"
print(obj.getMinKey())  # "foo" or "bar"

obj.decrementKey("foo")
# print(obj.key_count)
print(obj.getMaxKey())  # "bar"
print(obj.getMinKey())  # "foo"

obj.decrementKey("foo")
obj.decrementKey("foo")
obj.decrementKey("foo")
# print(obj.key_count)

print(obj.getMaxKey())  # "bar"
print(obj.getMinKey())  # "bar"
