class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Time: O(max(N1,N2))
        Space: O(max(N1,N2))
        """
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        result = []

        while i >= 0 or j >= 0:
            x1 = ord(num1[i]) - ord("0") if i >= 0 else 0
            x2 = ord(num2[j]) - ord("0") if j >= 0 else 0
            value = (carry + x1 + x2) % 10
            carry = (carry + x1 + x2) // 10
            result.append(value)
            i -= 1
            j -= 1
        
        if carry:
            result.append(carry)

        return "".join(str(x) for x in result[::-1])

        

        