import pytest
from src.models.challenges_models import QueryN, RecycleMatrix
from pydantic import ValidationError

def test_recycle_matrix_validation_success():
    valid_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    model = RecycleMatrix(root=valid_matrix)
    assert model.root == valid_matrix

def test_recycle_matrix_validation_failure_not_3x3():
    invalid_matrix = [[1, 2], [3, 4], [5, 6]]
    with pytest.raises(ValueError, match='The matrix must be 3x3 integers'):
        RecycleMatrix(root=invalid_matrix)

def test_recycle_matrix_validation_failure_non_integer():
    invalid_matrix = [[1, 2, 3], [4, "x", 6], [7, 8, 9]] 
    with pytest.raises(ValidationError, match="Input should be a valid integer"):
        RecycleMatrix(root=invalid_matrix)


def test_query_n_validation_success():
    valid_n = 10
    model = QueryN(n=valid_n)
    assert model.n == valid_n

def test_query_n_validation_failure_negative():
    invalid_n = -1
    with pytest.raises(ValueError, match="Input should be greater than 0"):
        QueryN(n=invalid_n)

def test_query_n_validation_failure_zero():
    invalid_n = 0
    with pytest.raises(ValueError, match="Input should be greater than 0"):
        QueryN(n=invalid_n)