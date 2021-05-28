# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:07:31 2021

@author: AADITYA RAJ BARNWAL
"""
import random
import math 


def find_naximum(distance_from_corner_right_top,distance_from_corner_left_top, distance_from_corner_bottom_right,distance_from_corner_bottom_left,distance_from_caveman1,distance_from_caveman2): # it returns which one is greater
            # return 1 for cavemen 1,caveem2 is 2, topleft=3,topright=4,bottomleft=5,bottomright=6
    ans=distance_from_caveman1
    res=1
    if ans<distance_from_caveman2:
        ans=distance_from_caveman2
        res=2
    if ans<distance_from_corner_bottom_left:
        ans=distance_from_corner_bottom_left
        res=3
    if ans<distance_from_corner_right_top:
        ans=distance_from_corner_right_top
        res=4
    if ans<distance_from_corner_bottom_left:
        ans=distance_from_corner_bottom_left
        res=5
    if ans<distance_from_corner_bottom_right:
        ans=distance_from_corner_bottom_left
        res=5
    return res
def find_euclidean_distance(x1,y1,x2,y2): #this return the euclidean distance between two points
    p=x1-x2
    q=y1-y2
    r=p*p+q*q
    return math.sqrt(r)


def myfunction_for_caveman2(caveman1_location_x,caveman1_location_y):  #so that they dont lie in the same place
    caveman2_location_x=random.randint(1, 8)

    caveman2_location_y=random.randint(1, 8)
    if caveman1_location_x==caveman2_location_x or caveman1_location_y==caveman2_location_y:
     return myfunction_for_caveman2(caveman1_location_x,caveman1_location_y)
    else:
        return caveman2_location_x,caveman2_location_y
    



def check_whether_caveman_reached(caveman1_location_x,curr_sheep_location_x,caveman1_location_y,curr_sheep_location_y): #it return true if caveman catches thee sheep
    if caveman1_location_x+1==curr_sheep_location_x and caveman1_location_y==curr_sheep_location_y:
        return True
    if caveman1_location_x-1==curr_sheep_location_x and caveman1_location_y==curr_sheep_location_y:
        return True
    if caveman1_location_x==curr_sheep_location_x and caveman1_location_y+1==curr_sheep_location_y:
        return True
    if caveman1_location_x==curr_sheep_location_x and caveman1_location_y-1==curr_sheep_location_y:
        return True
    return False

def find_sheep_move_or_stay(caveman1_location_x,curr_sheep_location_x,caveman1_location_y,curr_sheep_location_y,caveman2_location_x,caveman2_location_y): # this function is to know whether the sheep should move or not, by investigating 2 unit radius 
    if caveman1_location_x+1==curr_sheep_location_x and caveman1_location_y==curr_sheep_location_y:
        return True
    if caveman1_location_x-1==curr_sheep_location_x and caveman1_location_y==curr_sheep_location_y:
        return True
    if caveman1_location_x==curr_sheep_location_x and caveman1_location_y+1==curr_sheep_location_y:
        return True
    if caveman1_location_x==curr_sheep_location_x and caveman1_location_y-1==curr_sheep_location_y:
        return True
    if caveman2_location_x+1==curr_sheep_location_x and caveman2_location_y==curr_sheep_location_y:
        return True
    if caveman2_location_x-1==curr_sheep_location_x and caveman2_location_y==curr_sheep_location_y:
        return True
    if caveman2_location_x==curr_sheep_location_x and caveman2_location_y+1==curr_sheep_location_y:
        return True
    if caveman2_location_x==curr_sheep_location_x and caveman2_location_y-1==curr_sheep_location_y:
        return True
    
    
    if caveman2_location_x+2==curr_sheep_location_x and caveman2_location_y==curr_sheep_location_y:
        return True
    if caveman2_location_x-2==curr_sheep_location_x and caveman2_location_y==curr_sheep_location_y:
        return True
    if caveman2_location_x==curr_sheep_location_x and caveman2_location_y+2==curr_sheep_location_y:
        return True
    if caveman2_location_x==curr_sheep_location_x and caveman2_location_y-2==curr_sheep_location_y:
        return True
    
    return False

def move_in_direction_of_caveman(curr_sheep_location_x,caveman1_location_x,curr_sheep_location_y,caveman1_location_y): #this function moves the sheep in the direction of the given caveman, we approach this part when we know that distance from this caveman is greater than any corner and other caveman
    if curr_sheep_location_x<=caveman1_location_x and curr_sheep_location_y<=caveman1_location_y:
        if curr_sheep_location_x-2>=1 and curr_sheep_location_y+2<=8:
             curr_sheep_location_x-=2
             curr_sheep_location_y+=2
        elif curr_sheep_location_x-1>=1 and curr_sheep_location_y+1<=8:
            curr_sheep_location_x-=1
            curr_sheep_location_y+=1
    elif curr_sheep_location_x>=caveman1_location_x and curr_sheep_location_y>=caveman1_location_y:
          if curr_sheep_location_x-2>=1 and curr_sheep_location_y-2<=8:
             curr_sheep_location_x-=2
             curr_sheep_location_y-=2
          elif curr_sheep_location_x-1>=1 and curr_sheep_location_y-1>=1:
            curr_sheep_location_x-=1
            curr_sheep_location_y-=1
    elif curr_sheep_location_x<=caveman1_location_x and curr_sheep_location_y>=caveman1_location_y:
          if curr_sheep_location_x+2<=8 and curr_sheep_location_y-2>=1:
             curr_sheep_location_x+=2
             curr_sheep_location_y-=2
          elif curr_sheep_location_x+1<=8 and curr_sheep_location_y-1>=1:
            curr_sheep_location_x+=1
            curr_sheep_location_y-=1
    else:
          if curr_sheep_location_x-2>=1 and curr_sheep_location_y-2>=1:
             curr_sheep_location_x-=2
             curr_sheep_location_y-=2
          elif curr_sheep_location_x-1>=1 and curr_sheep_location_y-1>=1:
            curr_sheep_location_x-=1
            curr_sheep_location_y-=1
    return curr_sheep_location_x,curr_sheep_location_y
    

def move_caveman_in_direction_of_sheep(caveman1_location_x,caveman1_location_y,curr_sheep_location_x,curr_sheep_location_y): # it moves the caveman in direction of sheep
    move_left_x=caveman1_location_x
    move_left_y=caveman1_location_y+1
    move_down_x=caveman1_location_x+1
    move_up_x=caveman1_location_x-1
    move_up_y=caveman1_location_y
    move_down_y=caveman1_location_y
    move_right_x=caveman1_location_x
    move_right_y=caveman1_location_y-1
    if move_left_x<=8 and move_left_y<=8:
     move_left=math.sqrt((curr_sheep_location_x-move_left_x)* (curr_sheep_location_x-move_left_x) + (curr_sheep_location_y-move_left_y)*(curr_sheep_location_y-move_left_y))   
    else:
        move_left=100000
    
    if move_right_x<=8 and move_right_y>=1:
     move_right=math.sqrt((curr_sheep_location_x-move_right_x)* (curr_sheep_location_x-move_right_x) + (curr_sheep_location_y-move_right_y)*(curr_sheep_location_y-move_right_y))   
    else:
        move_right=100000
    
    if move_up_x>=1 and move_up_y<=8:
     move_up=math.sqrt((curr_sheep_location_x-move_up_x)* (curr_sheep_location_x-move_up_x) + (curr_sheep_location_y-move_up_y)*(curr_sheep_location_y-move_up_y))   
    else:
      move_up=100000
    
    if move_down_x<=8 and move_up_y<=8:
     move_down=math.sqrt((curr_sheep_location_x-move_down_x)* (curr_sheep_location_x-move_down_x) + (curr_sheep_location_y-move_down_y)*(curr_sheep_location_y-move_down_y))   
    else:
        move_down=100000
    
    ans=100000
    if ans>move_left:
        caveman1_location_x=move_left_x
        caveman1_location_y=move_left_y
        ans=move_left
    if ans>move_right:
        caveman1_location_x=move_right_x
        caveman1_location_y=move_right_y
        ans=move_right
    if ans>move_down:
        caveman1_location_x=move_down_x
        caveman1_location_y=move_down_y
        ans=move_down
    if ans>move_up:
        caveman1_location_x=move_up_x
        caveman1_location_y=move_up_y
        ans=move_up_x
    return caveman1_location_x,caveman1_location_y



if __name__ == "__main__":
    
    iteration=200
    curr_sheep_location_x=random.randint(1, 8)
    curr_sheep_location_y=random.randint(1, 8)
    caveman1_location_x=random.randint(1, 8)
    caveman1_location_y=random.randint(1, 8)
    caveman2_location_x,caveman2_location_y=myfunction_for_caveman2(caveman1_location_x,caveman1_location_y)
    is_any_one_catch=False
    for i in range(0,iteration):
        if check_whether_caveman_reached(caveman1_location_x,curr_sheep_location_x,caveman1_location_y,curr_sheep_location_y):
            print("Caveman 1 catches the Sheep")
            is_any_one_catch=True
            break
        if check_whether_caveman_reached(caveman2_location_x,curr_sheep_location_x,caveman2_location_y,curr_sheep_location_y):
            print("Caveman 2 catches the Sheep")
            is_any_one_catch=True
            break
        prev_x=curr_sheep_location_x
        prev_y=curr_sheep_location_y
        if find_sheep_move_or_stay(caveman1_location_x,curr_sheep_location_x,caveman1_location_y,curr_sheep_location_y,caveman2_location_x,caveman2_location_y):
            distance_from_corner_right_top=find_euclidean_distance(curr_sheep_location_x, curr_sheep_location_y, 1, 1)
            distance_from_corner_left_top=find_euclidean_distance(curr_sheep_location_x, curr_sheep_location_y, 1  , 8)
            distance_from_corner_bottom_right=find_euclidean_distance(curr_sheep_location_x, curr_sheep_location_y, 8  , 1)
            distance_from_corner_bottom_left=find_euclidean_distance(curr_sheep_location_x, curr_sheep_location_x, 8, 8)
            distance_from_caveman1=find_euclidean_distance(curr_sheep_location_x, curr_sheep_location_y, caveman1_location_x, caveman1_location_y)
            distance_from_caveman2=find_euclidean_distance(curr_sheep_location_x, curr_sheep_location_y, caveman2_location_x, caveman2_location_y)
            res=find_naximum(distance_from_corner_right_top,distance_from_corner_left_top, distance_from_corner_bottom_right,distance_from_corner_bottom_left,distance_from_caveman1,distance_from_caveman2)
           
            if res==1:
               curr_sheep_location_x,curr_sheep_location_y= move_in_direction_of_caveman(curr_sheep_location_x,caveman1_location_x,curr_sheep_location_y,caveman1_location_y)
            elif res==2:
                curr_sheep_location_x,curr_sheep_location_y=move_in_direction_of_caveman(curr_sheep_location_x,caveman2_location_x,curr_sheep_location_y,caveman2_location_y)
            elif res==3:
                if curr_sheep_location_x-2>=1 and curr_sheep_location_y-2>=1:
                     curr_sheep_location_x-=2
                     curr_sheep_location_y-=2
                elif curr_sheep_location_x-1>=1 and curr_sheep_location_y-1>=1:
                    curr_sheep_location_x-=1
                    curr_sheep_location_y-=1
                                    
                
            elif res==4:
                if curr_sheep_location_x-2>=1 and curr_sheep_location_y+2<=8:
                    curr_sheep_location_x-=2
                    curr_sheep_location_y+=2
                elif curr_sheep_location_x-1>=1 and curr_sheep_location_y+1<=8:
                    curr_sheep_location_x-=1
                    curr_sheep_location_y+=1
                
                
            elif res==5:
                
                if curr_sheep_location_x+2<=8 and curr_sheep_location_y-2>=1:
                    curr_sheep_location_x+=2
                    curr_sheep_location_y-=2
                elif curr_sheep_location_x+1<=8 and curr_sheep_location_y-1>=1:
                    curr_sheep_location_x+=1
                    curr_sheep_location_y-=1
                
                
            elif res==6:
                
                if curr_sheep_location_x+2<=8 and curr_sheep_location_y+2<=8:
                    curr_sheep_location_x+=2
                    curr_sheep_location_y+=2
                elif curr_sheep_location_x+1<=8 and curr_sheep_location_y+1<=8:
                    curr_sheep_location_x+=1
                    curr_sheep_location_y+=1
        
        caveman1_location_x,caveman1_location_y=move_caveman_in_direction_of_sheep(caveman1_location_x,caveman1_location_y,prev_x,prev_y)
        caveman2_location_x,caveman2_location_y=move_caveman_in_direction_of_sheep(caveman2_location_x,caveman2_location_y,prev_x,prev_y)
            
    if is_any_one_catch==False:
        print("No one catches Sheep")        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    