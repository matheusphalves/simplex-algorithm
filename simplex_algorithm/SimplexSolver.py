import time
import numpy as np
import json
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
            print(f'Starting iteraction {self.iterations}')
            b_inverted, list_z_index, matrix_XB = self.make_iteraction(set_B, set_N)
            print(f'Z score:{self.previous_interactions[-1].z_value}')
            self.iterations += 1
            if self.is_done is False:
                index_entering = self.compare_tuples(list_z_index)[1]
                leaving_data = self.calculate_leaving_variable(b_inverted, index_entering)
                alpha_data = self.calculate_alpha(leaving_data, matrix_XB, set_B)
                index_leaving = set_B[alpha_data[0][1]]
                print(f'XB({index_leaving}) is leaving. XB({index_entering}) is entering')
                set_B = self.swap_matrices_index(set_B, index_leaving, index_entering)
                set_N = self.swap_matrices_index(set_N, index_entering, index_leaving)

        end = time.time()
        print(f'Simplex Iteractions has finished: {end-start}')
        self.generate_report()
        return self.previous_interactions

    
    def add_slack_variable(self):
        pass

    def swap_matrices_index(self, set_list, leaving, entering):
        aux = []
        for index in set_list:
            if index == leaving:
                aux.append(entering)
            else:
                aux.append(index)
        return aux


    def make_iteraction(self, set_B, set_N):
        try:
            matrix_B = self.matrix_a[:, set_B]
            matrix_N = self.matrix_a[:, set_N]
            matrix_CB = self.matrix_c[:, set_B]
            return self.calculate(matrix_B=matrix_B, matrix_CB=matrix_CB, set_B=set_B, set_N=set_N, matrix_N=matrix_N)
        except Exception as ex:
            print(f'Failed on make_iteraction method\n{ex}')

    def calculate(self, matrix_B, matrix_CB, set_B, set_N, matrix_N):
        b_inverted = np.linalg.inv(matrix_B)
        u = np.matmul(matrix_CB, b_inverted)
        matrix_XB = np.matmul(b_inverted, self.matrix_b)
        z = np.matmul(u, self.matrix_b)[:,0][0]

        list_z_index = [(np.matmul(u, self.matrix_a[:, index])[0] - self.matrix_c[:, index][0], index) for index in set_N]

        self.previous_interactions.append(Interaction(matrix_B, set_B, matrix_N, set_N, matrix_XB, z))
        self.is_done = all(i[0] >= 0 for i in list_z_index)

        return b_inverted, list_z_index, matrix_XB

    def compare_tuples(self, tuple): #(z_value, index)
        smaller = tuple[0]
        for index in range(1, len(tuple)):
            if tuple[index][0] < smaller[0]:
                smaller = tuple[index]
        return smaller

    def calculate_leaving_variable(self, b_inverted, index_N):
        y_index_N = np.matmul(b_inverted, self.matrix_a[:, index_N])
        greater_0 = []
        for index in range(len(y_index_N)):
            if y_index_N[index] > 0:
                greater_0.append(index)

        return y_index_N, greater_0

    def calculate_alpha(self, leaving_data, matrix_XB, set_B):
        alpha_list = [(matrix_XB[index][0]/ leaving_data[0][index], index) for index in leaving_data[1]]
        smaller = alpha_list[0]
        index_leaving = set_B[0]
        for index in range(1, len(alpha_list[0])):
            if(alpha_list[index][0]<smaller[0]):
                smaller = alpha_list[index]
                index_leaving = set_B[index]

        return smaller, index_leaving #retorna posição que deve ser removida

    def generate_report(self):
        #dict_list = [item.__dict__ for item in self.previous_interactions]
        #return json.dumps(dict_list)
        print(self.previous_interactions)