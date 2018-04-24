#!/usr/bin/python3

import hcf


def findLCM(arrNum):
    lcm = arrNum[0]
    for i in range(1, len(arrNum)):
        lcm = ((arrNum[i]*lcm)//hcf.getHCF2(arrNum[i], lcm))
    return lcm
