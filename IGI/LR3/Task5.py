import data_init


def analyze_positive_elements(data):
    """
    Can work with generator and list
    """
    min_pos = None
    first_idx = -1
    last_idx = -1
    total_between_sum = 0

    # Временный список, если нам нужно считать сумму "между"
    # Для генератора нам все равно придется где-то хранить значения,
    # чтобы вычислить сумму после того, как узнаем, где был ПОСЛЕДНИЙ элемент.
    items = list(data)

    if not items:
        return None, 0

    #min positive
    positives = [x for x in items if x > 0]
    if positives:
        min_pos = min(positives)

    #Find range to sum
    for i, val in enumerate(items):
        if val > 0:
            if first_idx == -1:
                first_idx = i
            last_idx = i

    #Sum
    if first_idx != -1 and last_idx != -1 and last_idx > first_idx + 1:
        total_between_sum = sum(items[first_idx + 1: last_idx])

    return min_pos, total_between_sum

def main():
    n = int(input('Enter sequence size : '))
    data = data_init.init_float_generator(n)
    tup = analyze_positive_elements(data)
    print(f"Min pos : {tup[0]}. Between sum : {tup[1]}")

main()