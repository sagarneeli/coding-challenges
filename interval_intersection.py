def interval_intersection(first_list, second_list):
    i, j = 0, 0
    result = []

    while i < len(first_list) and j < len(second_list):
        # Find overlap
        start = max(first_list[i][0], second_list[j][0])
        end = min(first_list[i][1], second_list[j][1])

        # If overlap, add to result i.e valid overlap
        if start <= end:
            result.append([start, end])

        # Move to next interval
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1
    return result


# Example usage
list1 = [[1, 5], [10, 15]]
list2 = [[2, 6], [12, 18]]
print("Intersection of Intervals:", interval_intersection(list1, list2))

def flatten_json(list1):
    result = {}
    def dfs(data, parent_key, separator):
        if isinstance(data, dict):
            for k, v in data.items():
                new_key = f"{parent_key}{separator}{k}" if parent_key else k
                dfs(v, new_key, separator)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                new_key = f"{parent_key}{separator}{i}" if parent_key else str(i)
                dfs(item, new_key, separator)
        else:
            result[parent_key] = data
    dfs(list1, "", ".")
    return result

print(flatten_json(list1))
                dfs(v, new_key, separator)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                new_key = f"{parent_key}{separator}{i}" if parent_key else str(i)
                dfs(item, new_key, separator)
        else:
            result[parent_key] = data