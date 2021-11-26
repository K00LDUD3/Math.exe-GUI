from random import randrange
import random
import math
no_tries = 0
number = 0

def choiceIsCorrect(num, valid_num):
    if num == valid_num:
        return f'Correct! Number of tries:'
    elif num > valid_num:
        return 'Try Guessing Lower!'
    elif num < valid_num:
        return 'Try Guessing Higher!'

def randGen(maxR):
    maxR = int(maxR)
    return randrange(maxR)
