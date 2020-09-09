class Clause:
    def __init__(self):
        self.list = []

    def __str__(self):
        s = ""
        for literal in self.list:
            s = s + str(literal.value) + " "
        return s

    def contains_varible(self, literal):
        literal_values = [abs(literal.value) for literal in self.list]
        if literal in literal_values:
            return True
        else:
            return False

    def check_if_remove(self, variable_value):
        literal_values = [literal.value for literal in self.list]
        # print(variable_value)
        # print(literal_values)
        if variable_value in literal_values:
            # print("true")
            return True
        else:
            # print("false")
            return False
