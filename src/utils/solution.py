from typing import Union
from math import factorial

from src.config import (
    CHANNELS,
    MU,
    LAMBDA,
    NU,
    MAX_QUEUE_SIZE,
)


def solution_numerator(idx: int) -> Union[float, None]:
    if idx == 0:
        return 1
    if idx <= CHANNELS:
        return (LAMBDA**idx)/(factorial(idx)*(MU**idx))
    if idx <= CHANNELS+MAX_QUEUE_SIZE:
        top_numerator = LAMBDA**(CHANNELS+idx)

        top_denominator_product = 1
        for j in range(1, idx+1):
            top_denominator_product *= CHANNELS*MU + j*NU

        top_denominator = factorial(CHANNELS)*(MU**CHANNELS)*top_denominator_product
        return top_numerator/top_denominator
    # if something went wrong
    return None


def solution_denominator() -> float:
    denominator_sum_1 = 0
    for j in range(CHANNELS+1):
        denominator_sum_1 += (LAMBDA*j)/(factorial(j)*(MU**j))

    denominator_sum_2 = 0
    for k in range(1, MAX_QUEUE_SIZE+1):
        denominator_sum_2_numerator = LAMBDA**(CHANNELS+k)

        denominator_sum_2_denominator_product = 1
        for j in range(1, k+1):
            denominator_sum_2_denominator_product *= CHANNELS*MU + j*NU

        denominator_sum_2_denominator = factorial(CHANNELS) * (MU**CHANNELS) * denominator_sum_2_denominator_product

        denominator_sum_2 += denominator_sum_2_numerator/denominator_sum_2_denominator

    return denominator_sum_1 + denominator_sum_2


def solution(idx: int) -> float:
    return solution_numerator(idx)/solution_denominator()
