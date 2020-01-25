import numpy as np
import sys

f_name = sys.argv[1]

with open(f_name) as f_input:
    list_data = f_input.read().split()

list_number = [int(num) for num in list_data]

print('{:.2f}'.format(np.percentile(list_number, 90)))
print('{:.2f}'.format(np.median(list_number)))
print('{:.2f}'.format(np.max(list_number)))
print('{:.2f}'.format(np.min(list_number)))
print('{:.2f}'.format(np.mean(list_number)))