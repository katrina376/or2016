import math
import numpy

class KnapsackDPResult(object): # save this in the KnapsackDP.py file
    def __init__(self, f, result):
        # instance variables
        self.f = f # optimal objective value
        self.result = result # optimal combination of goods in knapsack


def knapsackDP(C,W,V):
    # C is the capacity, which is a constant
    # W is the weight vector
    # V is the value vector

    # fill in the logic for Dynamic Programming here:
    # ...
    N = len(W)
    i_list = range(N)
    i_list.reverse()

    f = numpy.zeros((N + 1, C + 1)) # initial value = 0 for all
    m_logger = numpy.zeros((N, C + 1))

    for i in i_list:
        m_max = int(math.floor(C/W[i]))
        m_list = range(m_max + 1)
        x_list = range(C + 1)

        f_list = numpy.zeros((m_max + 1))

        for x in x_list:
            for m in m_list:
                if (x - W[i] * m >= 0):
                    f_list[m] = V[i] * m + f[i + 1, int(x - W[i] * m)]
                else:
                    f_list[m] = -numpy.inf
            m_logger[i,x] = numpy.argmax(f_list)
            f[i,x] = f_list[m_logger[i,x]]

    #optf is the optimal objective value
    #result stores the optimal combination of goods in knapsack
    optf = f[0, C]
    result = []

    remain = optf
    for i in range(N):
        for x in range(C + 1):
            if (f[i,x] == remain):
                result.append(int(m_logger[i,x]))
                remain -= V[i] * m_logger[i,x]
                break

    return KnapsackDPResult(optf, result)
