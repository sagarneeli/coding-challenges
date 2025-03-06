def pow_n(x: int, n: int) -> float:
    def helper(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        result = helper(x * x, n // 2)
        return x * result if n % 2 else result

    result = helper(x, abs(n))
    return result if n > 0 else 1 / result


print(pow_n(2, 10))  # 1024
print(pow_n(2, -3))  # 0.125
