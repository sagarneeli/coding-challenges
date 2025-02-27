from typing import TypeVar, Generic, Optional
from sortedcontainers import SortedDict  # pip install sortedcontainers
import threading

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, val: T):
        self.val: T = val
        self.prev: Optional['Node[T]'] = None
        self.next: Optional['Node[T]'] = None

class MaxStack(Generic[T]):
    def __init__(self):
        # Dummy head and tail nodes for the doubly-linked list.
        self.head: Node[T] = Node(None)  # type: ignore
        self.tail: Node[T] = Node(None)  # type: ignore
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # SortedDict mapping value -> list of nodes with that value.
        self.map: SortedDict[T, list[Node[T]]] = SortedDict()
        
        # Lock for thread safety.
        self.lock = threading.RLock()

    def push(self, to_push: T) -> None:
        with self.lock:
            node = Node(to_push)
            self._add_node(node)
            if to_push in self.map:
                self.map[to_push].append(node)
            else:
                self.map[to_push] = [node]

    def top(self) -> T:
        with self.lock:
            if self.head.next == self.tail:
                raise IndexError("peek from empty stack")
            return self.tail.prev.val

    def pop(self) -> T:
        with self.lock:
            if self.head.next == self.tail:
                raise IndexError("pop from empty stack")
            node = self.tail.prev
            self._remove_node(node)
            nodes_list = self.map[node.val]
            nodes_list.remove(node)
            if not nodes_list:
                del self.map[node.val]
            return node.val

    def peekMax(self) -> T:
        with self.lock:
            if not self.map:
                raise IndexError("peekMax from empty stack")
            return self.map.peekitem(-1)[0]

    def popMax(self) -> T:
        with self.lock:
            if not self.map:
                raise IndexError("popMax from empty stack")
            max_val, nodes_list = self.map.peekitem(-1)
            node = nodes_list.pop()
            if not nodes_list:
                del self.map[max_val]
            self._remove_node(node)
            return node.val

    def _add_node(self, node: Node[T]) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def _remove_node(self, node: Node[T]) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    # Helper method to visualize the current stack from bottom to top.
    def get_stack_elements(self) -> list[T]:
        elements = []
        cur = self.head.next
        while cur != self.tail:
            elements.append(cur.val)
            cur = cur.next
        return elements


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()