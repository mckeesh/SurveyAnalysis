class Q50_1:
    name = "Q50_1"
    answers = [36, 37, 38, 39, 40]
    answersFullNames = ["Not at all", "A little", "A moderate amount", \
                                 "A lot", "A great deal"]
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
        self.listed = answers

    @staticmethod
    def getAnswerTitle(answerNumber):
        return Q50_1.answersFullNames[answerNumber-36]

class Q50_2:
    name = "Q50_2"
    answers = [1, 2, 3, 4, 5]
    answersFullNames = ["Not useful", "Slightly useful", "Moderately useful", \
                                 "Very useful", "Essential"]
    def __init__(self, answers):
        self.betterToolTransparency, \
        self.betterUsability, \
        self.betterFiltering, \
        self.betterGraphicalInfo, \
        self.betterExploration, \
        self.betterTerminology = answers
        self.listed = answers

    @staticmethod
    def getAnswerTitle(answerNumber):
        return Q50_2.answersFullNames[answerNumber-1]

class Q36:
    name = "Q36"
    answers = [13, 14, 15, 16, 17]
    answersFullNames = ["Not at all", "A little", "A moderate amount", \
                                 "A lot", "A great deal"]
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
        self.listed = answers

    @staticmethod
    def getAnswerTitle(answerNumber):
        return Q36.answersFullNames[answerNumber-13]

class Q19:
    name = "Q19"
    answers = [22, 23, 24, 25, 26]
    answersFullNames = ["Not effective at all", "Slightly effective", "Moderately effective", \
                                 "Very effective", "Extremely effective"]
    def __init__(self, answers):
        self.simpleSmall, \
        self.simpleLarge, \
        self.complexSmall, \
        self.complexLarge, \
        self.explorationReqd, \
        self.littleNoExploration = answers
        self.listed = answers

    @staticmethod
    def getAnswerTitle(answerNumber):
        return Q19.answersFullNames[answerNumber-22]

class Q26:
    def __init__(self, answer):
        self.answer = answer

class Q34:
    name = "Q34"
    answers = [1]
    answersFullNames = ["Checked"]
    def __init__(self, answers):
        self.deadlines, \
        self.teamAwareness, \
        self.projectSizeScale, \
        self.projectStructureIssues, \
        self.projectRules = answers
        self.listed = answers

    @staticmethod
    def getAnswerTitle(answerNumber):
        if answerNumber == 1:
            return "Checked"
        else:
            return "Not Checked"