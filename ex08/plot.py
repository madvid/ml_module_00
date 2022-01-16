import sys
import os
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

sys.path.insert(1, os.path.realpath("../ex04"))
from prediction import predict_

def plot_with_loss(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        y: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
        Nothing.
    Raises:
        This function should not raise any Exception.
    """

    fig, axe = plt.subplots(1, 1, figsize = (15,8))
    axe.scatter(x, y, c="blue")
    ypred = predict_(x, theta)
    axe.plot(x, ypred, '--', c='orange')
    
    for ii in range(x.shape[0]):
        axe.plot([x[ii], y[ii]], [x[ii], ypred[ii]], 'r--')
    plt.show()

if __name__ == "__main__":
    x = np.arange(1,6)
    y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
    #Example 1:
    theta1= np.array([[18],[-1]])
    plot_with_loss(x, y, theta1)
    # Output:

    #Example 2:
    theta2 = np.array([[14], [0]])
    plot_with_loss(x, y, theta2)
    # Output:

    #Example 3:
    theta3 = np.array([[12], [0.8]])
    plot_with_loss(x, y, theta3)
    # Output:

    plot_with_loss(np.array([0, 1]), np.array([0, 1]), np.array([[0], [1]]))
    plot_with_loss(np.array([0, 1]), np.array([0, 1]), np.array([[1], [1]]))
    plot_with_loss(np.array([0, 2]), np.array([0, 0]), np.array([[-1], [1]]))