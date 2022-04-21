from simplex_algorithm.SimplexSolver import SimplexSolver


matrix_A = [
    [1, 0.5, 1, 0, 0],
    [6, 2, 0, 1, 0],
    [5, 4, 0, 0, 1]]
matrix_B = [44, 250, 280]
matrix_C = [60, 40, 0, 0, 0]

simplex = SimplexSolver(matrix_a=matrix_A, matrix_b=matrix_B, matrix_c=matrix_C)