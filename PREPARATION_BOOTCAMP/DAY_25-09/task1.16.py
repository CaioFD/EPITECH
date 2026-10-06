def remove_duplicates(values):
    result = []
    for value in values:
        if value not in result:     # only add it if we have not seen it yet
            result.append(value)
    return result


print(remove_duplicates([1, 1, 1, 1, 2, 2, 2, 2, 2]))            # [1, 2]
print(remove_duplicates([42, '42', 42.0, 21 + 21, 42 * 10 / 10])) # [42, '42']