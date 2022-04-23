from simplex_algorithm.SimplexSolver import SimplexSolver


#matrix_A = [
#    [1, 0.5, 1, 0, 0],
#    [6, 2, 0, 1, 0],
#    [5, 4, 0, 0, 1]]
#matrix_B = [44, 250, 280]
#matrix_C = [60, 40, 0, 0, 0]

#matrix_A = [
#    [1, 0, 1, 0, 0],
#    [0, 1, 0, 1, 0],
#    [3, 2, 0, 0, 1]]
#matrix_B = [4, 6, 18]
#matrix_C = [3, 5, 0, 0, 0]

matrix_A = [
    [1, 3, 1, 0],
    [1, 1, 0, 1]]
matrix_B = [8, 4]
matrix_C = [1, 2, 0, 0, 0]

simplex = SimplexSolver(matrix_a=matrix_A, matrix_b=matrix_B, matrix_c=matrix_C, max_iteractions=10)

simplex.start([2,3], [0, 1])