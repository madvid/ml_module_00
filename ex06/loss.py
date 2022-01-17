import numpy as np

def loss_elem_(y, y_hat):
    """
    Description:
    Calculates all the elements (y_pred - y)^2 of the loss function.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    J_elem: numpy.array, a vector of dimension (number of the training examples,1).
    None if there is a dimension matching problem between y and y_hat.
    None if y or y_hat is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    res = np.zeros(y.shape)
    ii = 0
    for ii in range(y.shape[0]):
        res[ii] = (y[ii] - y_hat[ii]) ** 2
    return res


def loss_(y, y_hat):
    """
    Description:
    Calculates the value of loss function.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    J_value : has to be a float.
    None if there is a shape matching problem between y or y_hat.
    None if y or y_hat is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    residual = loss_elem_(y, y_hat)
    loss = 0.0
    for residual_i in residual:
        loss += residual_i
    return float(loss / (2.0 * y.shape[0]))
