"""
@file fibonacci_recursive.py
@brief Python program to generate Fibonacci series using recursion.
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print("--- Fibonacci Series (Recursive Method) ---")
    try:
        n = int(input("Enter the number of terms: "))
        if n <= 0:
            print("Error: Please enter a valid positive integer.")
        else:
            series = [fibonacci(i) for i in range(n)]
            print("Fibonacci Series:", *series)
    except ValueError:
        print("Error: Invalid input! Please enter an integer.")
