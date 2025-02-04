class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0  # Points to the front element
        self.tail = 0  # Points to the next insertion point
        self.count = 0  # Number of elements in the buffer

    def push(self, x):
        if self.count == self.capacity:
            self.resize(self.capacity * 2)

        self.buffer[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise IndexError("Buffer is empty")

        value = self.buffer[self.head]
        self.buffer[self.head] = None  # Optional: Clear the slot
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return value

    def peek(self):
        if self.count == 0:
            raise IndexError("Buffer is empty")
        return self.buffer[self.head]

    def size(self):
        return self.count

    def resize(self, new_size):
        new_capacity = new_size
        new_buffer = [None] * new_capacity
        for i in range(self.count):
            new_buffer[i] = self.buffer[(self.head + i) % self.capacity]
        self.buffer = new_buffer
        self.head = 0
        self.tail = self.count
        self.capacity = new_capacity


# Usage example
buffer = CircularBuffer(3)
print(buffer.size())  # -> 0

buffer.push(1)
print(buffer.peek())  # -> 1

buffer.push(2)
buffer.push(3)

buffer.push(4)  # Should trigger resize instead of error

print(buffer.size())  # -> 4

print(buffer.pop())  # -> 1
print(buffer.pop())  # -> 2

buffer.push(5)

print(buffer.pop())  # -> 3
print(buffer.pop())  # -> 4
print(buffer.pop())  # -> 5

# Test case for resize
resize_test_buffer = CircularBuffer(2)
resize_test_buffer.push(10)
resize_test_buffer.push(20)
resize_test_buffer.push(30)  # Should trigger resize
resize_test_buffer.push(40)
resize_test_buffer.push(50)

print(resize_test_buffer.size())  # -> 5
print(resize_test_buffer.pop())  # -> 10
print(resize_test_buffer.pop())  # -> 20
print(resize_test_buffer.pop())  # -> 30
print(resize_test_buffer.pop())  # -> 40
print(resize_test_buffer.pop())  # -> 50
