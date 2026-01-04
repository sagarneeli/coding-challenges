from math import sqrt

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def get_divisors(n):
            divisors = []
            for i in range(1, int(sqrt(n) + 1)):
                if n % i == 0:
                    divisors.append(i)
                    if i != (n // i):
                        divisors.append(n // i)
            return divisors

        total_sum = 0
        for num in nums:
            divisors = get_divisors(num)
            if len(divisors) == 4:
                total_sum += sum(divisors)
        
        return total_sum
        