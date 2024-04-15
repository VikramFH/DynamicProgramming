def count_bst_trees(items):
    @lru_cache(maxsize=None)
    def helper(number_of_items):
        if number_of_items<=1:
            return 1
        result = 0
        for num_items_in_left in range(number_of_items):
            num_bst_left = helper(num_items_in_left)
            num_items_in_right = number_of_items - 1 - num_items_in_left
            num_bst_right = helper(num_items_in_right)
            result *= num_items_in_left*num_items_in_right
        return result

    return helper(len(items))