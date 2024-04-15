
def max_prod_array(nums):



    def helper(nums):
        product = 1
        max_product = 0
        for num in nums:
            if not product:
                product = num
            else:
                product=product*num
            max_product = max(product,max_product)
        return max_product

    return max(helper(nums),helper(nums[::-1]))
