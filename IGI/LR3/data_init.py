from pydoc import render_doc

import input_check
import random

def init_with_zero_generator():
    '''
    Generator to initialize sequence until zero dont meet
    '''

    print('Enter number sequence (0 stop sequence)')
    while True:
        val = input_check.get_int_input('>')
        if val == 0:
            return
        yield val

def init_with_zero_user_variant():
    inp = []
    print('Enter number sequence (0 stop sequence)')
    while True:
        val = input_check.get_int_input('>')
        if val == 0:
            break
        inp.append(val)
    return inp

def init_float_generator(size, min_val = -100.0, max_val = 100.0):
    for _ in range(size):
        val = random.uniform(min_val, max_val)
        yield val

def init_float_by_user(size, min_val = -100.0, max_val = 100.0):
    inp = []
    print('Enter float number sequence')
    for _ in range(size):
        val = input_check.get_float_input(f"Element [{len(inp) + 1}]: ")
        inp.append(val)
    return inp