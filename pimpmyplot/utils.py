

import matplotlib.pyplot as plt
from functools import wraps



def setupax(func):
    '''
    If func takes in input ax argument replace it with plt.gca() in case it is None
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'ax' in kwargs:
            kwargs['ax'] = plt.gca() if not kwargs['ax'] else kwargs['ax']
        else:
            kwargs['ax'] = plt.gca()
        return func(*args, **kwargs)
    return wrapper
