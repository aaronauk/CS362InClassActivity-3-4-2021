import sys

def fibonacci(num):
    if not isinstance(num, int):
        return None
    elif num < 0:
        return None
    elif num == 0 or num == 1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

def factorial(num):
    if not isinstance(num, int):
        return None
    elif num < 0:
        return None
    elif num == 0 or num == 1:
        return num
    else:
        fact_num = 1
        while (num > 0):
            fact_num = fact_num * num
            num = num - 1
    return fact_num

