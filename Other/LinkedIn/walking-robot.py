"""
Implement a multithreaded program that passes control
from one thread to another in a round-robin manner (threads order is given).

Pass Criteria:
- Solution will ensure that the correct leg walks in order.
- Solution correctly uses synchronization mechanisms (for example, not wait()ing on a lock that it does not hold).
- Solution will not deadlock.

Stretch Criteria:
- Solution makes use of multiple synchronization mechanisms, as appropriate.
- Candidate can explain why they have chosen the method of approach that they did.
"""

from threading import Lock, Thread


class Robot:
    def __init__(self, legs: int):
        self.legs = legs
        self.lock = Lock()
        self.current_leg = 0

    def walk(self):
        threads = []
        for i in range(self.legs):
            thread = Thread(target=self.walk_leg, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def walk_leg(self, leg_number):
        while True:
            with self.lock:
                if self.current_leg == leg_number:
                    print(leg_number, end=" ", flush=True)
                    self.current_leg = (self.current_leg + 1) % self.legs
                    self.lock.notify_all()
                else:
                    self.lock.wait()


if __name__ == "__main__":
    robot = Robot(3)
    robot.walk()
    # Expected output: 0 1 2 0 1 2 0 1 2 ...
