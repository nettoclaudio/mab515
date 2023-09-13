#!/usr/bin/env python3

import random

def flip_coin() -> str:
    return random.choice(['H', 'T'])

def trials_until_two_consecutive_coins(expected: str = 'H') -> int:
    flips:    int = 0
    previous: str = None

    while True:
        current = flip_coin()
        flips += 1

        if current == expected and current == previous:
            return flips

        previous = current

def mean(numbers: [int]) -> float:
    return sum(numbers) / len(numbers)

def variance(numbers: [int]) -> float:
    _mean: [int] = mean(numbers)

    return sum(map(lambda x: (x - _mean) ** 2, numbers)) / len(numbers)

def main() -> None:
    N: int = 10 ** 6 # one million

    trials: [int] = [trials_until_two_consecutive_coins() for i in range(0, N)]

    print('Number of samples: ', len(trials))
    print('Mean: ', mean(trials))
    print('Variance: ', variance(trials))

if __name__ == '__main__':
    main()
