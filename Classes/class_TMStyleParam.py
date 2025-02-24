class TMStyleParam:

    def __init__(self, p_value: str | bool, p_sign: str = "$"):
        self.value = p_value
        self.sign = p_sign

    def result_bool_param(self):
        if isinstance(self.value, bool) and self.value:
            return self.sign
        else:
            return ""
