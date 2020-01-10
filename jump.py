import math

import config


def magnitude(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def dot_product(a_x, a_y, b_x, b_y):
    return a_x * b_x + a_y * b_y


def angle_between(b_x, b_y, c_x, c_y):
    if b_x == 0 and b_y == 0:
        return 0
    
    if c_x == 0 and c_y == 0:
        return 0
    
    return math.acos(dot_product(b_x,b_y, c_x,c_y) / (magnitude(b_x,b_y) * magnitude(c_x,c_y)))


"""Compute jump endpoint for a jump from cur_x,cur_y towards dest_x,dest_y,
making sure not to jump farther than config.maximum_jump_distance"""
def towards(cur_x, cur_y, dest_x, dest_y):
    distance_to_destination = magnitude(dest_x - cur_x, dest_y - cur_y)

    if distance_to_destination > config.maximum_jump_distance:
        x = cur_x - round((config.maximum_jump_distance * (cur_x - dest_x)) / distance_to_destination)
        y = cur_y - round((config.maximum_jump_distance * (cur_y - dest_y)) / distance_to_destination)
    else:
        x = dest_x
        y = dest_y

    return x, y


def find_collision_point(target_pos_x,target_pos_y, target_vel_x,target_vel_y, interceptor_pos_x,interceptor_pos_y):
    k = magnitude(target_vel_x,target_vel_y) / config.maximum_jump_distance
    distance_to_target = magnitude(interceptor_pos_x - target_pos_x, interceptor_pos_y - target_pos_y)

    b_hat_x = target_vel_x
    b_hat_y = target_vel_y
    c_hat_x = interceptor_pos_x - target_pos_x
    c_hat_y = interceptor_pos_y - target_pos_y

    cab = angle_between(b_hat_x,b_hat_y, c_hat_x,c_hat_y)
    abc = math.asin(math.sin(cab) * k)
    acb = math.pi - (cab + abc)

    j = distance_to_target / math.sin(acb)
    #a = j * math.sin(cab)
    b = j * math.sin(abc)

    time_to_collision = b / magnitude(target_vel_x,target_vel_y)
    collision_pos_x = target_pos_x + (target_vel_x * time_to_collision)
    collision_pos_y = target_pos_y + (target_vel_y * time_to_collision)

#    return interceptor_pos_x - collision_pos_x, interceptor_pos_y - collision_pos_y
    return math.ceil(time_to_collision), round(collision_pos_x),round(collision_pos_y)
    