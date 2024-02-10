#Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор.
#Також потрібно реалізувати функцію sum_profit, яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.

import re
from typing import Callable

def generator_numbers(text: str):
    """Arg.: some text. Generates numeric values from text"""
    for element in text.split(" "):
        if re.search(r"\d+\.{0,1}\d+", element):
            yield float(element)

def sum_profit(text: str, func: Callable[[str], float]) -> float:
    """Args.: some text, function -> generator. Returns sum of values from list created by generator from text"""
    return sum(list(generator_numbers(text)))

# Check results
# text="Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# gen=generator_numbers(text)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(sum_profit(text, gen))

# text="Загальний дохід працівника складається з декількох частин: 1000 як основний дохід, доповнений додатковими надходженнями 2745 і 324.00 доларів."
# gen=generator_numbers(text)
# print(sum_profit(text, gen))

# text="Загальний дохід працівника складається з декількох частин: x як основний дохід, доповнений додатковими надходженнями x і x доларів."
# gen=generator_numbers(text)
# print(list(gen))
# print(sum_profit(text, gen))