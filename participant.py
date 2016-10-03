class Participant:
    def __init__(self):
        self.roles = None
        self.experience = None
        self.projectSource = None
        self.Q19 = None
        self.Q50_1 = None
        self.Q50_2 = None
        self.Q34 = None
        self.Q36 = None

    def __str__(self):
        return "<Participant object>\n" \
                + "\tRoles: %s\n" % str(self.roles) \
                + "\tExperience: %s\n" % str(self.experience)

    def setRoles(self, rolesObj):
        self.roles = rolesObj

    def setExperience(self, expObject):
        self.experience = expObject

    def setProjectSource(self, projectSourceObj):
        self.projectSource = projectSourceObj

    def setQ19(self, q19Response):
        self.Q19 = q19Response

    def setQ50_1(self, response):
        self.Q50_1 = response

    def setQ50_2(self, response):
        self.Q50_2 = response

    def setQ34(self, response):
        self.Q34 = response

    def setQ36(self, response):
        self.Q36 = response