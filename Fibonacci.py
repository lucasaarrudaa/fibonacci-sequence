from time import sleep

class Fibonacci:
    
    def init(self):
        self.fibo_list = []
        
    def fibo(self, n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return self.fibo(n - 1) + self.fibo(n - 2)

def limit(self, chosen_number):
    n = 1
    while self.fibo(n) <= chosen_number:
        self.fibo_list.append(self.fibo(n))
        n += 1

def check_number(self, chosen_number):
    self.fibo_list = []
    self.limit(chosen_number)

    if chosen_number in self.fibo_list:
        index_list = [n for n, x in enumerate(self.fibo_list) if x == chosen_number]
        index = int(index_list[0] + 1)
        print(f"\nThe number {chosen_number} is in the Fibonacci sequence, and it's the {index}th number\n")
        sleep(1)
        continue_request = input(str("\nIf you want to check another number, enter [Y]\n"
                                      "if you want to stop, enter [X]\n").strip().lower())
        if continue_request == "x":
            print("Closing the Program...")
            exit()
    else:
        print(f"\nThe number {chosen_number} is not in the Fibonacci sequence")
        sleep(1)
        continue_request = input(str("\nIf you want to check another number, enter [Y]\n"
                                      "if you want to stop, enter [X]\n").strip().lower())
        if continue_request == "x":
            print("Closing the Program...")
            exit()
            
if __name__ == '__main__':
    
    fibo = Fibonacci()
    print("\nThe Fibonacci Sequence starts with 0 and 1, and the next value will always be the sum of the 2 previous values\n"
          "(example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)\n")
    print("Do you want to find out if a number belongs to the sequence?\n"
          "\nIf yes, enter [Y]\n"
          "If you want to exit, enter [X]")

    while True:
        user_choice = input().strip().lower()

        if user_choice == "x":
            break

        while True:
            chosen_number = 0

            while True:
                try:
                    chosen_number = int(input("\nNumber to be checked: "))
                    if not 0 <= chosen_number <= 500000:
                        raise ValueError("Please enter a number smaller than 500000?")
                except ValueError as e:
                    print("Invalid value:", e)
                else:
                    break

            fibo.check_number(chosen_number)
