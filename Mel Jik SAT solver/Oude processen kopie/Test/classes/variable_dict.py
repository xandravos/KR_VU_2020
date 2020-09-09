class Variable_dict():
    def __init__(self, variable_dict):
        self.variable_dict = variable_dict

    def set_values(self, values_to_set):
        for value in values_to_set:
            if value > 0:
                self.variable_dict[value] = True

            else:
                self.variable_dict[abs(value)] = False
