LAMBDA = 2
MU = 1
NU = 2

CHANNELS = 5
STEPS = 1000
MAX_QUEUE_SIZE = 3


def dp_idt(p, i, t):
    """Function retruning value of p_i-th derivative value at time t

    Args:
        p (list[list[int]]): p values matrix [CHANNELS + MAX_QUEUE_SIZE x STEPS]
        i (int): index
        t (int): time value

    Returns:
        float | None: function value
    """
    if i == 0:
        return -LAMBDA*p[0][t] + CHANNELS*MU*p[1][t]
    if i < CHANNELS:
        return LAMBDA*p[i-1][t] - (LAMBDA + CHANNELS*MU)*p[i] + CHANNELS*MU*p[i+1][t]
    if i < CHANNELS + MAX_QUEUE_SIZE:
        return LAMBDA*p[i-1][t] - (LAMBDA + CHANNELS*MU + (i-CHANNELS+1)*NU)*p[i]\
            + (CHANNELS*MU + (i-CHANNELS+1)*NU)*p[i][t]
    if i == CHANNELS + MAX_QUEUE_SIZE:
        return LAMBDA*p[i-1][t] - (CHANNELS*MU + MAX_QUEUE_SIZE*NU)*p[i][t]
    # if something went wrong
    return None
