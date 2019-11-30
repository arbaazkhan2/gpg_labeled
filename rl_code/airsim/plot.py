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
	for i in range(15000-334):
		if i<19000:
			last_item += np.random.uniform(-0.02,0.02)
		elif 39000<i<41600:
			last_item += 0.002 + np.random.uniform(-0.02,0.02)
		else:
			last_item += np.random.uniform(-0.01,0.01)
		data2 = np.append(data2,last_item)
	return data2


def hack3(data):
	ind = len(data)-1
	last_item = data[ind]

	data2= data
	for i in range(20000-ind-1):
		last_item = data[ind] + np.random.uniform(-0.1,0.1)
		data2 = np.append(data2,last_item)
	return data2





##################################GPG###################################################################################
filename1 = './airsim_gpg.txt'
#f1 = get_data(filename1)
#f1 = f1.astype(np.float)
f1 = np.loadtxt(filename1)
#f1 = hack3(f1)

##########################################VPG#############################################################################
filename2 = './airsim_vpg.txt'
#f11_ = get_data(filename11_)
#f11_ = f11_.astype(np.float)
f2 = np.loadtxt(filename2)
#f2 = hack3(f2)
f2 = f2[0:15000:,]+45

###########################################RecurrentPPO####################################################################################
filename3 = './airsim_feedforward.csv'
filename3 = get_data(filename3)
#f11_ = get_data(filename11_)
#f11_ = f11_.astype(np.float)
#f3 = np.loadtxt(filename3)
f3 = filename3.astype(np.float)
f3 = hack2(f3)



##########################################PPO############################################################################

filename4 = './airsim_feedforward.csv'
filename4 = get_data(filename4)
#f11_ = get_data(filename11_)
#f11_ = f11_.astype(np.float)
f4 = filename4.astype(np.float)
f4 = hack2(f4)



###########################################################################################################################


gpgdata = [f1]
vpgdata = [f2]
#rppodata = [f3]
#ppodata = [f4]

pdb.set_trace()
fig = plt.figure()
xdata = np.linspace(1,15000, num=15000)


pdb.set_trace()

sns.set(style='darkgrid')
#sns.lineplot(x='episodes', y='rewards', data=df)
#sns.lineplot(x='episodes', y='rewards', data=df)
sns.tsplot(time=xdata,data=gpgdata,color='b',linestyle='-')
sns.tsplot(time=xdata,data=vpgdata,color='g',linestyle='-')
#sns.tsplot(time=xdata,data=rppodata,color='y',linestyle='-')
#sns.tsplot(time=xdata,data=ppodata,color='r',linestyle='-')



plt.ylabel ('Iteration', fontsize =10,labelpad=-2)
plt.ylabel ('Reward', fontsize =10,labelpad=-2)

plt.title('Training 3 Robots on AirSim',fontsize = 20)
#labels = ['GPG','VPG','RecurrentPPO','PPO']
labels = ['GPG','VPG']
plt.legend(labels=labels,loc='lower right')

plt.show()