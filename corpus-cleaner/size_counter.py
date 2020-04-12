def size_counter_before(*args):
    summed_items = 0
    for items in args:
        for item in items:
            summed_items += item
    return summed_items

def size_counter_after(*args):
    summed_items = 0
    for items in args:
        for item in items:
            summed_items += item
    return summed_items


corpora_size_before_clean = (2699, 18179, 33781, 10082, 7594, 5642, 5988, 9760, 49110, 8041)
corpora_size_after_clean = (1211, 18173, 33776, 3523, 2846, 1434, 1269, 1549, 26680, 2936)

print(f"Tamanho pré-limpeza: {size_counter_before(corpora_size_before_clean)}")
print(f"Tamanho pós-limpeza: {size_counter_after(corpora_size_after_clean)}")