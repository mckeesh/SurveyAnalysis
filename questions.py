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
        self.listed = answers
        self.name = "Q36"
        self.answers = [13, 14, 15, 16, 17]
        self.answersFullNames = ["Not at all", "A little", "A moderate amount", \
                                 "A lot", "A great deal"]

class Q19:
    def __init__(self, answers):
        self.simpleSmall, \
        self.simpleLarge, \
        self.complexSmall, \
        self.complexLarge, \
        self.explorationReqd, \
        self.littleNoExploration = answers

class Q26:
    def __init__(self, answer):
        self.answer = answer

class Q34:
    def __init__(self, answers):
        self.deadlines, \
        self.teamAwareness, \
        self.projectSizeScale, \
        self.projectStructureIssues, \
        self.projectRules = answers
