#!/usr/bin/python3

"""A matrix multiplication function definition"""

def matrix_mul(m_a, m_b):
    """Multiply two matrices

    Args:
        m_a: The first
        m_b: The second
    Raises:
        TypeError: parameters are not a list of lists of ints or floats.
        TypeError: parameters are empty.
        TypeError: parameters with similar sized rows.
        ValueError: matrix cannot be multiplied.
    Returns:
        The multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        w_rw = []
        for c in range(len(m_b)):
            w_rw.append(m_b[c][r])
        inverted_b.append(w_rw)

    w_matrix = []
    for row in m_a:
        w_rw = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            w_rw.append(prod)
        w_matrix.append(w_rw)

    return w_matrix
