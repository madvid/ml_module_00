import numpy as np

from ..ex04.prediction.predict_


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
    return np.power(y - y_hat, 2)


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
    loss = np.sum(loss_elem_, axis=0) / (2.0 * y.shape[0])
    return loss


if __name__ == "__main__":
    # Example 1:
    x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
    theta1 = np.array([[2.], [4.]])
    y_hat1 = ex04.prediction.predict_(x1, theta1)
    
    y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
    loss_elem_(y1, y_hat1)
    # Output:
    #array([[0.], [1], [4], [9], [16]])
    
    # Example 2:
    loss_(y1, y_hat1)
    # Output:
    # 3.0
    
    # Example 3:
    x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
    theta2 = np.array([[0.05], [1.], [1.], [1.]])
    y_hat2 = ex04.prediction.predict_(x2, theta2)
    y2 = np.array([[19.], [42.], [67.], [93.]])
    
    loss_elem_(y2, y_hat2)
    # Output:
    # array([[10.5625], [6.0025], [0.1225], [17.2225]])
    
    # Example 4:
    loss_(y2, y_hat2)
    # Output:
    # 4.238750000000004
    
    
    
    # Example 5:
    x3 = np.array([[0],[ 15],[ -9],[ 7],[ 12],[ 3],[ -21]])
    theta3 = np.array([[0.], [1.]])
    y_hat3 = ex04.prediction.predict_(x3, theta3)
    y3 = np.array([[2],[ 14],[ -13],[ 5],[ 12],[ 4],[ -19]])
    
    loss_(y3, y_hat3)
    # Output:
    # 2.142857142857143
    
    
    # Example 6:
    loss_(y3, y3)
    # Output:
    # 0.0