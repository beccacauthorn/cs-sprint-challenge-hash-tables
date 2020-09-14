def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # build dict with each number as key and a dummy value (eg True)
    d = {}
    for i in range(len(a)):
        if a[i] > 0:
            key = a[i]
        else:
            key = -a[i]

        if key not in d:
            d[key] = []

        if a[i] < 0:
            d[key].append("neg")
        else:
            d[key].append("pos")

    # iterate over the keys of the dict and keep the ones that
    # have "neg" and "pos"
    result = []
    for k in d:
        if len(d[k]) == 2:
            result.append(k)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
