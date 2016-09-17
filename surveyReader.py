import csv

def main():
    participantList = []

    with open('survey.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        index = 0
        for row in reader:

            if index < 2:
                pass
            else:
                participant = Participant()

                roles = getRoles(row)
                participant.setRoles(roles)

                q50_1 = getQ50_1(row)
                participant.setQ50_1(q50_1)

                q50_2 = getQ50_2(row)
                participant.setQ50_2(q50_2)

                q36 = getQ36(row)
                participant.setQ36(q36)

                q19 = getQ19(row)
                participant.setQ19(q19)

                q34 = getQ34(row)
                participant.setQ34(q34)

                participantList.append(participant)

            index += 1

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

    def __init__(self, roleList):
        self.isSoftEng, \
        self.isSysEng, \
        self.isSysAdmin, \
        self.isProjMaint, \
        self.isProjManag, \
        self.isOtherRole, \
        self.isSysArch, \
        self.isDevOps = roleList

def getRoles(row):
    isSoftEng = convertStrToBoolean(row[16])
    isSysEng = convertStrToBoolean(row[17])
    isSysAdmin = convertStrToBoolean(row[18])
    isProjMaint = convertStrToBoolean(row[19])
    isProjManag = convertStrToBoolean(row[20])
    isOtherRole = convertStrToBoolean(row[21])
    isSysArch = convertStrToBoolean(row[23])
    isDevOps = convertStrToBoolean(row[24])

    return Roles([isSoftEng, isSysEng, isSysAdmin, isProjMaint, isProjManag, isOtherRole, isSysArch, isDevOps])

class Q50_1:
    def __init__(self, answers):
        self.timeToResolve, \
        self.conflictingLOC, \
        self.complexityOfLOC, \
        self.numberOfFiles, \
        self.complexityOfFile, \
        self.nonFunctionalChanges, \
        self.dependencies, \
        self.atomicity, \
        self.knowledgeExpertise = answers

class Q50_2:
    def __init__(self, answers):
        self.betterToolTransparency, \
        self.betterUsability, \
        self.betterFiltering, \
        self.betterGraphicalInfo, \
        self.betterExploration, \
        self.betterTerminology = answers

class Q36:
    def __init__(self, answers):
        self.amountOfInfo, \
        self.understandability, \
        self.toolSupport, \
        self.projectStructComplexity, \
        self.toolInfoPresentation, \
        self.toolTrustworthiness, \
        self.commitMessage, \
        self.outdatedAssumptions, \
        self.projectCulture, \
        self.expertiseInArea = answers

class Q19:
    def __init__(self, answers):
        self.simpleSmall, \
        self.simpleLarge, \
        self.complexSmall, \
        self.complexLarge, \
        self.explorationReqd, \
        self.littleNoExploration = answers

class Q34:
    def __init__(self, answers):
        self.deadlines, \
        self.teamAwareness, \
        self.projectSizeScale, \
        self.projectStructureIssues, \
        self.projectRules = answers

def getQ50_1(row):
    answerList = []

    for each in range(27,36):
        answerList.append(castToInt(row[each]))

    return Q50_1(answerList)

def getQ50_2(row):
    answerList = []

    for each in range(81,87):
        answerList.append(castToInt(row[each]))

    return Q50_2(answerList)

def getQ36(row):
    answerList = []

    for each in range(57,67):
        answerList.append(castToInt(row[each]))

    return Q36(answerList)

def getQ19(row):
    print(row)
    answerList = []

    for each in range(72,78):
        answerList.append(castToInt(row[each]))

    return Q19(answerList)

def getQ34(row):
    print(row)
    answerList = []

    for each in range(49,54):
        answerList.append(castToInt(row[each]))

    return Q34(answerList)


def castToInt(string):
    if string == '':
        return None
    else:
        return int(string)

def convertStrToBoolean(string):

    if string == '':
        return False

    try:
        convertedValue = int(string)
        return bool(convertedValue)
    except ValueError as e:
        pass

    try:
        return bool(string)
    except Exception as e:
        raise e





main()