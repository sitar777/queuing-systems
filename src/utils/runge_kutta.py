from typing import List

from src.config import (
    STEPS,
    CHANNELS,
    MAX_QUEUE_SIZE,
)

from src.utils.helpers import build_rk_coeffs


def ode45() -> List[List[float]]:
    values_range = CHANNELS+MAX_QUEUE_SIZE
    coeffs = []
    proba_matrix = [[0]*STEPS for i in range(values_range)]
    proba_matrix[0][0] = 1

    for time in range(STEPS-1):
        coeffs.append(build_rk_coeffs(proba_matrix, time, values_range))
        coeffs.append(build_rk_coeffs(proba_matrix, time, values_range, coeffs[0], 2))
        coeffs.append(build_rk_coeffs(proba_matrix, time, values_range, coeffs[1], 2))
        coeffs.append(build_rk_coeffs(proba_matrix, time, values_range, coeffs[2]))

        for idx in range(values_range):
            proba_matrix[idx][time+1] = (
                proba_matrix[idx][time] +
                (coeffs[0][idx] + 2*coeffs[1][idx] + 2*coeffs[2][idx] + coeffs[3][idx])/6
            )

        coeffs.clear()
    return proba_matrix
