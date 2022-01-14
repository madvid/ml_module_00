from __future__ import annotations
from copy import deepcopy

class Matrix():
    def __init__(self, *args):
        if len(args) != 1:
            raise ValueError("No or multiple arguments given. Only one is expected")
        self.checking_data(*args)
        self.data = self._get_data_(*args)
        self.shape = self._get_shape_(*args)


    @staticmethod
    def checking_data(arg):
        if not isinstance(arg, (tuple, list)):
            raise TypeError("Unexpected data type, must be a list or a tuple.")
        if isinstance(arg, tuple):
            l_t = len(arg)
            if l_t != 2:
                raise ValueError("Unexpected length for shape argument.")
            if not isinstance(arg[0], (int, float)) or not isinstance(arg[1], (int, float)):
                raise TypeError("Unexpected type within shape argument")

        if isinstance(arg, list):
            if any([not isinstance(l, list) for l in arg]):
                raise TypeError("Unexpected type within the data argument.")
            l_t = len(arg)
            if l_t == 0:
                raise ValueError("Unexpected length for data argument.")
            for l_line in arg:
                if any([not isinstance(elem, (int, float)) for elem in l_line]):
                    raise TypeError("Unexpected element type for data argument.")
            l_ref = len(arg[0])
            if any([len(line) != l_ref for line in arg]):
                raise ValueError("Heterogenous column length in data argument.")


    def _get_data_(self, arg):
        if isinstance(arg, list):
            dupplicate = arg.copy()
            return dupplicate
        else:
            # arg is a tuple
            n_line, n_col = arg[0], arg[1]
            data = []
            [data.append([0] * n_col) for _ in range(n_line)]
            return data


    def _get_shape_(self, arg):
        if isinstance(arg, tuple):
            return arg
        else:
            n_line, n_col = len(arg), len(arg[0])
            return (n_line, n_col)


    def T(self) -> Matrix:
        new = Matrix(self.shape[::-1])
        for ii in range(self.shape[0]):
            for jj in range(self.shape[1]):
                new[jj][ii] = self.data[ii][jj]
        return new
        
        
    def __add__(self, other):
        if not isinstance(other, Matrix):
            print("Right member of the addition operator is not a Matrix instance.")
            return
        try:
            if self.shape != other.shape:
                print("Incompatible shape.")
                return
            res = Matrix(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = self.data[ii][jj] + other.data[ii][jj]
            return res
        except:
            print("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")
      

    def __radd__(self, other):
        if not isinstance(other, Matrix):
            print("Left member of the addition operator is not a Matrix instance.")
            return
        try:
            if self.shape != other.shape:
                print("Incompatible shape.")
                return
            res = Matrix(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = other.data[ii][jj] + self.data[ii][jj]
            return res
        except:
            print("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __sub__(self, other):
        if not isinstance(other, Matrix):
            print("Right member of the subtraction operator is not a Matrix instance.")
            return
        try:
            if self.shape != other.shape:
                print("Incompatible shape.")
                return
            res = Matrix(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = self.data[ii][jj] - other.data[ii][jj]
            return res
        except:
            print("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __rsub__(self, other):
        if not isinstance(other, Matrix):
            print("Left member of the substraction operator is not a Matrix instance.")
            return
        try:
            if self.shape != other.shape:
                print("Incompatible shape.")
                return
            res = Matrix(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = other.data[ii][jj] - self.data[ii][jj]
            return res
        except:
            print("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __truediv__(self, other):
        if isinstance(other, Matrix):
            print("Warning, you should not try to divide a Matrix by another Matrix.")
            try:
                if other.shape == (1,1):
                    res = Matrix(self.shape)
                    for ii in range(self.shape[0]):
                        for jj in range(self.shape[1]):
                            res = self.data[ii][jj] / other[0][0]
                    return res      
            except:
                print("Divisor issue: either Matrix is not of dimension (1x1) or prior corruption of the Matrix object has been made.")
        if not isinstance(other, (int, float)):
            print("Right member of the division operator is not a scalar.")
            return
        try:
            res = Matrix(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res = self.data[ii][jj] / other[0][0]
            return res
        except:
            print("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __rtruediv__(self, other):
        print("Warning, you should not try to divide a Matrix by another Matrix. You must know what you are doing.")
        try:
            if self.shape != (1,1):
                print("Left member of the division operator is not a Matrix, int or float instance.")
                return
            
            if isinstance(other, Matrix):
                if self.shape == (1,1):
                    res = Matrix(other.shape)
                    for ii in range(other.shape[0]):
                        for jj in range(other.shape[1]):
                            res = other.data[ii][jj] / self.data[0][0]
                    return res
            
            elif isinstance(other, (int, float)):
                return Matrix([[other / self.data[0][0]]])
            else:
                print("Error: Right member of the division is not a (1x1) dimensional Matrix instance.")
                return
        except:
            print("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __mul__(self, other):
        if not isinstance(other, (Matrix, int, float, Vector)):
            print("Right member of the multiplication operator is not a Matrix instance.")
            return
        try:
            if isinstance(other, (int, float)):
                res = Matrix(self.shape)
                for ii in range(self.shape[0]):
                    for jj in range(self.shape[1]):
                        res[ii][jj] = self.data[ii][jj] * other
                return res
            elif isinstance(other, Matrix):
                if self.shape[1] == other.shape[0]:
                    res = Matrix((self.shape[0], other.shape[1]))
                    for ii in range(self.shape[0]):
                        for kk in range(other.shape[1]):
                            for jj in range(self.shape[1]):
                                res[ii][kk] += self.data[ii][jj] * other.data[jj][kk]
                    return res
                else:
                    print("Mismatch dimension between Matrix instances.")
                    return
            elif isinstance(other, Vector):
                if self.shape[1] == other.shape[0]:
                    res = Vector(other.shape[0])
                    for ii in range(self.shape[0]):
                        for jj in range(self.shape[1]):
                            res[ii][0] = self.data[ii][jj] * other[jj][0]
                    return res
                else:
                    print("Mismatch dimension between Matrix instances.")
                    return
        except:
            print("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __rmul__(self, other):
        if not isinstance(other, Matrix):
            print("Right member of the addition operator is not a Matrix instance.")
            return
        try:
            pass
        except:
            print("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        radical = "Matrix(["
        end = "])"
        for line in self.data:
            radical += str(line) + ' '
        return radical[:-1] + end
    
    
class Vector(Matrix):
    def __init__(self, *arg):
        super().__init__(self, *arg)
        
    
    def dot(self, v:Vector):
        pass
    
    def __add__(self, other):
        pass
        
    def __radd__(self, other):
        pass
    
    def __sub__(self, other):
        pass
        
    def __rsub__(self, other):
        pass
    
    def __truediv__(self, other):
        pass
        
    def __rtruediv__(self, other):
        pass
    
    def __mul__(self, other):
        pass
        
    def __rmul__(self, other):
        pass
    
    def __str__(self):
        pass
    
    def __repr__():
        pass