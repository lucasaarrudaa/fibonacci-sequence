Find out whether or not the number you entered is in the fibonacci sequence, and its position.

## Description:
The code implements functionality that allows the user to check whether a given number belongs to the Fibonacci sequence. The Fibonacci sequence is a mathematical sequence in which each number is the sum of the two previous numbers. The sequence starts with 0 and 1, and the next numbers are 1, 2, 3, 5, 8, 13, 21, 34, and so on.

1. The execution starts with the printing of an explanatory text about the Fibonacci sequence and a request for the user to inform if he wants to verify if a number belongs to the sequence.

2. Next is a main loop that will continue to run until the user chooses to exit the program. If the user types "x" during the execution of the main loop, the program will exit immediately.

3. Inside the main loop is another loop that asks the user to enter a number that they want to check if it belongs to the Fibonacci sequence. The program validates that the number is within a given valid range and then uses two functions to generate the Fibonacci sequence and verify that the user-supplied number belongs to it.

4. If the number is in the Fibonacci sequence, the program displays a message informing the index of the number in the sequence and asks the user if he wants to check another number or exit the program.

5. If the number is not in the Fibonacci sequence, the program displays a message stating that the number does not belong to the sequence and asks the user if he wants to check another number or exit the program.

6. The program uses the "time" library to wait 1 second before printing the message to check for another number or exit the program so that the user has time to read the message.
