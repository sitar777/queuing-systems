from typing import List

LAMBDA = 2
MU = 1
NU = 2

CHANNELS = 5
STEPS = 1000
MAX_QUEUE_SIZE = 3


def probability_deriavative(
    proba_matrix: List[List[float]],
    idx: int,
    time: int,
    rk_coeffs: List[float] = [0, 0, 0]
        ):
    """Function retruning value of p_i-th derivative value at time t

    Args:
        proba_matrix (list[list[float]]): p values matrix [CHANNELS + MAX_QUEUE_SIZE x STEPS]
        idx (int): index
        time (int): time value
        rk_coeffs (list[float]): Runge Kutta's method coeffs

    Returns:
        float | None: function value
    """
    if idx == 0:
        return (
            - LAMBDA*(proba_matrix[0][time]+rk_coeffs[0])
            + CHANNELS*MU*(proba_matrix[1][time]+rk_coeffs[1])
        )
    if idx < CHANNELS:
        return (
            LAMBDA*(proba_matrix[idx-1][time]+rk_coeffs[0])
            - (LAMBDA + CHANNELS*MU)*(proba_matrix[idx]+rk_coeffs[1])
            + CHANNELS*MU*(proba_matrix[idx+1][time]+rk_coeffs[2])
        )
    if idx < CHANNELS + MAX_QUEUE_SIZE:

        return (
            LAMBDA*(proba_matrix[idx-1][time]+rk_coeffs[0])
            - (LAMBDA + CHANNELS*MU + (idx-CHANNELS)*NU)*(proba_matrix[idx]+rk_coeffs[1])
            + (CHANNELS*MU + (idx-CHANNELS+1)*NU)*(proba_matrix[idx][time]+rk_coeffs[2])
        )
    if idx == CHANNELS + MAX_QUEUE_SIZE:
        return (
            LAMBDA*(proba_matrix[idx-1][time]+rk_coeffs[1])
            - (CHANNELS*MU + MAX_QUEUE_SIZE*NU)*(proba_matrix[idx][time]+rk_coeffs[2])
        )
    # if something went wrong
    return None
