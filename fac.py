def factorial_recur(n):
    if n == 0:
        return 1
    return n * factorial_recur(n - 1)


def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


while True:
    try:
        num = int(input("Enter the number to get its factorial: "))
        if num < 0:
            print("Factorial isn't defined for negative numbers.Try again.")
            continue
        method = int(input("Choose the method (1 for iterative, 2 for recursive): "))

        if method == 1:
            print(f"The factorial of {num} using the iterative method is: {factorial_iter(num)}")
        elif method == 2:
            print(f"The factorial of {num} using the recursive method is: {factorial_recur(num)}")
        else:
            print("Invalid. Please select 1 or 2.")

        again = input("Do you want to calculate another factorial? (yes/no): ").strip().lower()
        if again != 'yes':
            print("See in the next time.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
