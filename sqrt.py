#!/usr/bin/env python

import math


def calc(num1, num2):
    num1 = math.sqrt(float(num1))
    print(float(num1))
    num3 = float(num1) * float(num2)
    num3 = round(float(num3), 2)
    return num3
