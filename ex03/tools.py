import numpy as np


def add_intercept(x):
    """Adds a column of first to the non-empty numpy.array x.
    Args:
        x: has to be an numpy.array, a vector of shape m * 1.
    Returns:
        x as a numpy.array, a vector of shape m * 2.
        None if x is not a numpy.array.
        None if x is a empty numpy.array.
    Raises:
        This function should not raise any Exception.
    """
    try:
        if not isinstance(x, np.ndarray):
            return None
        if any([n == 0 for n in x.shape]):
            return None
        intercept = np.ones((x.shape[0], 1))
        xp = np.hstack((intercept, x))
        return xp
    except:
        return None