import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
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
        rmse = np.sqrt(mse_(y, y_hat))
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



if __name__ == '__main__':
    x = np.array([[0],[ 15],[ -9],[ 7],[ 12],[ 3],[ -21]])
    y = np.array([[2],[ 14],[ -13],[ 5],[ 12],[ 4],[ -19]])
    
    # Mean squared error
    ## your implementation
    mse_(x,y)
    ## Output:
    ## 4.285714285714286
    ## sklearn implementation
    mean_squared_error(x,y)
    ## Output:
    ## 4.285714285714286
    
    
    # Root mean squared error
    ## your implementation
    rmse_(x,y)
    ## Output:
    ## 2.0701966780270626
    ## sklearn implementation not available: take the square root of MSE
    sqrt(mean_squared_error(x,y))
    ## Output:
    ## 2.0701966780270626
    
    
    # Mean absolute error
    ## your implementation
    mae_(x,y)
    # Output:
    ## 1.7142857142857142
    ## sklearn implementation
    mean_absolute_error(x,y)
    # Output:
    ## 1.7142857142857142
    
    
    # R2-score
    ## your implementation
    r2score_(x,y)
    ## Output:
    ## 0.9681721733858745
    ## sklearn implementation
    r2_score(x,y)
    ## Output:
    ## 0.9681721733858745