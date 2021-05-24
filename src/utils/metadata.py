from src.config import (
    CHANNELS,
    MU,
    LAMBDA,
    NU,
    MAX_QUEUE_SIZE,
    RHO
)

from src.utils.solution import solution
from src.utils.service import productivity_loss


def print_metadata():
    print('Reduced demand flow rate: ', RHO)

    # TODO make sure that t_och is calculated in a right way
    t_och = 1/NU
    print('Average time of demand in the queue: ', t_och)

    l_och = 0
    for i in range(CHANNELS+1, MAX_QUEUE_SIZE):
        l_och += i*solution(CHANNELS+i)
    print('Average number of demands in the queue: ', l_och)

    print('The rate of withdrawal of claims from the queuing system without service: ', NU)

    A = LAMBDA - NU * l_och
    print('Absolute throughput of the queuing system: ', A)

    Q = A/LAMBDA
    print('Relative throughput of the queuing system: ', Q)

    n_zan = A/MU
    print('Average number of busy channels: ', n_zan)

    print('Productivity loss due to breakage: ', productivity_loss())
