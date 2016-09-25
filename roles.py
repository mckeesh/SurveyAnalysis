class Roles:
    def __eq__(self, other):
      return other.isSoftEng == self.isSoftEng and \
             other.isSysEng == self.isSysEng and \
             other.isSysAdmin == self.isSysAdmin and \
             other.isProjMaint == self.isProjMaint and \
             other.isProjManag == self.isProjManag and \
             other.isOtherRole == self.isOtherRole and \
             other.isSysArch == self.isSysArch and \
             other.isDevOps == self.isDevOps

    def __init__(self, roleList=[False]*8):
        self.isSoftEng, \
        self.isSysEng, \
        self.isSysAdmin, \
        self.isProjMaint, \
        self.isProjManag, \
        self.isOtherRole, \
        self.isSysArch, \
        self.isDevOps = roleList
        self.listed = roleList

    def getActiveRoles(self):
        titles = self.getRoleTitles()
        return [titles[i] for i in range(len(titles)) if self.listed[i]]

    @staticmethod
    def getRoleTitles():
        return ["Software Engineer", "Systems Engineer", "System Administrator", \
                "Project Maintainer", "Project Manager", "Other", "System Architect", \
                "DevOps"]

    def sharesRoleWith(self, other, includesOthers=False):
      if includesOthers:
        if other.isOtherRole == self.isOtherRole and self.isOtherRole == True:
            return True

      if other.isSoftEng == self.isSoftEng and self.isSoftEng == True:
        return True
      if other.isSysEng == self.isSysEng and self.isSysEng == True:
        return True
      if other.isSysAdmin == self.isSysAdmin and self.isSysAdmin == True:
        return True
      if other.isProjMaint == self.isProjMaint and self.isProjMaint == True:
        return True
      if other.isProjManag == self.isProjManag and self.isProjManag == True:
        return True
      if other.isOtherRole == self.isOtherRole and self.isOtherRole == True:
        return True
      if other.isSysArch == self.isSysArch and self.isSysArch == True:
        return True
      if other.isDevOps == self.isDevOps and self.isDevOps == True:
        return True