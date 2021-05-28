# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:16:06 2021

@author: AADITYA RAJ BARNWAL

"""

import numpy as np
import random
import math
REWARD = 0 # constant reward for non-terminal states
DISCOUNT = 0.85  #given this question
MAX_ERROR = 10**(-3) # ASSUMPTION

NUM_ROW = 5
NUM_COL = 5

c1=[3,4] # uses 0 based indexing
c2=[0,0]
magneto=[2,1]
wolverine=[0,2]
jean_pos=[0,0]





NUM_ACTIONS = 4 # no. of action for all except jean

ACTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)] # Down, Left, Up, Right

def check_for_up_movement(x,y): # this function return true if upward movement is valid for magneto
    if x==2 and y==3:
        return False
    if x<0:
        return False
    if x==0 and y==4:
        return False
    return True



    

def getOptimalPolicy(U):
    policy = [[-1, -1, -1, -1 ,-1 ] for i in range(NUM_ROW)]
    
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            if (r ==magneto[0] and c == magneto[1]) or (r == 2 and c == 3) or (r==jean_pos[0] and c==jean_pos[1]):
                continue
            # Choose the action that maximizes the utility
            maxAction, maxU = None, -float("inf")
            for action in range(NUM_ACTIONS):
                u = calculateU(U, r, c, action)
                if u > maxU:
                    maxAction, maxU = action, u
            policy[r][c] = maxAction
    return policy

def check_for_down_movement(x,y): # this function return true if down movement is valid for magneto
    if x==2 and y==3:
        return False
    if x>=NUM_ROW:
        return False
    if x==0 and y==4:
        return False
    return True

def check_for_left_movement(x,y): # this function return true if left movement is valid for magneto
    if x==2 and y==3:
        return False
    if y<0:
        return False
    if x==0 and y==4:
        return False
    return True

def check_for_right_movement(x,y): # this function return true if right movement is valid for magneto
    if x==2 and y==3:
        return False
    if y>=NUM_COL:
        return False
    if x==0 and y==4:
        return False
    return True

def update_u():  # this function update the value of utlity function as position of magneto and jean is always changing
    
    U=np.zeros([5, 5], dtype = int) 
    U[magneto[0]][magneto[1]]=-20
    U[jean_pos[0]][jean_pos[1]]=+20
    return U

def switch_jean_pos():  # this is for changing jean position
    x=jean_pos[0]
    y=jean_pos[1]
    if x==3 and y==4:
        jean_pos[0]=jean_pos[1]=0
    else:
        jean_pos[0]=3
        jean_pos[1]=4

def move_magneto_in_direction_of_wolverine():  # this is for moving magneto in the direction of wolverine so that it minize the distance between the two
   w_x=wolverine[0]
   w_y=wolverine[1]
   m_x=magneto[0]
   m_y=magneto[1]
   
  
   
   up_dir=math.dist([w_x,w_y],[m_x-1,m_y]) if  check_for_up_movement(m_x-1, m_y) else 147483647
   down_dir=math.dist([w_x,w_y],[m_x+1,m_y]) if  check_for_down_movement(m_x+1, m_y) else 147483647
   right_dir=math.dist([w_x,w_y],[m_x,m_y+1]) if  check_for_right_movement(m_x, m_y+1) else 147483647
   left_dir=math.dist([w_x,w_y],[m_x,m_y-1]) if  check_for_left_movement(m_x, m_y-1) else 147483647
   m=[]
   m.append(up_dir)
   m.append(down_dir)
   m.append(right_dir)
   m.append(left_dir)
   
   index=1
   ans=147483647
   for i in range(4):
       if ans>m[i]:
           ans=m[i]
           index=i+1
   if ans==147483647:
       return
   if index==1:
       magneto[0]-=1
       return
   if index==2:
       magneto[0]+=1
       return
   if index==3:
       magneto[1]+=1
       return
   if index==4:
       magneto[1]-=1
       return
      
   
    
   
    
   
            
def move_wolverine(U):  # this moves the wolverine
     x=wolverine[0]
     y=wolverine[1]
     up_x=x-1
     up_y=y
     up_value=0
     if up_x >=0 :
         up_value=U[up_x][up_y]
    
     
     down_x=x+1
     down_y=y
     down_value=0
     if down_x <NUM_ROW :
         down_value=U[down_x][down_y]
     
     left_x=x
     left_y=y-1
     left_value=0
     if left_y>=0 :
         left_value=U[left_x][left_y]
     
     
     right_x=x
     right_y=y+1
     right_value=0
     if right_y < NUM_COL :
         right_value=U[right_x][right_y]
     
        
     stay=0
     m=[]
     m.append(stay)
     m.append(up_value)
     m.append(down_value)
     m.append(right_value)
     m.append(left_value)
     
     index=1
     ans=m[0]
     for i in range(len(m)):
         if ans<m[i]:
             ans=m[i]
             index=i+1
     if index==1:
         return 
     if index==2:
         wolverine[0]=up_x
         wolverine[1]=up_y
         return 
     if index==3:
         wolverine[0]=down_x
         wolverine[1]=down_y
         return 
     if index==4:
         wolverine[0]=right_x
         wolverine[1]=right_y
         return 
     if index==5:
         wolverine[0]=left_x
         wolverine[1]=left_y
         return 
     
     
def check_wolverine_reaches_to_jean():  # this is for checking whetehr the wolverine has reached the jane position
    j_x=jean_pos[0]
    j_y=jean_pos[1]
    w_x=wolverine[0]
    w_y=wolverine[1]
    if w_x==j_x and w_y==j_y:
        return True
    
    return False
     

def getU(U, r, c, action):  # it returns the utility of that state going to state transisition
    dr, dc = ACTIONS[action]
    newR, newC = r+dr, c+dc
    if newR < 0 or newC < 0 or newR >= NUM_ROW or newC >= NUM_COL or (newR ==2 and newC == 3): # collide with the boundary or the wall
        return U[r][c]
    else:
        return U[newR][newC]

def calculateU(U, r, c, action):    # it return the utility after applying everything , 0.95 is probabilty given
    u = REWARD
    u += 0.95 * DISCOUNT * getU(U, r, c, (action-1)%4)
    u += 0.95 * DISCOUNT * getU(U, r, c, action)
    u += 0.95 * DISCOUNT * getU(U, r, c, (action+1)%4)
    return u
def valueIteration(U):
    
    while True:
       
        if random.randint(1, 100) <80: # probablity of changing jean posiiton
           switch_jean_pos()
        
        move_wolverine(U) # it moves the wolverine
        
        move_magneto_in_direction_of_wolverine() #it moves the magneto in the direction which minimize the distance the magneto and wolverine
        
        nextU = update_u() #it updates the utilty function
        
        error = 0 # so that after this we can stop this algo
        for r in range(NUM_ROW):
            for c in range(NUM_COL):
                if (r ==magneto[0] and c == magneto[1]) or (r ==2 and c == 3) or (r==jean_pos[0] and c==jean_pos[1]):
                    continue
                nextU[r][c] = max([calculateU(U, r, c, action) for action in range(NUM_ACTIONS)]) # Bellman update formula
                error = max(error, abs(nextU[r][c]-U[r][c]))
        U = nextU
        
        
        
        
        
        
        
       
        if error < MAX_ERROR * (1-DISCOUNT) / DISCOUNT or check_wolverine_reaches_to_jean(): #checking for constant reward and wolverine and jean position
            break
    return U

def printEnvironment(arr, policy=False): # this is to print the state of  the final output and given input
    
    res = ""
    for r in range(NUM_ROW):
        res += "|"
        for c in range(NUM_COL):
            if r == 2 and c == 3:
                val = "WALL"
            elif r==magneto[0] and c==magneto[1]:
                val ="B"
            elif r==jean_pos[0] and c==jean_pos[1]:
                val ="jean"
            elif r==wolverine[0] and c==wolverine[1]:
                val="A"
            else:
                if policy:
                    val = ["Down", "Left", "Up", "Right"][arr[r][c]]
                else:
                    val = str(arr[r][c])
            res += " " + val[:5].ljust(5) + " |" # format
        res += "\n"
    print(res)
    
    
    
if __name__ == '__main__':    
    U=update_u()
    
    print("Initial Setup \n")
    printEnvironment(U)
    
    
    U = valueIteration(U)
   
    policy = getOptimalPolicy(U)
    print("The Optimal Policy is as follow \n")
    printEnvironment(policy, True)
    
    
    
    

