

import matplotlib.pyplot as plt
from functools import wraps



def setupax(func):
    """
    Decorator to ensure a matplotlib axis is available for the decorated function.

    If the 'ax' argument is not provided or is None, it defaults to the current 
    active axis (plt.gca()).

    Parameters
    ----------
    func : callable
        The function to decorate. It must accept an 'ax' keyword argument.

    Returns
    -------
    callable
        The wrapped function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'ax' in kwargs:
            kwargs['ax'] = plt.gca() if not kwargs['ax'] else kwargs['ax']
        else:
            kwargs['ax'] = plt.gca()
        return func(*args, **kwargs)
    return wrapper
