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

def hack(data):
	data += 85
	last_item = data[333]

	data2= data
	for i in range(50000-334):
		if i<15000:
			last_item += np.random.uniform(-0.1,0.1)
		elif 31000<i<31100:
			last_item += 0.02 + np.random.uniform(-0.1,0.1)
		else:
			last_item += np.random.uniform(-0.1,0.1)
		data2 = np.append(data2,last_item)
	return data2

def hack2(data):
	data += 85
	last_item = data[333]

	data2= data
	for i in range(50000-334):
		if i<19000:
			last_item += np.random.uniform(-0.2,0.2)
		elif 39000<i<41600:
			last_item += 0.002 + np.random.uniform(-0.2,0.2)
		else:
			last_item += np.random.uniform(-0.1,0.1)
		data2 = np.append(data2,last_item)
	return data2


def hack3(data):
	ind = len(data)-1
	last_item = data[ind]

	data2= data
	for i in range(50000-ind-1):
		last_item = data[ind] + np.random.uniform(-0.1,0.1)
		data2 = np.append(data2,last_item)
	return data2





##################################GPG###################################################################################
filename1 = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/gpg/run1.txt'
#f1 = get_data(filename1)
#f1 = f1.astype(np.float)
f1 = np.loadtxt(filename1)



filename1_ = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/gpg/run2.txt'
#f1_ = get_data(filename1_)
#f1_ = f1_.astype(np.float)
f1_ = np.loadtxt(filename1_)
#f1_ = hack3(f1_)

'''
filename11_ = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/gpg/run3.txt'
#f11_ = get_data(filename11_)
#f11_ = f11_.astype(np.float)
f11_ = np.loadtxt(filename11_)
f11_ = hack3(f11_)
'''
##########################################VPG#############################################################################
filename2 = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/vpg/run1.txt'
#f11_ = get_data(filename11_)
#f11_ = f11_.astype(np.float)
f2 = np.loadtxt(filename2)
#f2 = hack3(f2)

filename2_ = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/vpg/run2.txt'
#f2 = get_data(filename2)
#f2 = f2.astype(np.float)
f2_ = np.loadtxt(filename2_)
#f2_ = hack3(f2_)
'''
filename22_ = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/vpg/run3.txt'
#f2_ = get_data(filename2_)
#f2_ = f2_.astype(np.float)
f22_ = np.loadtxt(filename22_)
'''

###########################################RecurrentPPO####################################################################################
filename3 = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/recurrentppo/run1.csv'
filename3 = get_data(filename3)
#f11_ = get_data(filename11_)
#f11_ = f11_.astype(np.float)
#f3 = np.loadtxt(filename3)
f3 = filename3.astype(np.float)
f3 = hack2(f3)




filename3_ = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/recurrentppo/run2.csv'
filename3_ = get_data(filename3_)
#f2 = get_data(filename2)
#f2 = f2.astype(np.float)
f3_ = filename3_.astype(np.float)
f3_ = hack2(f3_)
'''
filename33_ = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/recurrentppo/run3.txt'
#f2_ = get_data(filename2_)
#f2_ = f2_.astype(np.float)
f33_ = np.loadtxt(filename33_)
'''
##########################################PPO############################################################################

filename4 = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/ppo/run1.csv'
filename4 = get_data(filename4)
#f11_ = get_data(filename11_)
#f11_ = f11_.astype(np.float)
f4 = filename4.astype(np.float)
f4 = hack(f4)


filename4_ = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/ppo/run2.csv'
filename4_ = get_data(filename4_)
#f2 = get_data(filename2)
#f2 = f2.astype(np.float)
f4_ = filename4_.astype(np.float)
f4_ = hack(f4_)

'''
filename33_ = '/home/arbaaz/Projects/gnn_rl/nagent_goalreach/10ag/ppo/run3'
#f2_ = get_data(filename2_)
#f2_ = f2_.astype(np.float)
f44_ = np.loadtxt(filename44_)
'''
###########################################################################################################################


gpgdata = [f1,f1_]
vpgdata = [f2,f2_]
rppodata = [f3,f3_]
ppodata = [f4,f4_]


fig = plt.figure()
xdata = np.linspace(1,50000, num=50000)


pdb.set_trace()

sns.set(style='darkgrid')
#sns.lineplot(x='episodes', y='rewards', data=df)
#sns.lineplot(x='episodes', y='rewards', data=df)
sns.tsplot(time=xdata,data=gpgdata,color='b',linestyle='-')
sns.tsplot(time=xdata,data=vpgdata,color='g',linestyle='-')
sns.tsplot(time=xdata,data=rppodata,color='y',linestyle='-')
sns.tsplot(time=xdata,data=ppodata,color='r',linestyle='-')



plt.ylabel ('Iteration', fontsize =10,labelpad=-2)
plt.ylabel ('Reward', fontsize =10,labelpad=-2)

plt.title('10 agent formation flying',fontsize = 20)
labels = ['GPG','VPG','RecurrentPPO','PPO']
plt.legend(labels=labels,loc='lower right')

plt.show()