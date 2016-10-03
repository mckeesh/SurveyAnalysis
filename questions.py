class Q50_1:
    name = "Q50_1"
    answers = [36, 37, 38, 39, 40]
    answersFullNames = ["Not at all", "A little", "A moderate amount", \
                                 "A lot", "A great deal"]

    subquestions = ["Time to resolve a conflict",
                    "Number of conflicting lines of code",
                    "Complexity of conflicting lines of code",
                    "Number of files in the conflict",
                    "Complexity of the files with conflicts",
                    '"Non-functional changes (whitespace, renaming, etc)"',
                    "Dependencies of conflicting code on other components",
                    "Atomicity of changesets in the conflict",
                    "Your knowledge/expertise in area of conflicting code"]

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
        if type(answerNumber) == int:
            return Q50_1.answersFullNames[answerNumber-36]
        else:
            return "No Answer Title"

class Q50_2:
    name = "Q50_2"
    answers = [1, 2, 3, 4, 5]
    answersFullNames = ["Not useful", "Slightly useful", "Moderately useful", \
                                 "Very useful", "Essential"]

    subquestions = ["Better transparency in tool functionality/operations",
                    "Better usability",
                    "Better ways of filtering out less relevant information",
                    "Better graphical presentation of information",
                    "Better ways of exploring project history",
                    "Better terminology that is more consistent with my other tools"]

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
        if type(answerNumber) == int:
            return Q50_2.answersFullNames[answerNumber-1]
        else:
            return "No Answer Title"

class Q36:
    name = "Q36"
    answers = [13, 14, 15, 16, 17]
    answersFullNames = ["Not at all", "A little", "A moderate amount", \
                                 "A lot", "A great deal"]
    subquestions = ["The amount of information you have about the conflicting code", \
                    "How easy it is to understand the code involved in the merge conflict", \
                    "Tool support for examining development history", \
                    "Complexity of the project structure", \
                    "How well tools present information in an understandable way", \
                    "Trustworthiness of tools", \
                    "Informativiness of commit messages", \
                    "Changing assumptions within the code", \
                    "Project culture", \
                    "Your expertise in the area of code with the merge conflict"]
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
        if type(answerNumber) == int:
            return Q36.answersFullNames[answerNumber-13]
        else:
            return "No Answer Title"

class Q19:
    name = "Q19"
    answers = [22, 23, 24, 25, 26]
    answersFullNames = ["Not effective at all", "Slightly effective", "Moderately effective", \
                                 "Very effective", "Extremely effective"]
    subquestions = ['"Simple, small merge conflict resolutions"',
                    '"Simple, large merge conflict resolutions"',
                    '"Complex, small merge conflict resolutions"',
                    '"Complex, large merge conflict resolutions"',
                    "Merge conflict resolutions that require exploring code history",
                    "Merge conflict resolutions that require little or no code history exploration"]

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
        if type(answerNumber) == int:
            return Q19.answersFullNames[answerNumber-22]
        else:
            return "No Answer Title"

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