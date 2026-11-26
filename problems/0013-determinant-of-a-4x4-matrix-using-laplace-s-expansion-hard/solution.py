def determinant_4x4(matrix):

    # Base case: 2x2 determinant
    if len(matrix) == 2:
        return (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )

    det = 0

    # Laplace Expansion along first row
    for col in range(len(matrix)):

        # Create minor matrix
        minor = [
            row[:col] + row[col + 1:]
            for row in matrix[1:]
        ]

        # Calculate sign (+ - + -)
        sign = (-1) ** col

        # Recursive determinant calculation
        det += sign * matrix[0][col] * determinant_4x4(minor)

    return det
