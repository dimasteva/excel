from typing import List
import sys
from structure import Cell

INT_MIN = -sys.maxsize - 1
INT_MAX = sys.maxsize

def SUM(cells: List[str]):
    #print(cells) #
    cells2 = [float(cell) for cell in cells]
    sum = 0
    for cell in cells2:
        sum += cell
    return sum

def AVERAGE(cells):
    cells2 = [float(cell) for cell in cells]
    return SUM(cells2) / len(cells2)

def MAX(cells):
    cells2 = [float(cell) for cell in cells]
    mx = INT_MIN
    for cell in cells2:
        mx = max(mx, cell)
    return mx

def MIN(cells):

    cells2 = [float(cell) for cell in cells]
    mn = INT_MAX
    for cell in cells2:
        mn = min(mn, cell)
    return mn

def PRODUCT(cells):
    cells2 = [float(cell) for cell in cells]
    product = 1
    for cell in cells2:
        product *= cell
    return product

def IF(condition, true_result, false_result):
    if eval(condition):
        return true_result
    else:
        return false_result

def AND(cells):
    if 'False' in cells:
        return False
    return True

def OR(cells):
    if 'True' in cells:
        return True
    return False

def NOT(arg):
    return not eval(arg)