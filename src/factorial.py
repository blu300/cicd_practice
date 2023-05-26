import time

final_list = []


def factorial(number: int) -> int:
    time.sleep(0.1)
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial


def sum_factorial(number: int) -> int:
    for i in range(number):
        final_list.append(factorial(i))

    result = sum(final_list)

    print(f"Final__SUM = {result}")

    return result


if __name__ == "__main__":
    sum_factorial(3)
