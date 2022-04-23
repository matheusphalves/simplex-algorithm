class Interaction():
    '''Class stores the result of a Simplex interaction'''
    def __init__(self, matrix_B, set_B, matrix_N, set_N, matrix_XB, z_value) -> None:
        self.matrix_B = matrix_B
        self.set_B = set_B
        self.matrix_N = matrix_N
        self.set_N = set_N
        self.z_value = z_value
        self.matrix_XB = matrix_XB

