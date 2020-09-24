# 1. Import object data to a list
# 2. Create nested list of objects
# 3. Sort based of on first(title) or on last(current value) index
# 4. Return data. Not yet sure in what format


def indexing(data, order):
    if order == 'title':
        index_order = 0
    elif order == 'price':
        index_order = -1
    sorted_data = sorted(data, key=lambda x: x[index_order])
    return sorted_data
