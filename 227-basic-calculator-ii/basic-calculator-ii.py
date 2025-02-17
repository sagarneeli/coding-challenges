class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if ch in "+-*/" or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                if op == "-":
                    stack.append(-num)
                if op == "*":
                    stack.append(stack.pop() * num)
                if op == "/":
                    stack.append(int(stack.pop() / num))
                
                op = ch
                num = 0

        return sum(stack)        