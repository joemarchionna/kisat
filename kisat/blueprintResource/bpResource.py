class _API_BP_RESOURCE(object):
    def __init__(self, prefix: str, rule: str):
        self.prefix = prefix
        self.rule = rule

    def __radd__(self, other) -> str:
        return other + self.__str__()

    def __add__(self, other) -> str:
        return other + self.__str__()

    def __repr__(self):
        rs = "{}{}".format(self.prefix, self.rule)
        return rs

    def __str__(self):
        return self.__repr__()
