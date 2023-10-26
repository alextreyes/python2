def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    diagonal1_sum = 0  
    diagonal2_sum = 0  
    matrix_size = len(matrix)

    for i in range(matrix_size):
        diagonal1_sum += matrix[i][i]  
        diagonal2_sum += matrix[i][matrix_size - i - 1]  

    return diagonal1_sum + diagonal2_sum