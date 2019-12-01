## Graph Policy Gradients for Large Scale Robot Control
#### In CoRL 2019, Oral Paper [[Paper]](https://arxiv.org/pdf/1907.03822.pdf)[[Video]](https://www.youtube.com/watch?v=RefiX9UCCw8)[[Blog Post]](https://devmesh.intel.com/projects/graph-policy-gradients-for-large-scale-robot-control) [[CoRL Talk]](https://youtu.be/b7StSnt85S4?t=8604)

[Arbaaz Khan](https://www.seas.upenn.edu/~arbaazk/), [Ekaterina Tolstaya](https://katetolstaya.github.io/), [Alejandro Ribeiro](https://alliance.seas.upenn.edu/~aribeiro/wiki/), [Vijay Kumar](hhttps://www.kumarrobotics.org/dr-vijay-kumar/)<br/>
GRASP Lab, University of Pennsylvania <br/>

<img src="rl_code/results/gpg.png" width="300">  

This repository contains the code for our paper  Graph Policy Gradients for Large Scale Robot Control. The idea is to train a large number of agents by exploiting local structure using Graph Convolutional Networks. Training code as well as inference code is included in this implementation. 



### 1) Installation and Usage
1.  . To install, run these commands:
  
  # First install the formation flying environment from inside env/gym_formation. Instructions provided in the enclosed readme file.
  
  #Install deep graph library (https://www.dgl.ai/) and compatible version of PyTorch.

  # Running the code:

- If you wish to train GPG from scratch, run main.py. 
- If you wish to watch formations, run parameter_reload.py. parameter_reload.py loads model from ./logs. 

- A simple arrowhead formation is specified in constr_formation_flying.py (inside gym_formation/gym_flock/envs/)
To increase the number of agents simply change the parameter self.n_agents in constr_formation_flying.py, line 39.

  