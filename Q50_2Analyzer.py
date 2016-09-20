import os

from roles import Roles
from comparison import Comparison
from questions import Q50_2

class Q50_2Analyzer:
    
    def __init__(self, roles=None):
        self.roles = roles

    #set the roles to be analyzed
    def setRoles(self, roles):
        self.roles = roles

    def analyze(self, participants, ignoreOtherRole=True):
        self.createDirs()

        responseCounts = self.getResponseCounts(participants)
        responsePercentages = self.getResponsePercentages(participants)
        
        #Eew, clean it up
        comparisons = []
        if ignoreOtherRole:
            for i in range(8):
                iRoles = [False]*8
                iRoles[i] = True
                roles1 = Roles(iRoles)

                for j in range(8):
                    jRoles = [False]*8
                    jRoles[j] = True

                    if i == 5 or j == 5:
                        pass
                    else:
                        roleTitles = roles1.getRoleTitles()
                        roles2 = Roles(jRoles)

                        comparison = self.compareRoles(roles1, roles2, participants)
                        comparisons.append(comparison)
        else:
            for i in range(8):
                iRoles = [False]*8
                iRoles[i] = True
                roles1 = Roles(iRoles)

                for j in range(8):
                    jRoles = [False]*8
                    jRoles[j] = True

                    roleTitles = roles1.getRoleTitles()
                    roles2 = Roles(jRoles)

                    comparison = self.compareRoles(roles1, roles2, participants)
                    comparisons.append(comparison)

        subquestions = self.rankComparisons(comparisons)

        rankingsFile = self.createResultsFile("rankings.csv")

        i = 0
        for subquestion in subquestions:
            rankingsFile.write("Role 1, %s\n" % subquestion.role1.getActiveRoles()[0])
            rankingsFile.write("Role 2, %s\n" % subquestion.role2.getActiveRoles()[0])
            rankingsFile.write("Question, %s\n" % subquestion.questionNumber)
            rankingsFile.write("Subquestion, %d\n" % subquestion.subquestionNumber)
            rankingsFile.write("Answer, %s\n" % Q50_2.getAnswerTitle(subquestion.answer))
            rankingsFile.write("Percent Difference, %f\n" % subquestion.value)
            rankingsFile.write("")
            i += 1

        rankingsFile.close()


    def getResponseCounts(self, participants):
        roles = None
        if self.roles is not None:
            participants = [p for p in participants if p.roles.sharesRoleWith(self.roles)]

        scoreSums = [self._blankAnswerDict(participants[0].q50_2) for x in range(len(participants[0].q50_2.listed))]
        for participant in participants:
            q50_2 = participant.q50_2.listed

            for i in range(len(q50_2)):
                currentValue = q50_2[i]
                if currentValue is not None:
                    scoreSums[i][q50_2[i]] += 1

        return scoreSums

    def getResponsePercentages(self, participants):
        counts = self.getResponseCounts(participants)

        totals = [sum(dictionary.values()) for dictionary in counts]
        percentageResult = []
        percentDict = {}
        for i in range(len(counts)):
            percentDict = {}
            dictionary = counts[i]
            for key in dictionary.keys():
                percentDict[key] = (float(dictionary[key])/totals[i])*100
            percentageResult.append(percentDict)

        return percentageResult

    def rankComparisons(self, comparisonList):
        subquestions = []
        for comparison in comparisonList:
            subquestions += comparison.splitSubquestions()

        subquestions.sort(key=lambda x: x.value, reverse=True)

        return subquestions


    def compareRoles(self, roles1, roles2, participants):
        self.setRoles(roles1)
        roles1Result = self.getResponsePercentages(participants)

        self.setRoles(roles2)
        roles2Result = self.getResponsePercentages(participants)

        comparison = self.compareResults(roles1Result, roles2Result)

        return Comparison(roles1, roles2, "Q50_2", comparison)

    def compareResults(self, result1, result2):
        if len(result1) != len(result2):
            raise Exception("Results don't seem to be of the same form.")
        
        comparisons = []
        for i in range(len(result1)):
            dictComparison = self._compareDictResult(result1[i], result2[i])
            comparisons.append(dictComparison)

        return comparisons


    def _compareDictResult(self, dict1, dict2):
        
        dict1Keys = list(dict1.keys())
        dict2Keys = list(dict2.keys())

        dict1Keys.sort()
        dict2Keys.sort()

        if dict1Keys != dict2Keys:
            raise Exception("The two dictionaries you are comparing have different keys.")

        comparison = self._calculateDictDiff(dict1, dict2)

        return comparison

    def _calculateDictDiff(self, dict1, dict2):
        diffDict = {}

        dict1Keys = dict1.keys()

        for key in dict1.keys():
            difference = abs(dict1[key]-dict2[key])
            diffDict[key] = difference


        return diffDict

    def _blankAnswerDict(self, question):
        answerDict = {}
        for answer in question.answers:
            answerDict[answer] = 0

        return answerDict

    def createDirs(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        resultsDirectory = dir_path + "/results/Q50_2/" 
    
        if not os.path.exists(resultsDirectory):
            os.makedirs(resultsDirectory)

    def createResultsFile(self, fileName):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        resultsFile = dir_path + "/results/Q50_2/" + fileName

        f = open(resultsFile, "w")

        return f