class Super:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

class S(Super):
##    def __init__(self, param1, param2):
##        self.param1 = param1
##        self.param2 = param2

    def __str__(self):
        return self.param1 + self.param2

    def __repr__(self):
        return "this"
