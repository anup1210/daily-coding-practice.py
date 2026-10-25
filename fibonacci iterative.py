"""
@file fibonacci_iterative.py
@brief Python program to generate Fibonacci series using an iterative approach.
"""

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series

if __name__ == "__main__":
    print("--- Fibonacci Series (Iterative Method) ---")
    try:
        n = int(input("Enter the number of terms: "))
        if n <= 0:
            print("Error: Please enter a valid positive integer.")
        else:
            result = generate_fibonacci(n)
            print("Fibonacci Series:", *result)
    except ValueError:
        print("Error: Invalid input! Please enter an integer.")
