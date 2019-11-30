import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import csv 

import numpy as np
import pdb
import pandas as pd 
import pdb

def get_data(filename_arg):
	f = open(filename_arg, 'r')
	reader = csv.reader(f)
	reader = list(reader)

	reader_arr = np.asarray(reader)
	reader_arr = reader_arr[:,2]
	return reader_arr[1:]

a = './run1.csv'
b = get_data(a)
pdb.set_trace()
np.savetxt('run1.txt',b)

pdb.set_trace()