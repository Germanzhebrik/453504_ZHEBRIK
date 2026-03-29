"""
Task1 - get sum and max of sequence
Author: Zhebrik German
Date: 25-03-2026
"""

import data_init

def task_2_business_logic(sequence):
    total_sum = 0
    max_val = None

    for num in sequence:
        total_sum += num
        if max_val is None or num > max_val:
            max_val = num

    return total_sum, max_val

def main():
    while True:
        seq = data_init.init_with_zero_generator()

        t = task_2_business_logic(seq)
        print(f"Max element is {t[1]}. Sum is {t[0]}")

main()