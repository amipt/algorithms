#!/usr/bin/python3


def getHCF2(a, b):
    while(b):
        a, b = b, a % b
    return a


def findHCF(arrNum):
    hcf = arrNum[0]
    for i in range(1, len(arrNum)):
        hcf = getHCF2(hcf, arrNum[i])
    return hcf
