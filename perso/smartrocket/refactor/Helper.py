from Constante import TOUCH_OBS, TOUCH_TARGET, SUCCED_SCALE
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
        if arround < step / 2:
            new_value -= arround
        else:
            new_value += step - arround
        return new_value

def distsq(rocket, target):
    """
    """
    return (rocket.posx - target.posx)**2 + (rocket.posy - target.posy)**2
