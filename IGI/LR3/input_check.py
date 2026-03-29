def get_float_input(prompt, validator=None):
    """
    Generic function to get a valid float with optional validation.
    Protects against ValueError and logic errors.
    """
    while True:
        try:
            val = float(input(prompt))
            if validator is None or validator(val):
                return val
            print("Error: Input value is out of range.")
        except ValueError:
            print("Error: Please enter a numeric value (e.g., 0.5).")

def ask_to_continue():
    """Asks the user if they want to run the program again."""
    choice = input("\nDo you want to calculate for another x? (y/n): ").lower()
    return choice == 'y'

def get_int_input(prompt, validator=None):
    while True:
        try:
            val = int(input(prompt))
            if validator is None or validator(val):
                return val
        except ValueError:
            print("Incorrect input.")
