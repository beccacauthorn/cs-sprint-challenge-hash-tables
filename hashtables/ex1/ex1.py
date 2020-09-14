def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # build the dict with weights as keys and list indices as values
    d = {}
    for i in range(len(weights)):
        # d[weights[i]] = i
        if weights[i] not in d:
            d[weights[i]] = []
        d[weights[i]].append(i)

    # iterate over the keys of the dict and try to find the complementary
    for i in range(len(weights)):
        w = weights[i]
        complementary_weight = limit - w
        
        if complementary_weight in d:
            complementary_index = max(d[complementary_weight])

            if complementary_index > i:
                return complementary_index, i
            else:
                return i, complementary_index

    return None
