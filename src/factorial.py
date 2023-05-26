import time


def factorial(number: int) -> int:
    """Find the factorial"""
    time.sleep(0.1)
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
    return fact


def sum_factorial(number: int) -> int:
    """Find the sum of all the numbers in te factorial
    I dont know, I just copied this from the internet to practice CI/CD on"""

    final_list = []

    for i in range(number):
        final_list.append(factorial(i))

    result = sum(final_list)
    print(f"Final__SUM = {result}")
    return result


if __name__ == "__main__":
    sum_factorial(3)
