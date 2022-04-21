import numpy as np

class SimplexSolver():
    '''
    Class is responsable to solve maximization Linear Programming Problems.
        @author: Matheus Phelipe
    '''
    def __init__(self, matrix_a, matrix_b, matrix_c, max_iterations, has_slack_var = True) -> None:
        
        try:
            self.convert_2_np_array(matrix_a, matrix_b, matrix_c)
            self.has_slack_var = has_slack_var
            self.is_done = False
            self.iterations = 0
            self.max_iterations = max_iterations
        except Exception as ex:
            print(f'Failed to create numpy matrices\n {ex}')

    def convert_data_2_np_array(self, matrix_a, matrix_b, matrix_c):
        self.matrix_a = np.array([item for item in matrix_a])
        self.matrix_b = np.reshape(np.array([item for item in matrix_b]), (len(matrix_b), 1))
        self.matrix_c = np.reshape(np.array([item for item in matrix_c]), (1, len(matrix_c)))

    
    def start(self):
        if(self.has_slack_var):
            self.add_slack_variable()
        
        while(self.is_done is False or self.iterations == self.max_iterations):
            print('Starting iteration {}', self.iterations)
            self.make_iteration()
            pass
    
    def add_slack_variable(self):
        pass
        

    def make_iteration(self):
        pass

    def evaluate(self):
        pass

    def generate_report(self):
        pass