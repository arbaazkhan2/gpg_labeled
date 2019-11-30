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




##################################GPG###################################################################################
filename1 = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/dynagraph/dynagraph10ag.txt'
#f1 = get_data(filename1)
#f1 = f1.astype(np.float)
f1 = np.loadtxt(filename1)




##########################################VPG#############################################################################
filename2 = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/dynagraph/staticgraph.txt'
#f11_ = get_data(filename11_)
#f11_ = f11_.astype(np.float)
f2 = np.loadtxt(filename2)
#f2 = hack3(f2)


###########################################################################################################################


dgpgdata = [f1]
sgpgdata = [f2]


fig = plt.figure()
xdata = np.linspace(1,50000, num=50000)


pdb.set_trace()

sns.set(style='darkgrid')
#sns.lineplot(x='episodes', y='rewards', data=df)
#sns.lineplot(x='episodes', y='rewards', data=df)
sns.tsplot(time=xdata,data=dgpgdata,color='b',linestyle='-')
sns.tsplot(time=xdata,data=sgpgdata,color='g',linestyle='-')
#sns.tsplot(time=xdata,data=rppodata,color='y',linestyle='-')
#sns.tsplot(time=xdata,data=ppodata,color='r',linestyle='-')



plt.ylabel ('Iteration', fontsize =10,labelpad=-2)
plt.ylabel ('Reward', fontsize =10,labelpad=-2)

plt.title('Static vs Dynamic Graph Policy Gradients',fontsize = 20)
labels = ['Dynamic GPG','Static GPG']
plt.legend(labels=labels,loc='lower right')

plt.show()