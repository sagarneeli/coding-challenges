class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Time: O(N), where N is length of order
        Space: O(M + N), where M is the length of s and N is the length of order
        """
        count = [0] * 26  # Fixed space for lowercase English letters
        
        # Count occurrences of each character in s
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        result = []
        
        # Add characters in the order defined by 'order'
        for ch in order:
            index = ord(ch) - ord('a')
            if count[index] > 0:
                result.append(ch * count[index])
                count[index] = 0  # Mark as used
        
        # Add remaining characters not in 'order'
        for i in range(26):
            if count[i] > 0:
                result.append(chr(i + ord('a')) * count[i])
        
        return "".join(result)

        