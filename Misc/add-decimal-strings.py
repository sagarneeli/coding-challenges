"""
Followup: sum up two decimal point numbers represented by strings.
Return a string as the result. (Meta version)
Input
Input
num1 = "13598.0012"
num2 = "405.099"
Expected output
"14003.1002"

num1 = "0.05"
num2 = "0.95"
Expected output
"1" or "1.0"
"""


def add_decimal_strings(num1, num2):
    """Adds two decimal numbers represented as strings.

    Args:
        num1 (str): The first decimal number as a string.
        num2 (str): The second decimal number as a string.

    Returns:
        str: The sum of the two numbers as a string.
    """

    def add_integers(n1, n2, carry):
        if not n1 and not n2 and not carry:
            return 0, ""
        if not n1 and not n2:
            return carry, str(carry)

        p1 = len(n1) - 1
        p2 = len(n2) - 1
        result = []

        while p1 >= 0 or p2 >= 0:
            x1 = ord(n1[p1]) - ord("0") if p1 >= 0 else 0
            x2 = ord(n2[p2]) - ord("0") if p2 >= 0 else 0
            total = x1 + x2 + carry
            carry = total // 10
            value = total % 10
            result.append(value)
            p1 -= 1
            p2 -= 1

        return carry, "".join(str(x) for x in result[::-1])

    num1_parts = num1.split(".")
    num2_parts = num2.split(".")

    if len(num1_parts) == 1:
        num1_parts.append("0")
    if len(num2_parts) == 1:
        num2_parts.append("0")

    n1 = num1_parts[0]
    n2 = num2_parts[0]
    d1 = num1_parts[1]
    d2 = num2_parts[1]
    if len(d1) < len(d2):
        d1 = d1 + "0" * (len(d2) - len(d1))
    elif len(d2) < len(d1):
        d2 = d2 + "0" * (len(d1) - len(d2))

    carry, decimal_result = add_integers(d1, d2, 0)
    carry, integer_result = add_integers(n1, n2, carry)

    if decimal_result == "0":
        return integer_result
    else:
        return str(carry) if carry == 1 else "" + integer_result + "." + decimal_result


print(add_decimal_strings("13598.0012", "405.099"))
print(add_decimal_strings("0.05", "0.95"))
