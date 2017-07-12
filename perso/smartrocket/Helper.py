import random
from Constante import   WIDTH,\
                        HEIGHT,\
                        TOUCH_OBS,\
                        TOUCH_TARGET,\
                        SUCCED_SCALE,\
                        NB_SECTEUR, \
                        OBS_SCALE, \
                        NB_OBS

def constrain(value, from_value, to_value):
    """
    """
    if value < from_value:
        return from_value
    elif value > to_value:
        return to_value
    else:
        return value

def mapjs(value, mini, maxi, newmin, newmax, step = None):
    """
    scaling function
    """
    if step is None:
        return (value / (maxi - mini))*(newmax-newmin)
    else:
        new_value = (value / (maxi - mini))*(newmax-newmin)
        arround = new_value % step
        if arround < 5:
            new_value -= arround
        else:
            new_value += 10-arround
        return new_value

def distsq(rocket, target):
    """
    """
    return (rocket.pos.x() - target.posx)**2 + (rocket.pos.y() - target.posy)**2


def succed(rocket, target):
    """
    """
    dis = 1/distsq(rocket, target)
    if rocket.crashed:
        dis *= TOUCH_OBS
    if rocket.goal:
        dis *= TOUCH_TARGET
        dis /= mapjs(rocket.iter, 0, rocket.max_iter, 0, 100) + 0.1
    return dis * SUCCED_SCALE


if __name__ == "__main__":
    for i in range(100):
        print(i, mapjs(i, 0, 100, 0, 100, 10))
