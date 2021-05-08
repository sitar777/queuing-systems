from src.utils.equations import probability_derivative
from src.config import STEP_HEIGHT


def try_get_coeff(coeffs, idx):
    try:
        return coeffs[idx]
    except IndexError:
        return 0


def validate_coeffs(coeffs=None, idx=None, denominator=1):
    if not coeffs:
        return [0, 0, 0]
    if idx is None:
        raise RuntimeError('idx should be provided if coeffs are not None')
    return [
        try_get_coeff(coeffs, idx-1)/denominator,
        try_get_coeff(coeffs, idx)/denominator,
        try_get_coeff(coeffs, idx+1)/denominator,
    ]


def build_rk_coeffs(proba_matrix, time, values_range, coeffs=None, denominator=1):
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