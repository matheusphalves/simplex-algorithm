import time
import numpy as np
from simplex_algorithm.Interaction import Interaction

class SimplexSolver():
    '''
    Class is responsable to solve maximization Linear Programming Problems.
        @author: Matheus Phelipe
    '''
    def __init__(self, matrix_a, matrix_b, matrix_c, max_iteractions, has_slack_var = True) -> None:
        
        try:
            self.convert_data_2_np_array(matrix_a, matrix_b, matrix_c)
            self.has_slack_var = has_slack_var
            self.is_done = False
            self.iterations = 0
            self.max_iteractions = max_iteractions
            self.previous_interactions = []
        except Exception as ex:
            print(f'Failed to create numpy matrices\n {ex}')

    def convert_data_2_np_array(self, matrix_a, matrix_b, matrix_c):
        self.matrix_a = np.array([item for item in matrix_a])
        self.matrix_b = np.reshape(np.array([item for item in matrix_b]), (len(matrix_b), 1))
        self.matrix_c = np.reshape(np.array([item for item in matrix_c]), (1, len(matrix_c)))

    
    def start(self, set_B, set_N):
        if self.has_slack_var is False:
            self.add_slack_variable()
        
        start = time.time()

        while self.is_done is False and self.iterations <= self.max_iteractions:
            print(f'Starting iteration {self.iterations}')
            self.make_iteration(set_B, set_N)
            set_B = [2,3,4]
            Set_N = [0, 1]
            print(f'Z score:{self.previous_interactions[-1].z_value}')
            print(f'XB matrix: {self.previous_interactions[-1].matrix_XB}')
            self.iterations += 1

        end = time.time()
        print(f'Simplex Iteractions finished: {end-start}')
        return self.previous_interactions

    
    def add_slack_variable(self):
        pass
        

    def make_iteration(self, set_B, set_N):
        try:
            matrix_B = self.matrix_a[:, set_B]
            matrix_N = self.matrix_a[:, set_N]
            matrix_CB = self.matrix_c[:, set_B]
            self.calculate(matrix_B=matrix_B, matrix_CB=matrix_CB, set_B=set_B, set_N=set_N, matrix_N=matrix_N)
            if self.is_done is False:
                self.calculate_leaving_variable()
                self.calculate_alpha()
        except Exception as ex:
            print(f'Failed on make_iteration method\n{ex}')

    def calculate(self, matrix_B, matrix_CB, set_B, set_N, matrix_N):
        b_inverted = np.linalg.inv(matrix_B)
        u = np.matmul(matrix_CB, b_inverted)
        xb = np.matmul(b_inverted, self.matrix_b)
        z = np.matmul(u, self.matrix_b)[:,0][0]

        list_z_index = [np.matmul(u, self.matrix_a[:, index])[0] - self.matrix_c[:, index][0] for index in set_N]

        self.is_done = all(i >= 0 for i in list_z_index)
        self.previous_interactions.append(Interaction(matrix_B, set_B, matrix_N, set_N, xb, z))

    def calculate_leaving_variable(self):
        pass

    def calculate_alpha(self, l_set):
        pass

    def generate_report(self):
        pass