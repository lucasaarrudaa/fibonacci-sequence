from math import sqrt
from time import sleep

class Fibonacci:

    @staticmethod
    def is_fibonacci_number(n):
        """
        Check if a number is in the Fibonacci sequence using the property that a number 'n' is in the Fibonacci
        sequence if and only if one or both of (5*n*n + 4) or (5*n*n - 4) is a perfect square.
        """
        def is_perfect_square(x):
            s = int(sqrt(x))
            return s * s == x

        return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def get_user_choice():
    """
    Ask the user if they want to check a number in the Fibonacci sequence.
    Limit the number of attempts to 3 for avoiding infinite loops.
    """
    attempts = 0
    while attempts < 3:
        user_choice = input("Do you want to check a number in the Fibonacci sequence? [Y/N]: ").strip().lower()
        if user_choice in ["y", "n"]:
            return user_choice
        else:
            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")
            attempts += 1
    return "n"

def get_number():
    """
    Get a number from the user to check in the Fibonacci sequence.
    Ensure the number is within a specified range.
    """
    while True:
        try:
            chosen_number = int(input("\nNumber to be checked: "))
            if not 0 <= chosen_number <= 10000000:
                raise ValueError("Number out of range. Please enter a number between 0 and 10,000,000.")
            return chosen_number
        except ValueError as e:
            print("Invalid value:", e)

def main():
    print("\nThe Fibonacci Sequence starts with 0 and 1, and the next value will always be the sum of the 2 previous values\n"
          "(example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)\n")

    while get_user_choice() == 'y':
        chosen_number = get_number()
        if Fibonacci.is_fibonacci_number(chosen_number):
            print(f"\nThe number {chosen_number} is in the Fibonacci sequence\n")
        else:
            print(f"\nThe number {chosen_number} is not in the Fibonacci sequence")
        sleep(1)

    print("Exiting program...")

if __name__ == '__main__':
    main()
