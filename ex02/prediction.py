import numpy as np

def simple_predict(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be an numpy.array, a vector of shape 2 * 1.
    Returns:
    y_hat as a numpy.array, a vector of shape m * 1.
    None if x or theta are empty numpy.array.
    None if x or theta shapes are not appropriate.
    None if x or theta is not of the expected type.
    Raises:
    This function should note raise any Exception
    """
    try:
        if not isinstance(x, np.ndarray):
            return None
        if not isinstance(theta, np.ndarray):
            return None
        if (theta.shape != (2, 1)) or (x.shape[1] != 1):
            return None

        y = np.zeros(x.shape)
        for ii in range(x.shape[0]):
            y[ii] = theta[0] + theta[1] * x[ii]
        return y
    except:
        return None