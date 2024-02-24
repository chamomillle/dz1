import pytest
from dz.eleven import Matrix

@pytest.mark.parametrize(
        ('rows', 'cols', 'elements'),
        [
        (2, 2, [[1, 1],[1, 1]])
        ]
)

def test_init(rows, cols, elements):
    m = Matrix(rows, cols, elements)
    assert m.rows == rows
    assert m.cols == cols
    assert m.elements == elements
    
def test_init_default():
    m1 = Matrix()
    assert m1.rows == 0
    assert m1.cols == 0
    assert m1.elements == []

def test_input(mocker):
    mocker.patch('builtins.input', side_effect = ['2', '3', '2 4 2', '1 4 7'])
    matrix = Matrix()
    matrix.input_matrix()
    assert matrix.rows == 2
    assert matrix.cols == 3
    assert matrix.elements == [[2, 4, 2], [1, 4, 7]]
        
@pytest.mark.xfail(raises=ValueError)
def test_much_el(mocker):
    mocker.patch('builtins.input', side_effect = ['2', '3', '2 4 2', '1 4 7 9'])
    matrix = Matrix()
    matrix.input_matrix()
    
@pytest.mark.parametrize(
        ('rows1', 'cols1', 'elements1', 'result'),
        [
        (2, 4, [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]], '1.0 1.0 1.0 1.0\n1.0 1.0 1.0 1.0\n'),
        (2, 3, [[3.14, 1.0, 1.0], [1.0, 1.0, 3.14]], '3.14 1.0 1.0\n1.0 1.0 3.14\n')
        ]
)

def test_output(rows1, cols1, elements1, result):
    assert str(Matrix(rows1, cols1, elements1)) == result