""" Function to rotate a N x M matrix by 90 degrees in clockwise direction """

def rotate_matrix_clockwise(matrix):
    """
    Parameters:
        matrix : List[List[int]] - The matrix to rotate.

    Time Complexity: O(N * M) - where N is the number of rows and M is the number of columns in the matrix.
    Space Complexity: O(N * M) - for the new rotated matrix.

    Examples:
        >>> rotate_matrix_clockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        >>> rotate_matrix_clockwise([[1]])
        [[1]]
        >>> rotate_matrix_clockwise([[1, 2], [3, 4]])
        [[3, 1], [4, 2]]
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    rotated_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotated_matrix[j][rows - 1 - i] = matrix[i][j]

    return rotated_matrix

if __name__ == "__main__":
    matrix_input = input("Enter the matrix rows separated by spaces (use ';' for new rows): ")
    try:
        matrix = [list(map(int, row.split())) for row in matrix_input.split(';')]
        rotated = rotate_matrix_clockwise(matrix)
        print("Rotated Matrix:")
        for row in rotated:
            print(row)
    except ValueError:
        print("Please enter a valid matrix.")
