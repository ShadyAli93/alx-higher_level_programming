#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[-5:] > 5:
    print(f"Last digit of {number:d} and is greater than 5")
