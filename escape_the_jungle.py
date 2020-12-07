# import world.turtle
from world.turtle import world

import random
obstacle_list = []

def draw_rect(start_x, end_x, start_y, end_y):
    global obstacle_list

    door = random.randrange((start_x+5),(end_x-5),5)
    for i in range(start_x,end_x,5):
        if (i == door or i ==(door + 5)):
            continue
        else:
            obstacle_list.append((i,end_y))


    door = random.randrange((start_y+5),(end_y+5),5)
    for i in range(start_y,end_y,5):
        if (i == door or i ==(door + 5)):
            continue
        else:
            obstacle_list.append((end_x,i))

    door = random.randrange((start_x+5),(end_x+5),5)
    for i in range(start_x,end_x,5):
        if (i == door or i ==(door + 5)):
            continue
        else:
            obstacle_list.append((i,start_y))

    door = random.randrange((start_y+5),(end_y+5),5)
    for i in range(start_y,end_y,5):
        if (i == door or i ==(door + 5)):
            continue
        else:
            obstacle_list.append((start_x,i))


def make_obstacles():
    start_x = -90
    end_x = 85

    start_y=-190
    end_y=185

    draw_rect(start_x, end_x, start_y, end_y)
    
    for i in range(4):
        start_x = start_x+15
        end_x = end_x-15
        
        start_y = start_y+15
        end_y = end_y-15
        
        draw_rect(start_x, end_x, start_y, end_y)
    
 
    


def make_obstacle_list():
    global obstacle_list
    
    make_obstacles()
    return obstacle_list

def is_position_blocked(x,y):
    #import turtle.world
    """
    Checks for each obstacle if new x and y- coordinates lie within the obstacle.
    """
    for item in obstacle_list:
        
        if (x in range(item[0],item[0]+5) and y in range(item[1],item[1]+5)):
            world.path_or_position_blocked = True
            return True
    
    return False

def is_path_blocked(x1,y1, x2, y2):
    global obstacle_list
    print(x1)
    print(x2)
    print(y1)
    [print(obstacle) for obstacle in obstacle_list]
    print(y2)
    """
    checks if an obstacle is not in the path from the old 
    to the new position of the turtle,
    for each randomly generated obstacle.
    """
    
    for item in obstacle_list:
        if world.current_direction_index == 0:
             if (item[1] in range(y1,y2) and x1 in range(item[0],item[0]+5)):
                    world.path_or_position_blocked = True
                    return True
            
            
        if world.current_direction_index == 3:
            
            if (y1 in range(item[1],item[1]+5) and item[0] in range(x2,x1)):
                world.path_or_position_blocked = True
                return True

        if world.current_direction_index == 2:
            
            if (item[1] in range(y1,y2) and x1 in range(item[0],item[0]+5)):
                world.path_or_position_blocked = True
                return True

        if world.current_direction_index == 1:
            if (item[0] in range(x1,x2) and y1 in range(item[1],item[1]+5)):
                world.path_or_position_blocked = True
                print("here")
                return True
            
    return False


    
