from tkinter import YES
import numpy as np
def return_state_utility(v,T,u,reward,gamma):
    #four actions : up , left, right , down
    action_array = np.zeros(4)#initial values
    for action in range(0,4):
        action_array[action] = np.sum(np.multiply(u,np.dot(v,T[: , : , action])))
    return reward + gamma * np.max(action_array)
def main():
    #The agent starts from (1 , 1)
    v = np.array([[0.0 , 0.0 , 0.0 , 0.0 ,
                           0.0 , 0.0 , 0.0 , 0.0 ,
                           1.0 , 0.0, 0.0 , 0.0]])
    #Transition matrix to be loaded from file : T.npy
    T = np.load('T.npy')
    #Utility vector
    u = np.array([[0.812 , 0.868 , 0.918 , 1.0 ,
                          0.762 , 0.0 , 0.660 , -1.0 ,
                           0.705 , 0.655 , 0.611 , 0.388]])
    #Defining the reward for the state : (1 , 1)
    reward = -0.4
    gamma = 1.0
    utility_11 = return_state_utility(v,T,u,reward,gamma)
    print('Utility of the state (1 , 1) : '+ str(utility_11))
main()