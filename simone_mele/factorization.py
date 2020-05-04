# Scrivere un programma Python che dato un intero N, calcola e stampa
# il numero di primi minori di N ed accanto ad esso il valore di log(N) /N.


class Primes:
    __primes__ = [2, 3]

    def __init__(self):
        self.__index__ = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index__ == len(Primes.__primes__) - 1:
            # add next prime to list
            n = Primes.__primes__[-1] + 2
            while not Primes.__isPrime__(n):
                n += 2
            Primes.__primes__.append(n)

        self.__index__ += 1
        return Primes.__primes__[self.__index__]

    @staticmethod
    def __isPrime__(value, primes=__primes__):
        for prime in primes:
            if(value % prime == 0):
                return value == prime
        return True

    @staticmethod
    def isPrime(value):
        return Primes.__isPrime__(value, Primes())


def factorize(N):
    if(N == 1):
        return [(1, 1)]

    factors = []
    primes = iter(Primes())

    while N > 1:
        prime = next(primes)
        exp = 0
        while(N % prime == 0):
            N /= prime
            exp += 1
        if(exp > 0):
            factors.append((prime, exp))

    return factors


N = int(input('Insert integer: '))
if(N < 1):
    print('Integer must be greater than 1')
else:
    print('Factors of {0}: {1}'.format(N, factorize(N)))
