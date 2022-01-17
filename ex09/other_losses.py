import numpy as np
from math import sqrt


def mse_(y, y_hat):
    """
    Description:
    Calculate the MSE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
    mse: has to be a float.
    None if there is a matching shape problem.
    Raises:
    This function should not raise any Exception.
    """
    try:
        mse = (1.0 / y.shape[0]) * np.sum((y - y_hat) ** 2, axis=0)
        return float(mse)
    except:
        return None


def rmse_(y, y_hat):
    """
    Description:
    Calculate the RMSE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
    rmse: has to be a float.
    None if there is a matching shape problem.
    Raises:
    This function should not raise any Exception.
    """
    try:
        rmse = sqrt(mse_(y, y_hat))
        return float(rmse)
    except:
        return None


def mae_(y, y_hat):
    """
    Description:
    Calculate the MAE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
    mae: has to be a float.
    None if there is a matching shape problem.
    Raises:
    This function should not raise any Exception.
    """
    try:
        mae = (1.0 / y.shape[0]) * np.sum(np.absolute(y - y_hat), axis=0)
        return float(mae)
    except:
        return None


def r2score_(y, y_hat):
    """
    Description:
    Calculate the R2score between the predicted output and the output.
    Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
    r2score: has to be a float.
    None if there is a matching shape problem.
    Raises:
    This function should not raise any Exception.
    """
    try:
        mean = np.mean(y, axis = 0)
        r2 = 1 - np.sum((y_hat - y) ** 2, axis = 0) / np.sum((y - mean) ** 2, axis = 0)
        return float(r2)
    except:
        return None