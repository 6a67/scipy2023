def main():
    print("Factorial of 0:", factorial(0))
    print("Factorial of 1:", factorial(1))
    print("Factorial of 5:", factorial(5))
    print("Factorial of 10:", factorial(10))


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


if __name__ == "__main__":
    main()