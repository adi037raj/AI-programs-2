# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:17:53 2021

@author: AADITYA RAJ BARNWAL

"""
import random
import numpy as np

REWARD = 0 # constant reward for non-terminal states
DISCOUNT = 0.85
MAX_ERROR = 10**(-3)

NUM_ROW = 5
NUM_COL = 5

c1=[3,4] # uses 0 based indexing
c2=[0,0]
magneto=[2,1]
wolverine=[0,2]
jean_pos=c1

NUM_ACTIONS = 4
ACTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)] # Down, Left, Up, Right
policy = [[random.randint(0, 3) for j in range(NUM_COL)] for i in range(NUM_ROW)] # construct a random policy


def check_for_up_movement(x,y):  # for checking in up direction of magneto
    if x==2 and y==3:
        return False
    if x<0:
        return False
    if x==0 and y==4:
        return False
    return True

def check_for_down_movement(x,y): # for checking in down direction of magneto
    if x==2 and y==3:
        return False
    if x>=NUM_ROW:
        return False
    if x==0 and y==4:
        return False
    return True

def check_for_left_movement(x,y): # for checking in left direction of magneto
    if x==2 and y==3:
        return False
    if y<0:
        return False
    if x==0 and y==4:
        return False
    return True

def check_for_right_movement(x,y): # for checking in right direction of magneto
    if x==2 and y==3:
        return False
    if y>=NUM_COL:
        return False
    if x==0 and y==4:
        return False
    return True

def switch_jean_pos(): # switching the jean postion
    x=jean_pos[0]
    y=jean_pos[1]
    if x==3 and y==4:
        jean_pos[0]=jean_pos[1]=0
    else:
        jean_pos[0]=3
        jean_pos[1]=4


def move_magneto_in_random_direction():  # move magneto in any valid direction
    x=magneto[0]
    y=magneto[1]
    choice=random.randint(1, 4) # 1 means up,2 down,3 left,4 right
    while True:
        choice=random.randint(1, 4) 
        if choice==1:
            
            if check_for_up_movement(x-1, y):
                magneto[0]=x-1
                magneto[1]=y
                
                return
                
        elif choice==2:
            
            if check_for_down_movement(x+1,y):
                magneto[0]=x+1
                magneto[1]=y
                
                return
            
        elif choice==3:
            
            if check_for_left_movement(x, y-1):
                magneto[0]=x
                magneto[1]=y-1
                
                return
            
        elif choice==4:
            
            if check_for_right_movement(x, y+1):
                magneto[0]=x
                magneto[1]=y+1
               
                return


def move_wolverine(U):  # move wolverine
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
     
     
def check_wolverine_reaches_to_jean():  # checking condtion
    j_x=jean_pos[0]
    j_y=jean_pos[1]
    w_x=wolverine[0]
    w_y=wolverine[1]
    if w_x==j_x and w_y==j_y:
        return True
    
    return False
     


def update_u(): # update the utlity
    
    U=np.zeros([5, 5], dtype = int) 
    U[magneto[0]][magneto[1]]=-20
    U[jean_pos[0]][jean_pos[1]]=20
    return U

def printEnvironment(arr, policy=False): # for printing the output
    
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

def getU(U, r, c, action):
    dr, dc = ACTIONS[action]
    newR, newC = r+dr, c+dc
    if newR < 0 or newC < 0 or newR >= NUM_ROW or newC >= NUM_COL or (newR ==2 and newC == 3): # collide with the boundary or the wall
        return U[r][c]
    else:
        return U[newR][newC]

def calculateU(U, r, c, action):
    u = REWARD
    u += 0.1 * DISCOUNT * getU(U, r, c, (action-1)%4)
    u += 0.4 * DISCOUNT * getU(U, r, c, action)
    u += 0.2 * DISCOUNT * getU(U, r, c, (action+1)%4)
    return u
    
def policyEvaluation(policy, U):
    while True:
        nextU = update_u()
        error = 0
        for r in range(NUM_ROW):
            for c in range(NUM_COL):
                if (r ==magneto[0] and c == magneto[1]) or (r ==2 and c == 3) or (r==jean_pos[0] and c==jean_pos[1]):
                    continue
                nextU[r][c] = calculateU(U, r, c, policy[r][c]) # simplified Bellman update
                error = max(error, abs(nextU[r][c]-U[r][c]))
        U = nextU
        if error < MAX_ERROR * (1-DISCOUNT) / DISCOUNT:
            break
    return U
    
def policyIteration(policy, U):
   
    while True:
        
        if random.randint(1, 100) <80:
           switch_jean_pos()
        
        move_wolverine(U)
        
        move_magneto_in_random_direction()
        
        U = policyEvaluation(policy, U)
        unchanged = True
        for r in range(NUM_ROW):
            for c in range(NUM_COL):
                if (r ==magneto[0] and c == magneto[1]) or (r ==2 and c == 3) or (r==jean_pos[0] and c==jean_pos[1]):
                    continue
                maxAction, maxU = None, -float("inf")
                for action in range(NUM_ACTIONS):
                    u = calculateU(U, r, c, action)
                    if u > maxU:
                        maxAction, maxU = action, u
                if maxU > calculateU(U, r, c, policy[r][c]):
                    policy[r][c] = maxAction # the action that maximizes the utility
                    unchanged = False
        
        if unchanged or check_wolverine_reaches_to_jean():
            break
        
    return policy



if __name__ == '__main__':   
   U=update_u()
   printEnvironment(U)
   
   
   policy = policyIteration(policy, U)
   print("The optimal policy is:\n")
   printEnvironment(policy,True)
   
   
   