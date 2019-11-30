1. nagent_goalreach has the main code. 
2. ./nagent_goalreach/logs has saved models
3. 2d_3agents is when the agents spit out deltax and deltay. The observations are relative positions to goals. 
4. 3agents is when the agents spit out delta_theta only (radial agents). The observations again were relative positions to goals. 
5. use ./nagent_goalreach/parameter_reload.py to run experiments for large number of agents. To do this first change the number of agents inside constr_formation_flying. Code for triangle goal patterns is in constr_formation_flying. 
6. Make sure the action space is right (if using radial agents). By default everything is setup for deltax, deltay case. 
7. ./nagent_goalreach/1ag has code for training just one agent. ./nagent_goalreach/1ag/parameter_reload.py loads this 1 agent model and uses it for all ten. 
8.  ./nagent_goalreach/10ag has results from training for 10 agents. This is pretty redundant if we can just train on 3 and transfer to 10. 
9. ./nagent_goalreach/3ag has results from training gcn for 3 agents. 

10. ./baseline has code and experiment results from runnning VPG and PPO on different configurations of robots. 