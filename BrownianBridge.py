import numpy as np
import matplotlib.pyplot as plt
from random import normalvariate


def brownian_bridge(start, end, T, increment=0.1):
    """
    Produces a simulated path of a brownian bridge.
    :param start: B_0
    :param end: B_T
    :param T: defines interval 0 < t < T
    :param increment: 𝚫T
    :return: simulated brownian bridge path x_t on the interval 0 < t < T
    """
    x = [start]
    interval = np.linspace(0+increment, T, int(T//increment))
    for t in interval[:-1]:
        x_prev = x[-1]
        z_i = normalvariate(0, 1)
        x_t = x_prev + (end - x_prev) * increment/(T-t) + ((increment*(T-t-increment))/(T-t))**0.5 * z_i
        x.append(x_t)

    plt.plot(interval, x, label='Brownian Bridge')
    plt.plot(interval, [((end-start)/T)*y + start for y in interval], label='Expectation')
    plt.legend()
    plt.grid()
    plt.show()
    return x


if __name__ == '__main__':
    brownian_bridge(10, 50, 100)
