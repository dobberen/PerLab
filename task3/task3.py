import numpy as np
import sys

f_name = sys.argv[1]

cash1 = np.loadtxt(f_name + 'Cash1.txt')
cash2 = np.loadtxt(f_name + 'Cash2.txt')
cash3 = np.loadtxt(f_name + 'Cash3.txt')
cash4 = np.loadtxt(f_name + 'Cash4.txt')
cash5 = np.loadtxt(f_name + 'Cash5.txt')

sum_cash = cash1 + cash2 + cash3 + cash4 + cash5

print(sum_cash.argmax() + 1)