class Participant:
    def __init__(self):
        self.roles = None
        self.q19 = None
        self.q50_1 = None
        self.q50_2 = None
        self.q34 = None
        self.q36 = None

    def setRoles(self, rolesObj):
        self.roles = rolesObj

    def setQ19(self, q19Response):
        self.q19 = q19Response

    def setQ50_1(self, response):
        self.q50_1 = response

    def setQ50_2(self, response):
        self.q50_2 = response

    def setQ34(self, response):
        self.q34 = response

    def setQ36(self, response):
        self.q36 = response