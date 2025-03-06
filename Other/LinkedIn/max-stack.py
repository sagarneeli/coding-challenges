"""
Given a stack-like data structure that also allows stack-like access to its elements by values.
Implement push(), peep(), pop(), peekMax(), popMax().

Example:
Given a stack of (1, 3, 2, 5, 3, 4, 5, 2):
peek() => 2, peekMax() => 5
pop() => 2; peek() => 5, peekMax() => 5
pop() => 5; peek() => 4, peekMax() => 4
push(6): peek() => 6, peekMax() => 6
popMax() => 6; peek() => 4, peekMax() => 4
popMax() => 5; peek() => 4, peekMax() => 4
"""

# from typing import TypeVar, Generic

# T = TypeVar("T")


# class MaxStack(Generic[T]):
#     def __init__(self):
#         self.stack = []
#         self.max_stack = []

#     def push(self, to_push: T) -> None:
#         """
#         Push an element to the stack.

#         Args:
#             to_push: The element to push to the stack.
#         """
#         self.stack.append(to_push)
#         if not self.max_stack or to_push >= self.max_stack[-1]:
#             self.max_stack.append(to_push)

#     def pop(self) -> T:
#         """
#         Remove and return the top element of the stack.

#         Returns:
#             T: The top element of the stack.
#         """
#         if not self.stack:
#             raise IndexError("pop from empty stack")
#         top = self.stack.pop()
#         if top == self.max_stack[-1]:
#             self.max_stack.pop()
#         return top

#     def peek(self) -> T:
#         """
#         Return the top element of the stack.

#         Returns:
#             T: The top element of the stack.
#         """
#         return self.stack[-1]

#     def peekMax(self) -> T:
#         """
#         Return the maximum element of the stack.

#         Returns:
#             T: The maximum element of the stack.
#         """
#         return self.max_stack[-1]

#     def popMax(self) -> T:
#         """
#         Remove and return the maximum element of the stack.

#         Returns:
#             T: The maximum element of the stack.
#         """
#         if not self.max_stack:
#             return None  # Handle empty max_stack

#         max_val = self.max_stack.pop()

#         # Iterate through the main stack and rebuild the max_stack
#         temp_stack = []
#         while self.stack and self.stack[-1] != max_val:
#             temp_stack.append(self.stack.pop())

#         self.stack.pop()  # Remove the max value from the main stack

#         while temp_stack:
#             self.push(temp_stack.pop())  # Rebuild the main stack and max_stack

#         return max_val

#     def __len__(self) -> int:
#         """
#         Return the number of elements in the stack.
#         """
#         return len(self.stack)


# if __name__ == "__main__":
#     stack = MaxStack()
#     stack.push(1)
#     stack.push(3)
#     stack.push(2)
#     stack.push(5)
#     stack.push(3)
#     stack.push(4)
#     stack.push(5)
#     stack.push(2)
#     print(stack.peek())
#     print(stack.peekMax())
#     print(stack.pop())
#     print(stack.peek())
#     print(stack.peekMax())
#     print(stack.pop())
#     print(stack.peek())
#     print(stack.peekMax())
#     print(stack.push(6))
#     print(stack.peek())
#     print(stack.peekMax())
#     print(stack.popMax())
#     print(stack.peek())
#     print(stack.peekMax())
#     print(stack.popMax())
#     print(stack.peek())
#     print(stack.peekMax())


# from sortedcontainers import SortedDict
# import threasding


# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.prev = None
#         self.next = None


# class MaxStack:
#     def __init__(self):
#         self.head = Node(None)  # Dummy head
#         self.tail = Node(None)  # Dummy tail
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.max_map = SortedDict()  # Stores values in sorted order
#         self.lock = threading.Lock()

#     def push(self, to_push: int) -> None:
#         with self.lock:
#             node = Node(to_push)
#             node.prev = self.tail.prev
#             node.next = self.tail
#             self.tail.prev.next = node
#             self.tail.prev = node

#             if to_push in self.max_map:
#                 self.max_map[to_push].append(node)
#             else:
#                 self.max_map[to_push] = [node]

#     def peek(self) -> int:
#         with self.lock:
#             if self.head.next == self.tail:
#                 raise IndexError("peek from empty stack")
#             return self.tail.prev.val

#     def pop(self) -> int:
#         with self.lock:
#             if self.head.next == self.tail:
#                 raise IndexError("pop from empty stack")
#             node = self.tail.prev
#             self.tail.prev = node.prev
#             node.prev.next = self.tail
#             self.max_map[node.val].pop()
#             if not self.max_map[node.val]:
#                 del self.max_map[node.val]
#             return node.val

#     def peekMax(self) -> int:
#         with self.lock:
#             if not self.max_map:
#                 raise IndexError("peekMax from empty stack")
#             return next(reversed(self.max_map))

#     def popMax(self) -> int:
#         with self.lock:
#             if not self.max_map:
#                 raise IndexError("popMax from empty stack")
#             max_val = next(reversed(self.max_map))

#             # Remove the most recently added node with max_val
#             node = self.max_map[max_val].pop(-1)  # Remove last (most recent) occurrence
#             if not self.max_map[max_val]:
#                 del self.max_map[max_val]

#             # Remove node from linked list
#             node.prev.next = node.next
#             node.next.prev = node.prev

#             return node.val


# # Testing the MaxStack implementation with the given example:
# # Stack sequence: {1, 3, 2, 5, 3, 4, 5, 2}


# # Test the MaxStack class
# # Testing the MaxStack implementation with print statements

# # Initialize MaxStack
# stack = MaxStack()

# # Push elements {1, 3, 2, 5, 3, 4, 5, 2}
# elements = [1, 3, 2, 5, 3, 4, 5, 2]
# for num in elements:
#     stack.push(num)
#     print(f"Pushed {num}")

# # Perform peek() and peekMax() checks
# print(f"peek(): {stack.peek()}")  # Expected: 2
# print(f"peekMax(): {stack.peekMax()}")  # Expected: 5

# # Perform pop() and check state
# print(f"pop(): {stack.pop()}")  # Expected: 2
# print(f"peek() after pop: {stack.peek()}")  # Expected: 5
# print(f"peekMax() after pop: {stack.peekMax()}")  # Expected: 5

# # Pop again
# print(f"pop(): {stack.pop()}")  # Expected: 5
# print(f"peek() after pop: {stack.peek()}")  # Expected: 4
# print(f"peekMax() after pop: {stack.peekMax()}")  # Expected: 5

# # Push 6 and check state
# stack.push(6)
# print(f"Pushed 6")
# print(f"peek() after push(6): {stack.peek()}")  # Expected: 6
# print(f"peekMax() after push(6): {stack.peekMax()}")  # Expected: 6

# # Pop max (6) and check state
# print(f"popMax(): {stack.popMax()}")  # Expected: 6
# print(f"peek() after popMax(6): {stack.peek()}")  # Expected: 4
# print(f"peekMax() after popMax(6): {stack.peekMax()}")  # Expected: 5

# # Pop max (5) and check state
# print(f"popMax(): {stack.popMax()}")  # Expected: 5
# print(f"peek() after popMax(5): {stack.peek()}")  # Expected: 4
# print(f"peekMax() after popMax(5): {stack.peekMax()}")  # Expected: 4


class MaxStack:
    def __init__(self):
        # Initialize two stacks:
        # - self.stack: to store the values.
        # - self.max_stack: to store the maximum up to that index.
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        """
        Push x onto the stack.
        Time Complexity: O(1)
        """
        self.stack.append(x)
        # For max_stack, if it's empty, the current value is the maximum.
        # Otherwise, compare with the current maximum.
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x, self.max_stack[-1]))

    def pop(self) -> int:
        """
        Remove and return the top element from the stack.
        Time Complexity: O(1)
        """
        self.max_stack.pop()  # Remove the top from the max stack as well.
        return self.stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        Time Complexity: O(1)
        """
        return self.stack[-1]

    def peekMax(self) -> int:
        """
        Retrieve the maximum element in the stack.
        Time Complexity: O(1)
        """
        return self.max_stack[-1]

    def popMax(self) -> int:
        """
        Remove and return the maximum element in the stack.
        If there are multiple maximum elements, remove the one closest to the top.
        Time Complexity: O(n) in the worst case.
        """
        max_val = self.peekMax()  # Get the current maximum.
        buffer = []  # Temporary buffer to hold popped elements.

        # Pop elements until we find the maximum.
        while self.top() != max_val:
            buffer.append(self.pop())

        # Remove the maximum element.
        self.pop()

        # Push back the elements that were in the buffer.
        while buffer:
            self.push(buffer.pop())

        return max_val
