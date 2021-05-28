# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:44:24 2021

@author: AADITYA RAJ BARNWAL

"""

import random
import numpy as np


def get_sensor_value(state):
    sensor=[] #it contains the distance from north,south,east,west
    if state==1:
        
        sensor.append(1)
        sensor.append(0)
        sensor.append(0)
        sensor.append(0)
        
    elif state==2:
        sensor.append(0)
        sensor.append(1)
        sensor.append(2)
        sensor.append(0)
        
    elif state==3:
        sensor.append(0)
        sensor.append(1)
        sensor.append(1)
        sensor.append(1)
        
    elif state==4:
        sensor.append(0)
        sensor.append(1)
        sensor.append(0)
        sensor.append(2)
        
    elif state==5:
        sensor.append(1)
        sensor.append(0)
        sensor.append(0)
        sensor.append(0)
        
    else :
        sensor.append(1)
        sensor.append(0)
        sensor.append(0)
        sensor.append(0)
    return sensor


def generate_random_sensor(): # for generating the discreipencies
    
    sensor=[]
    sensor.append(random.randint(0,4))
    sensor.append(random.randint(0,4))
    sensor.append(random.randint(0,4))
    sensor.append(random.randint(0,4))
    return sensor

def make_action(state): # for robot to move_based on sensor value
    if state==1:
        return 2
    if state==2:
        a=[1,3]
        return select_one_from(a)
    if state==3:
        a=[6,2,4]
        return select_one_from(a)
    if state==4:
        a=[5,3]
        return select_one_from(a)
    if state==5:
        return 4
    if state==6:
        return 3

def select_one_from(a):  # just a random type function
    r=random.randint(0, len(a)-1)   
    return a[r]

          
def myfunction(obs)    : # it return the maximum probailty  of having in that state and return the same      
 index=1
 prob=obs[0]
 for i in range(len(obs)) :
     if prob<obs[i]:
         prob=obs[i]
         index=i+1
 return index,prob

def find_the_discrepencies(sensor1,sensor2):  # this function is for finding the number of discrepencies in reading
    sensor3=[]
    for i in range(4):
            if sensor1[i]==sensor2[i]:
                sensor3.append(0)
            else:
                sensor3.append(np.abs(sensor1[i]-sensor2[i]))
    sensor3.append(random.randint(0, 4))
    sensor3.append(random.randint(0, 4))
    return sensor3
class Hidden_Markov_Model:  # this class contains various method to evalauet the location of robot
    
    def __init__(self, transition_matrix,current_state): # the transition matrix is given to us
             self.transition_matrix = transition_matrix
             # the current stae of the environemtn is 1/6 0.1667
             self.current_state = current_state
    
    def filtering_method(self,observation_matrix):
        new_state = np.dot(observation_matrix,np.dot(self.transition_matrix,self.current_state))
        
        new_state_normalized = new_state/np.sum(new_state)
        self.current_state = new_state_normalized
        return new_state_normalized
    
    def create_observation_matrix_(self,error_rate, no_discrepancies):
        sensor_list=[]
        for number in no_discrepancies:
            probability=(1-error_rate)**(4-number)*error_rate**number # this is as per the formula in the report given(pdf attached)
            sensor_list.append(probability)
            observation_matrix = np.zeros((len(sensor_list),len(sensor_list)))
            np.fill_diagonal(observation_matrix,sensor_list)
        return observation_matrix # it return the obervation matrix
    
    
if __name__ == "__main__":
    
    
    state=random.randint(1,6)
    transistion_matrix=[    # givenr in question
                        [0.2,0.8,0,0,0,0],
                        [0.4,0.2,0.4,0,0,0],
                        [0,0.27,0.2,0.27,0,0.27],
                        [0,0,0.4,0.2,0.27,0.0],
                        [0,0,0,0.8,0.2,0],
                        [0,0,0.8,0,0,0.2]]
    error=25
    initial_state=[0.1667,0.1667,.1667,.1667,.1667,.1667]  # as its 1/6
    current_state=initial_state
    
    prev_state=state
    transistion_matrix2=np.transpose(transistion_matrix)
    
   
    for i in range (100):
        Model = Hidden_Markov_Model(transistion_matrix, current_state)
        curr_sensor_data=get_sensor_value(state)
        no_of_discrepencies=find_the_discrepencies(curr_sensor_data, generate_random_sensor())
        
        obs=Model.create_observation_matrix_(0.25, no_of_discrepencies)
        obs=Model.filtering_method(obs) # filtering everytime 
        
        
        
        index,prob=myfunction(obs)
        if i %10==0:
         print("State is ",index,"With a Probability of ",prob)
        current_state[index-1]*=prob
        state=make_action(state)
        
        if random.randint(1, 100)<80:
            state=random.randint(1, 6)
            current_state=initial_state
        
        
        
    
    
    
    
    