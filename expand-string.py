def expand_string(input_string):
    result = []
    i = 0

    while i < len(input_string):
        char = input_string[i]  # Current character
        i += 1
        count = 0

        # Extract the number that follows the character
        while i < len(input_string) and input_string[i].isdigit():
            count += input_string[i]
            i += 1

        count = int(count) if count else 0
        result.append(char * count)  # Append the character multiplied by its count

    return "".join(result)


# Example usage
input_string = "a12b2"
expanded_string = expand_string(input_string)
print(expanded_string)  # Output: aaab


def convert_to_usd(amount, exchange_rate):
    # Perform the conversion
    result = float(amount * exchange_rate)

    # If the result is an integer (no decimals), return as integer
    if result.is_integer():
        return int(result)

    # Otherwise, format the result to two decimal places
    return round(result, 2)


# Test cases
print(convert_to_usd(10000, 1))  # Output: 10000
print(convert_to_usd(12, 1.04))  # Output: 12.48
print(convert_to_usd(100, 0.5267656))  # Output: 52.68
