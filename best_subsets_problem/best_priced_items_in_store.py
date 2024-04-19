def get_top_items(items_price,limit):

    if limit >= items_price:
        return sum(items_price)

    start_range = limit
    end_range = 0
    total_sum = sum(items_price[0:start_range])
    highest_total = total_sum

    while end_range<=limit:
        start_range = start_range - 1
        end_range = end_range + 1
        total_sum = total_sum - items_price[start_range]
        total_sum = total_sum + items_price[-end_range]
        highest_total = max(total_sum,highest_total)

    return highest_total

