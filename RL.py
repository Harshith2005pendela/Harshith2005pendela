import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def greedy(reward,distributions,num):
    max_index = np.argmax(np.array(reward))
    if(max_index==5):
         random_no=npr.choice([0,1,2,3,4])
         reward[5]+= (1/num[5])*(distributions[random_no]-reward[5]) 
         num[5]+=1
    else:
       reward[max_index] += (1/num[max_index])*(distributions[max_index]-reward[max_index])
       num[max_index]+=1  
def explore(reward,distributions,n):
    random = npr.choice([0,1,2,3,4,5])
    if(random==5):
        r=npr.choice([0,1,2,3,4])
        reward[5]+= (1/num[5])*(distributions[r]-reward[5])
        num[5]+=1
    else:
        reward[random] += (1/num[random])*(distributions[random]-reward[random])
        num[random]+=1
colors =['r','g','b']
epsilons=[0.1, 0.01, 0]
no_episodes =1000
for i, epsilon in enumerate(epsilons):
    reward = [0,0,0,0,0,0]
    num = [1,1,1,1,1,1]
    probabilities = [1-epsilon, epsilon]
    for episodes in range(1,no_episodes+1):
        for time in range(1,101):
            distributions = np.array([npr.normal(0,1),npr.choice([-4,3]),npr.poisson(2),npr.standard_exponential(),npr.normal(1,1.414)])
            action = npr.choice([0,1],p = probabilities)
            if(action == 0):
                greedy(reward,distributions,num)
            elif(action == 1):
                explore(reward,distributions,num)
        list = np.array([x - 1 for x in num])
        numpy_reward =np.array(reward)
        avg_reward = np.sum(numpy_reward*list)/np.sum(list)
        # Plot the total reward for the episode
        plt.plot(episodes, avg_reward,marker='o',color = colors[i])
legend_elements = [Line2D([0], [0], color=colors[i], lw=2, label=f'epsilon={epsilons[i]}') for i in range(len(epsilons))]
plt.legend(handles=legend_elements)
plt.xlabel('Episodes')
plt.ylabel('Average Reward')
plt.title('Average Reward vs Episodes for Different Epsilon Values')
plt.show()
    