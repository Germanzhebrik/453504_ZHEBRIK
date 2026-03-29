"""
Task1 - get function value
Author: Zhebrik German
Date: 25-03-2026
"""

import input_check

def table_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 70)
        # ^10 означает выравнивание по центру в поле из 10 символов
        print(f"| {'x':^10} | {'n':^5} | {'F(x)':^12} | {'Math F(x)':^12} | {'eps':^10} |")
        print("-" * 70)

        # Вызов основной функции (calculate_taylor)
        result = func(*args, **kwargs)

        print("=" * 70)
        return result

    return wrapper


@table_decorator
def calculate_taylor(x, eps, max_iter=500):
    n = 0
    current_sum = 0.0
    term = 1.0  # Первый член ряда x^0 = 1

    while n < max_iter:
        current_sum += term
        n += 1

        term *= x

        if abs(term) < eps:
            math_f = 1 / (1 - x)
            print(f"| {x:10.4f} | {n:5} | {current_sum:12.6f} | {math_f:12.6f} | {eps:10.1e} |")
            return True

    print(f"\n Warning: Max iterations ({max_iter}) reached for x={x}.")
    return False

def main():
    print("Taylor Series Calculator (1/(1-x))")

    while True:
        x = input_check.get_float_input(
            "Enter x (must be -1 < x < 1): ",
            lambda val: abs(val) < 1
        )

        eps = input_check.get_float_input(
            "Enter precision eps : ",
            lambda e: e > 0
        )

        calculate_taylor(x, eps)

        if not input_check.ask_to_continue():
            break

main()