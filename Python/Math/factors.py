#!/usr/bin/python3

import math


def primeFactors(num):
    facts = []
    while num % 2 == 0:
        facts.append(2)
        num /= 2
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num % i == 0:
            facts.append(i)
            num /= i
    if num>2:
        facts.append(num)
    return facts
