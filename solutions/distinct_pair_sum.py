def distinct_pair_sum(nums, k):

    pairs = {}

    for i in range(len(nums) - 1):
        if nums[i] + nums[i + 1] == k:
            if nums[i] not in pairs and nums[i + 1] not in pairs:
                pairs[nums[i]] = [nums[i], nums[i + 1]]

    return list(pairs.values())

if __name__ == "__main__":
    # add your own tests here
    print("Expecting: [[1, 1], [2, 0]]")
    print(distinct_pair_sum([0, 1, 1, 2, 0, 1, 1], 2))

    print("")

    print("Expecting: [[2, 8]]")
    print(distinct_pair_sum([3, 4, 2, 1, 5, 2, 8, 2], 10))

    print("")

    print("Expecting: []")
    print(distinct_pair_sum([3, 4, 2, 1, 5, 2, 8, 2], 100))

    print("")

    print("Expecting: []")
    print(distinct_pair_sum([], 100))

    print("")

    print("Expecting: [[59, 41]]")
    print(distinct_pair_sum([59, 41], 100))

    print("")

    print("Expecting: []")
    print(distinct_pair_sum([59], 100))

    print("")

    print("Expecting: [[0, 0], [10, -10], [3, -3]]")
    print(distinct_pair_sum([1, 0, 0, 10, -10, 5, 4, 3, -3, -3], 0))

# Please add your pseudocode to this file
##########################################################################################
 # initialize empty object called pairs
 # 
 # iterate over array up to second to last item:
 #  if current item and next item are not keys in pairs and they sum to k:
 #    add current item as key in pairs with value of [current item, next item]
 # 
 # return values stored in pairs
##########################################################################################

# And a written explanation of your solution
##########################################################################################
 # Objects only allow keys with unique values. If we iterate over the array, and on 
 # each iteration, check if the current value and next value add up to k, we can then
 # check if either of those values is a key in pairs. If neither is a key in pairs, we
 # add the current element being iterated over as the key and the pair as the value. 
 # When the iteration is over, we just return the values from pairs.
##########################################################################################