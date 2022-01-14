from unittest import TestCase
import unittest
import matrix

def check_data_equality(expected, test):
    n_line = len(expected)
    n_col = len(expected[0])
    for ii in range(n_line):
        for jj in range(n_col):
            if expected[ii][jj] != test[ii][jj]:
                return False
    return True


def check_shape(expected, test):
    if expected == test:
        return True
    return False


class TestMatrixMethods(TestCase):
    def test_basic_instance_list_1(self):
        expected_val = [[0, 0], [0, 0]]
        expected_shape = (2,2)
        M = matrix.Matrix(expected_val)
        self.assertTrue(check_data_equality(expected_val, M.data) and check_shape(expected_shape, M.shape))

    def test_basic_instance_list_2(self):
        expected_val = [[1, 2], [3, 4]]
        expected_shape = (2,2)
        M = matrix.Matrix(expected_val)
        self.assertTrue(check_data_equality(expected_val, M.data) and check_shape(expected_shape, M.shape))

    def test_basic_instance_list_3(self):
        expected_val = [[21], [42]]
        expected_shape = (2,1)
        M = matrix.Matrix(expected_val)
        self.assertTrue(check_data_equality(expected_val, M.data) and check_shape(expected_shape, M.shape))

    def test_basic_instance_list_4(self):
        expected_val = [[21, 42, 63]]
        expected_shape = (1,3)
        M = matrix.Matrix(expected_val)
        self.assertTrue(check_data_equality(expected_val, M.data) and check_shape(expected_shape, M.shape))


    def test_basic_instance_shape_1(self):
        expected_val = [[0, 0], [0, 0]]
        expected_shape = (2,2)
        M = matrix.Matrix(expected_val)
        self.assertTrue(check_data_equality(expected_val, M.data) and check_shape(expected_shape, M.shape))

    def test_basic_instance_shape_2(self):
        expected_val = [[0], [0], [0]]
        expected_shape = (3,1)
        M = matrix.Matrix(expected_val)
        self.assertTrue(check_data_equality(expected_val, M.data) and check_shape(expected_shape, M.shape))

    def test_basic_instance_shape_3(self):
        expected_val = [[0, 0, 0]]
        expected_shape = (1,3)
        M = matrix.Matrix(expected_val)
        self.assertTrue(check_data_equality(expected_val, M.data) and check_shape(expected_shape, M.shape))

    def test_basic_instance_shape_4(self):
        expected_val = [[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]
        expected_shape = (5,6)
        M = matrix.Matrix(expected_val)
        self.assertTrue(check_data_equality(expected_val, M.data) and check_shape(expected_shape, M.shape))
    
    def test_error_instance_1(self):
        # No argument
        with self.assertRaises(ValueError):
            matrix.Matrix()

    def test_error_instance_2(self):
        # None as argument
        with self.assertRaises(TypeError):
            matrix.Matrix(None)
        
    def test_error_instance_3(self):
        # str as argument
        with self.assertRaises(TypeError):
            matrix.Matrix("toto")
        
    def test_error_instance_4(self):
        # integer as argument
        with self.assertRaises(TypeError):
            matrix.Matrix(3)
        
    def test_error_instance_5(self):
        # float as argument
        with self.assertRaises(TypeError):
            matrix.Matrix(3.142)
        
    def test_error_instance_6(self):
        # complex as argument
        with self.assertRaises(TypeError):
            matrix.Matrix(complex(4, 2))
        
    def test_error_instance_7(self):
        # double nested list (3 squared brackets) as argument
        with self.assertRaises(TypeError):
            matrix.Matrix([[[1, 2, 3]]])
        
    def test_error_instance_8(self):
        # Incorrect tuple as argument
        with self.assertRaises(ValueError):
            matrix.Matrix((1, 2, 3))
        
    def test_addition_1(self):
        # basic (2x2) with (2x2) addition matrix with shape instance method
        m1 = matrix.Matrix((2, 2))
        m2 = matrix.Matrix((2, 2))
        m3 = m1 + m2
        expected_val = [[0, 0], [0, 0]]
        expected_shape = (2, 2)
        self.assertTrue(isinstance(m3, matrix.Matrix) and check_data_equality(expected_val, m3.data) and check_shape(expected_shape, m3.shape))
        
    def test_addition_2(self):
        # basic (3x3) with (3x3) addition matrix with nested list instance method
        m1 = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = matrix.Matrix([[1, 1, 1], [2, 3, 2], [5, 4, 5]])
        m3 = m1 + m2
        expected_val = [[2, 3, 4], [6, 8, 8], [12, 12, 14]]
        expected_shape = (3, 3)
        self.assertTrue(isinstance(m3, matrix.Matrix) and check_data_equality(expected_val, m3.data) and check_shape(expected_shape, m3.shape))

    def test_addition_3(self):
        # basic (3x3) with (3x3) addition matrix with nested list instance method. The second matrix has all it component negative
        m1 = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = matrix.Matrix([[-1, -1, -1], [-2, -3, -2], [-5, -4, -5]])
        m3 = m1 + m2
        expected_val = [[0, 1, 2], [2, 2, 4], [2, 4, 4]]
        expected_shape = (3, 3)
        self.assertTrue(isinstance(m3, matrix.Matrix) and check_data_equality(expected_val, m3.data) and check_shape(expected_shape, m3.shape))

    def test_substraction_1(self):
        # basic (2x2) with (2x2) substraction matrix with shape instance method
        m1 = matrix.Matrix((2, 2))
        m2 = matrix.Matrix((2, 2))
        m3 = m1 - m2
        expected_val = [[0, 0], [0, 0]]
        expected_shape = (2, 2)
        self.assertTrue(isinstance(m3, matrix.Matrix) and check_data_equality(expected_val, m3.data) and check_shape(expected_shape, m3.shape))
        
    def test_substraction_2(self):
        # basic (3x3) with (3x3) substraction matrix with nested list instance method
        m1 = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = matrix.Matrix([[1, 1, 1], [2, 3, 2], [5, 4, 5]])
        m3 = m1 - m2
        expected_val = [[0, 1, 2], [2, 2, 4], [2, 4, 4]]
        expected_shape = (3, 3)
        self.assertTrue(isinstance(m3, matrix.Matrix) and check_data_equality(expected_val, m3.data) and check_shape(expected_shape, m3.shape))

    def test_substraction_3(self):
        # basic (3x3) with (3x3) substraction matrix with nested list instance method. The second matrix has all it component negative
        m1 = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = matrix.Matrix([[-1, -1, -1], [-2, -3, -2], [-5, -4, -5]])
        m3 = m1 - m2
        expected_val = [[2, 3, 4], [6, 8, 8], [12, 12, 14]]
        expected_shape = (3, 3)
        self.assertTrue(isinstance(m3, matrix.Matrix) and check_data_equality(expected_val, m3.data) and check_shape(expected_shape, m3.shape))

# ---------------------------------------------------------- #
# ________________________   MAIN   ________________________ #
# ---------------------------------------------------------- #
if __name__ == '__main__':
    unittest.main()