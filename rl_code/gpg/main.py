import gym
import gym_flock
import numpy as np
import pdb
import dgl
import torch.nn as nn
import torch.nn.functional as F
import torch as t
from make_g import build_graph
import torch.optim as optim
import dgl
import dgl.function as fn
import math
import pdb

from torch.autograd import Variable
from torch.distributions import Categorical
import torch
import networkx as nx
import pdb
import matplotlib.pyplot as plt
from policy import Net
#from linear_policy import Net
from make_g import build_graph
from utils import *

import os
import datetime

policy = Net()
optimizer = optim.Adam(policy.parameters(), lr=1e-3)
env = gym.make('FormationFlying-v3')

if not os.path.exists('./logs'):
	os.makedirs('./logs')

filename = str(datetime.datetime.now())+str('_%dagents_fixed_fcnpolicy'%env.n_agents)
filename = filename+str('.pt')
torch.save(policy.state_dict(),'./logs/%s'%filename)

def main(episodes):
	running_reward = 10
	plotting_rew = []

	for episode in range(episodes):
		reward_over_eps = []
		state = env.reset() # Reset environment and record the starting state
		g = build_graph(env)
		done = False

		for time in range(200):

			#if episode%50==0:
			#	env.render()
			#g = build_graph(env)
			action = select_action(state,g,policy)

			action = action.numpy()
			action = np.reshape(action,[-1])

			# Step through environment using chosen action
			action = np.clip(action,-env.max_accel,env.max_accel)

			state, reward, done, _ = env.step(action)

			reward_over_eps.append(reward)
			# Save reward
			policy.reward_episode.append(reward)
			if done:
				break

		# Used to determine when the environment is solved.
		running_reward = (running_reward * 0.99) + (time * 0.01)

		update_policy(policy,optimizer)

		if episode % 50 == 0:
			print('Episode {}\tLast length: {:5d}\tAverage running reward: {:.2f}\tAverage reward over episode: {:.2f}'.format(episode, time, running_reward, np.mean(reward_over_eps)))

		if episode % 5000 == 0 :
			torch.save(policy.state_dict(),'./logs/%s'%filename)


		plotting_rew.append(np.mean(reward_over_eps))
	#pdb.set_trace()
	np.savetxt('Relative_Goal_Reaching_for_%d_agents_rs_rg.txt' %(env.n_agents), plotting_rew)
	fig = plt.figure()
	x = np.linspace(0,len(plotting_rew),len(plotting_rew))
	plt.plot(x,plotting_rew)
	plt.savefig('Relative_Goal_Reaching_for_%d_agents_rs_rg.png' %(env.n_agents))
	plt.show()

	#pdb.set_trace()

episodes = 50000
main(episodes)











#pdb.set_trace()
