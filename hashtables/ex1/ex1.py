def get_indices_of_item_weights(weights, length, limit):

    index = {}
    # it will iterate until we reach the length passed into the function.
    for i in range(length):
        # print(limit - weights[i])
        # print(limit, weights[i])
        # limit - weights[i] tells us how much must be added on top of the current
        # index to add up to our desired limit total.
        diff = limit - weights[i]
        if diff in index:
            # print("found! ",[i, index[limit - weights[i]]] )
            return [i, index[diff]]
        else:
            index[weights[i]] = i
            # print("NOT! ",  i)


    return None
                
# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))

# keys are weights, values are the weights' index on the array
# iterate over array to specified length
# check to see if the hash table contains an entry for `limit - weight`. 
# If it does, then return the values [index, limit-weight]

# this solution is O(n)
