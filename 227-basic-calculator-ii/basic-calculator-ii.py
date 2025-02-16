class Solution:
    def calculate(self, s: str) -> int:
        s += '+'  # Append a '+' to force the last number to be processed
        result, last_number, current_number = 0, 0, 0
        operator = '+'
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)  # Build multi-digit numbers
            
            if char in "+-*/":  # Process current_number when an operator is encountered
                if operator == '+':
                    result += last_number
                    last_number = current_number
                elif operator == '-':
                    result += last_number
                    last_number = -current_number
                elif operator == '*':
                    last_number *= current_number
                elif operator == '/':
                    last_number = int(last_number / current_number)  # Truncate toward zero

                operator = char  # Update operator
                current_number = 0  # Reset current number
        
        return result + last_number  # Add the last processed number

        