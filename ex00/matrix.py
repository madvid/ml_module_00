from __future__ import annotations
from sys import stderr

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
                new.data[jj][ii] = self.data[ii][jj]
        return new
        
        
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ArithmeticError("Right member of the addition operator is not a Matrix instance.")
        if self.shape != other.shape:
            raise ArithmeticError("Incompatible shape.")
        try:
            res = Matrix(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = self.data[ii][jj] + other.data[ii][jj]
            return res
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")
      

    def __radd__(self, other):
        if not isinstance(other, Matrix):
            raise ArithmeticError("Left member of the addition operator is not a Matrix instance.")
        if self.shape != other.shape:
            raise ArithmeticError("Incompatible shape.")
        try:
            res = Matrix(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = other.data[ii][jj] + self.data[ii][jj]
            return res
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise ArithmeticError("Right member of the subtraction operator is not a Matrix instance.")
        if self.shape != other.shape:
            raise ArithmeticError("Incompatible shape.")
        try:
            res = Matrix(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = self.data[ii][jj] - other.data[ii][jj]
            return res
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __rsub__(self, other):
        if not isinstance(other, Matrix):
            raise ArithmeticError("Left member of the substraction operator is not a Matrix instance.")
        if self.shape != other.shape:
            raise ArithmeticError("Incompatible shape.")
        try:
            res = Matrix(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = other.data[ii][jj] - self.data[ii][jj]
            return res
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __truediv__(self, other):
        if isinstance(other, Matrix):
            print("Warning: You should not try to divide a Matrix by another Matrix.", file = stderr)
            try:
                if other.shape == (1,1):
                    res = Matrix(self.shape)
                    for ii in range(self.shape[0]):
                        for jj in range(self.shape[1]):
                            res.data[ii][jj] = self.data[ii][jj] / other.data[0][0]
                    return res      
            except:
                raise ArithmeticError("Divisor issue: either Matrix is not of dimension (1x1)" \
                    + " or prior corruption of the Matrix object has been made" \
                        + " or you are trying to divide by Matrix([[0]]).")
        if not isinstance(other, (int, float)):
            raise ArithmeticError("Right member of the division operator is not a scalar.")
        if isinstance(other, (int, float)) and other == 0:
            raise ZeroDivisionError("This is a bad idea to divide by 0.")
        try:
            res = Matrix(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = self.data[ii][jj] / other
            return res
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __rtruediv__(self, other):
        print("Warning: You should not try to divide by Matrix. You must know what you are doing.", file = stderr)
        try:
            if self.shape != (1,1):
                raise ArithmeticError("Divisor issue: either Matrix is not of dimension (1x1)")
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
                raise ArithmeticError("Error: Right member of the division is not a (1x1) dimensional Matrix instance.")
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __mul__(self, other):
        if not isinstance(other, (Matrix, int, float, Vector)):
            raise ArithmeticError("Right member of the multiplication operator is not a Matrix instance.")
        try:
            if isinstance(other, (int, float)):
                res = Matrix(self.shape)
                for ii in range(self.shape[0]):
                    for jj in range(self.shape[1]):
                        res.data[ii][jj] = self.data[ii][jj] * other
                return res
            elif isinstance(other, Matrix):
                if self.shape[1] == other.shape[0]:
                    res = Matrix((self.shape[0], other.shape[1]))
                    for ii in range(self.shape[0]):
                        for kk in range(other.shape[1]):
                            for jj in range(self.shape[1]):
                                res.data[ii][kk] += self.data[ii][jj] * other.data[jj][kk]
                    return res
                else:
                    raise ArithmeticError("Mismatch dimension between Matrix instances.")
            elif isinstance(other, Vector):
                if self.shape[1] == other.shape[0]:
                    res = Vector(other.shape)
                    for ii in range(self.shape[0]):
                        for jj in range(self.shape[1]):
                            res.data[ii][0] = self.data[ii][jj] * other[jj][0]
                    return res
                else:
                    raise ArithmeticError("Mismatch dimension between Matrix instances.")
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __rmul__(self, other):
        if not isinstance(other, (Matrix, int, float, Vector)):
            raise ArithmeticError("Right member of the addition operator is not a Matrix instance.")
        try:
            if isinstance(other, (int, float)):
                res = Matrix(self.shape)
                for ii in range(self.shape[0]):
                    for jj in range(self.shape[1]):
                        res.data[ii][jj] = self.data[ii][jj] * other
                return res
            elif isinstance(other, Matrix):
                if other.shape[1] == self.shape[0]:
                    res = Matrix((other.shape[0], self.shape[1]))
                    for ii in range(other.shape[0]):
                        for kk in range(self.shape[1]):
                            for jj in range(other.shape[1]):
                                res.data[ii][kk] += other.data[ii][jj] * self.data[jj][kk]
                    return res
                else:
                    raise ArithmeticError("Mismatch dimension between Matrix instances.")
            elif isinstance(other, Vector):
                if other.shape[1] == self.shape[0]:
                    res = Vector(other.shape)
                    for ii in range(other.shape[0]):
                        for jj in range(other.shape[1]):
                            res.data[ii][0] += other.data[ii][jj] * self.data[jj][0]
                    return res
                else:
                    raise ArithmeticError("Mismatch dimension between Matrix instances.")
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        try:
            radical = "Matrix(["
            end = "])"
            for line in self.data:
                radical += str(line) + ' '
            return radical[:-1] + end
        except:
            raise AttributeError("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")
    
    
class Vector(Matrix):
    def __init__(self, *args):
        super().__init__(*args)
        if all([l != 1 for l in self.shape]):
            raise ValueError("Data should have a dimension with size 1: shape == (n, 1) or (1, m).")
 

    def T(self):
        new = Vector(self.shape[::-1])
        for ii in range(self.shape[0]):
            for jj in range(self.shape[1]):
                new.data[jj][ii] = self.data[ii][jj]
        return new


    def dot(self, v:Vector):
        if not isinstance(v, Vector):
            raise TypeError("dot product can be applied only between Vector objects.")
        if (self.shape != v.shape) or (self.shape[1] != 1):
            raise TypeError("Vectors should be of same dimension and be 2 column vectors.")
        try:
            res = 0
            for ii in range(self.shape[0]):
                res += self.data[ii][0] * v.data[ii][0]
            return res
        except:
            raise AttributeError("Something wrong happened, possible corruption of the Vector instance prior to the operation.")
        
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError("Right member of the addition operator is not a Vector instance.")
        if self.shape != other.shape:
            raise ArithmeticError("Incompatible shape.")
        try:
            res = Vector(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = self.data[ii][jj] + other.data[ii][jj]
            return res
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Vector instance prior to the operation.")
      

    def __radd__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError("Left member of the addition operator is not a Vector instance.")
        if self.shape != other.shape:
            raise ArithmeticError("Incompatible shape.")
        try:
            res = Vector(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = other.data[ii][jj] + self.data[ii][jj]
            return res
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Vector instance prior to the operation.")
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError("Right member of the subtraction operator is not a Vector instance.")
        if self.shape != other.shape:
            raise ArithmeticError("Incompatible shape.")
        try:
            res = Vector(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = self.data[ii][jj] - other.data[ii][jj]
            return res
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Vector instance prior to the operation.")


    def __rsub__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError("Left member of the substraction operator is not a Vector instance.")
        if self.shape != other.shape:
            raise ArithmeticError("Incompatible shape.")
        try:
            res = Vector(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = other.data[ii][jj] - self.data[ii][jj]
            return res
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Vector instance prior to the operation.")

    
    def __truediv__(self, other):
        if isinstance(other, Vector):
            print("Warning: You should not try to divide a Vector by another Vector.", file = stderr)
            try:
                if other.shape == (1,1):
                    res = Vector(self.shape)
                    for ii in range(self.shape[0]):
                        for jj in range(self.shape[1]):
                            res.data[ii][jj] = self.data[ii][jj] / other.data[0][0]
                    return res      
            except:
                raise ArithmeticError("Divisor issue: either Vector is not of dimension (1x1)" \
                    + " or prior corruption of the Vector object has been made" \
                        + " or you are trying to divide by Vector([[0]]).")
        if not isinstance(other, (int, float)):
            raise ArithmeticError("Right member of the division operator is not a scalar.")
        if isinstance(other, (int, float)) and other == 0:
            raise ZeroDivisionError("This is a bad idea to divide by 0.")
        try:
            res = Vector(self.shape)
            for ii in range(self.shape[0]):
                for jj in range(self.shape[1]):
                    res.data[ii][jj] = self.data[ii][jj] / other
            return res
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Vector instance prior to the operation.")


    def __rtruediv__(self, other):
        print("You should not try to divide by a Vector. You must know what you are doing.", file = stderr)
        try:
            if self.shape != (1,1):
                raise ArithmeticError("Right member of the division operator is not a (1x1) Vector.")
            if isinstance(other, Vector):
                if self.shape == (1,1):
                    res = Vector(other.shape)
                    for ii in range(other.shape[0]):
                        for jj in range(other.shape[1]):
                            res = other.data[ii][jj] / self.data[0][0]
                    return res
            
            elif isinstance(other, (int, float)):
                return Vector([[other / self.data[0][0]]])
            else:
                raise ArithmeticError("Error: Right member of the division is not a (1x1) dimensional Vector instance.")
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Vector instance prior to the operation.")


    def __mul__(self, other):
        if not isinstance(other, (Matrix, int, float, Vector)):
            raise ArithmeticError("Right member of the multiplication operator is not a Matrix, int, float or Vetor instance.")
        try:
            if isinstance(other, (int, float)):
                res = Vector(self.shape)
                for ii in range(self.shape[0]):
                    for jj in range(self.shape[1]):
                        res.data[ii][jj] = self.data[ii][jj] * other
                return res
            elif isinstance(other, Matrix):
                if self.shape[1] == other.shape[0]:
                    res = Vector((self.shape[0], other.shape[1]))
                    for ii in range(self.shape[0]):
                        for kk in range(other.shape[1]):
                            for jj in range(self.shape[1]):
                                res.data[ii][kk] += self.data[ii][jj] * other.data[jj][kk]
                    return res
                else:
                    raise ArithmeticError("Mismatch dimension between Vector instances.")
            elif isinstance(other, Vector):
                if self.shape[1] == other.shape[0]:
                    res = Vector(other.shape)
                    for ii in range(self.shape[0]):
                        for jj in range(self.shape[1]):
                            res.data[ii][0] += self.data[ii][jj] * other.data[jj][0]
                    return res
                else:
                    raise ArithmeticError("Mismatch dimension between Matrix instances.")
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Matrix instance prior to the operation.")


    def __rmul__(self, other):
        if not isinstance(other, (int, float, Vector, Matrix)):
            raise ArithmeticError("Right member of the addition operator is not a Matrix, int, float or Vector instance.")
        try:
            if isinstance(other, (int, float)):
                res = Vector(self.shape)
                for ii in range(self.shape[0]):
                    for jj in range(self.shape[1]):
                        res.data[ii][jj] = self.data[ii][jj] * other
                return res
            elif isinstance(other, Vector):
                if other.shape[1] == self.shape[0]:
                    res = Vector((other.shape[0], self.shape[1]))
                    for ii in range(other.shape[0]):
                        for kk in range(self.shape[1]):
                            for jj in range(other.shape[1]):
                                res.data[ii][kk] += other.data[ii][jj] * self.data[jj][kk]
                    return res
                else:
                    raise ArithmeticError("Mismatch dimension between Vector instances.")
            elif isinstance(other, Matrix):
                if other.shape[1] == self.shape[0]:
                    res = Vector((other.shape[0], self.shape[1]))
                    for ii in range(other.shape[0]):
                        for jj in range(other.shape[1]):
                            res.data[ii][0] += other.data[ii][jj] * self.data[jj][0]
                    return res
                else:
                    raise ArithmeticError("Mismatch dimension between Vector instances.")
        except:
            raise  AttributeError("Something wrong happened, possible corruption of the Vector instance prior to the operation.")


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        radical = "Vector(["
        end = "])"
        for line in self.data:
            radical += str(line) + ' '
        return radical[:-1] + end