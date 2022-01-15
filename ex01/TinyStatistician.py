import numpy as np
from typing import Union, List

class TinyStatistician():
    
    @staticmethod
    def mean(x:Union[np.ndarray, list]) -> float:
        """Calculates the mean of the given array along the axis 0 of the array
        (i.e. column-wise)
        Parameters:
            x [np.ndarray]: np.ndarray containing the differents features along axis 1.
        Return:
            mean [np.ndarray]: array containing the mean of each feature (column)
        """
        try:
            mean = 0.0
            for x_i in x:
                mean += x_i
            mean = mean / len(x)
            return mean
        except:
            return None


    @staticmethod
    def median(x:Union[np.ndarray, list]) -> float:
        """Calculates the mean of the given array along the axis 0 of the array
        (i.e. column-wise)
        Parameters:
            x [np.ndarray]: np.ndarray containing the differents features along axis 1.
        Return:
            mean [np.ndarray]: array containing the mean of each feature (column)
        """
        try:
            x_sorted = sorted(x)
            if len(x) % 2:
                median = x_sorted[int(len(x) / 2)]
            else:
                median = 0.5 * (x_sorted[int(len(x) / 2) - 1] + x_sorted[int(len(x) / 2)])
            return median
        except:
            return None


    @staticmethod
    def quartile(x:Union[np.ndarray, list]) -> list:
        """ Extracts the percentile p of each features (column of x)
        Parameters:
            x [np.ndarray]: np.ndarray containing the differents features along axis 1.
        Return:
            v_percent [np.ndarray]: array (shape[1, m]) containing the p percentile of each features.
        """
        try:
            l_x = len(x)
            x_sorted = sorted(x)
            idx_1 = int(np.ceil(0.25 * l_x)) - 1
            idx_2 = int(np.ceil(0.75 * l_x)) - 1
            quartile =[x_sorted[idx_1], x_sorted[idx_2]]
            return quartile
        except:
            return None


    @staticmethod
    def percentile(x:Union[np.ndarray, list], p:int) -> float:
        """ Extracts the percentile p of each features (column of x)
        Parameters:
            x [np.ndarray]: np.ndarray containing the differents features along axis 1.
        Return:
            v_percent [np.ndarray]: array (shape[1, m]) containing the p percentile of each features.
        """
        try:
            l_x = len(x)
            x_sorted = sorted(x)
            idx = int(np.ceil(0.01 * p * l_x)) - 1
            percentiles = x_sorted[idx]
            return percentiles
        except:
            return None


    @staticmethod
    def var(x:Union[np.ndarray, list]) -> float:
        """Calculates the standard deviation of each features.
        Parameters:
            x [np.ndarray]: np.ndarray containing the differents features along axis 1.
            mean [np.ndarray]: numpy array containing the mean of each features.
        Return:
            std [np.ndarray]: array containing the standard deviation of each feature (column)
        """
        try:
            mean = TinyStatistician.mean(x)
            var =  0.0
            for x_i in x:
                var += (x_i - mean) ** 2
            
            var = var / len(x)
            return var
        except:
            return None

    
    @staticmethod
    def std(x:Union[np.ndarray, list]) -> float:
        """Calculates the standard deviation of each features.
        Parameters:
            x [np.ndarray]: np.ndarray containing the differents features along axis 1.
            mean [np.ndarray]: numpy array containing the mean of each features.
        Return:
            std [np.ndarray]: array containing the standard deviation of each feature (column)
        """
        try:
            
            var = TinyStatistician.var(x)
            return np.sqrt(var)
        except:
            return None

