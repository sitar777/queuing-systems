from math import factorial

from src.config import (
    CHANNELS,
    RHO_SERVICE,
    NUMBER_OF_WORKERS,
)


def count_service_probabilities():
    P = []
    for idx in range(CHANNELS+1):
        if idx == 0:
            sum_1 = 0
            for j in range(1, NUMBER_OF_WORKERS+1):
                sum_1 += (RHO_SERVICE**j)/(factorial(CHANNELS-j)*factorial(j))

            sum_2 = 0
            for k in range(NUMBER_OF_WORKERS+1, CHANNELS+1):
                sum_2 += (RHO_SERVICE**k)/(factorial(CHANNELS-k) * (NUMBER_OF_WORKERS**(k-NUMBER_OF_WORKERS)))

            P.append(
                1/(1 + factorial(CHANNELS)*sum_1 + (factorial(CHANNELS)/factorial(NUMBER_OF_WORKERS))*sum_2)
            )

        elif idx <= NUMBER_OF_WORKERS:
            P.append(
                (factorial(CHANNELS)/(factorial(CHANNELS-idx)*factorial(idx)))*(RHO_SERVICE**idx) * P[0]
            )

        elif idx <= CHANNELS:
            P.append(
                (factorial(CHANNELS)/factorial(NUMBER_OF_WORKERS)) *
                (1/(factorial(CHANNELS-idx)*NUMBER_OF_WORKERS**(idx-NUMBER_OF_WORKERS))) * (RHO_SERVICE**idx) * P[0]
            )

    return P


def productivity_loss():
    service_probabilities = count_service_probabilities()

    average_occupied_workers = 0
    for idx in range(NUMBER_OF_WORKERS):
        average_occupied_workers += idx*service_probabilities[idx]

    queue_probas = 0
    for idx in range(NUMBER_OF_WORKERS, CHANNELS+1):
        queue_probas += NUMBER_OF_WORKERS * service_probabilities[idx]

    average_occupied_workers += queue_probas
    average_broken_channels = CHANNELS - average_occupied_workers/RHO_SERVICE
    return average_broken_channels/CHANNELS
