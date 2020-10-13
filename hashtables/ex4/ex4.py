def has_negatives(a):
    index = {}
    result = []

    for i in a:
        index[i] = i
        
    for i in index:
        # print(i, index[i])
        j = -i
        if j > 0 and j in index:
            result.append(j)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
