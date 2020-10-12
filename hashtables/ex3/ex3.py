def intersection(arrays):
    index = {}
    result = []

    for a in arrays:
        for i in a:
            if i not in index:
                index[i] = 0
            else:
                index[i] = 1

    for k, v in index.items():
        if v == 1:
            result.append(k)
        else:
            pass

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
