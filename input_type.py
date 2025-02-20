class InputTypeChecker:
    def __init__(self, user_input):
        self.user_input = user_input
        self.input_type, self.value = self._determine_type()

    def _determine_type(self):
        try:
            return "Integer", int(self.user_input)
        except ValueError:
            pass

        try:
            return "Float", float(self.user_input)
        except ValueError:
            pass

        if self.user_input.lower() in ['true', 'false']:
            return "Boolean", self.user_input.lower() == 'true'

        if self.user_input.lower() in ["none", "null"]:
            return "NoneType", None

        return "String", self.user_input

    def get_type(self):
        return self.input_type

    def get_value(self):
        return self.value


