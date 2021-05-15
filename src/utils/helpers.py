from typing import List

from src.utils.equations import probability_derivative
from src.config import STEP_HEIGHT


def try_get_coeff(
    coeffs: List[float],
    idx: int,
        ) -> float:
    try:
        return coeffs[idx]
    except IndexError:
        return 0.


def validate_coeffs(
    coeffs: List[float] = None,
    idx: int = None,
    denominator: int = 1
        ) -> List[float]:
    if not coeffs:
        return [0, 0, 0]
    if idx is None:
        raise RuntimeError('idx should be provided if coeffs are not None')
    return [
        try_get_coeff(coeffs, idx-1)/denominator,
        try_get_coeff(coeffs, idx)/denominator,
        try_get_coeff(coeffs, idx+1)/denominator,
    ]


def build_rk_coeffs(
    proba_matrix: List[List[float]],
    time: int,
    values_range: int,
    coeffs: List[float] = None,
    denominator: int = 1
        ) -> List[float]:
    result = []
    for idx in range(values_range):
        result.append(
            STEP_HEIGHT*probability_derivative(
                proba_matrix,
                idx,
                time,
                validate_coeffs(coeffs, idx, denominator)
            )
        )
    return result
