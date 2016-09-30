from OutputWriter import OutputWriter
from roles import Roles
from comparison import Comparison

class RoleAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def analyzeEachRole(participants, question, ignoreOtherRole=False):

        if ignoreOtherRole:
            for i in range(8):
                roles = [False]*8
                roles[i] = True
                roles1 = Roles(roles)

                if i == 5 or j == 5:
                    pass
                else:
                    percentages = RoleAnalyzer.getResponsePercentages(participants, question, roles1)
                    OutputWriter.outputPercentages(percentages, question, "percentage_results_%s.csv" % Roles.getRoleTitles()[i])

                    means = ExperienceAnalyzer.getResponseMeans(participants, question)
                    OutputWriter.outputMeans(means, question, "mean_results_%s.csv" % experience.readable())

        else:
            for i in range(8):
                roles = [False]*8
                roles[i] = True
                roles1 = Roles(roles)

                percentages = RoleAnalyzer.getResponsePercentages(participants, question, roles1)
                OutputWriter.outputPercentages(percentages, question, "percentage_results_%s.csv" % Roles.getRoleTitles()[i])

                means = RoleAnalyzer.getResponseMeans(participants, question)
                OutputWriter.outputMeans(means, question, "mean_results_%s.csv" % Roles.getRoleTitles()[i])

    @staticmethod
    def analyzeRoleDifferences(participants, question, ignoreOtherRole=True):
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

                        roles2 = Roles(jRoles)

                        comparison = RoleAnalyzer.compareRoles(roles1, roles2, participants, question)
                        # print("##########\n%s,%s\n########\n" % (str(roles1), str(roles2)))
                        comparisons.append(comparison)
        else:
            for i in range(8):
                iRoles = [False]*8
                iRoles[i] = True
                roles1 = Roles(iRoles)

                for j in range(8):
                    jRoles = [False]*8
                    jRoles[j] = True

                    roles2 = Roles(jRoles)

                    comparison = self.compareRoles(roles1, roles2, participants)
                    comparisons.append(comparison)

        return comparisons

    @staticmethod
    def analyzeGeneralResults(participants, question):

        percentages = RoleAnalyzer.getResponsePercentages(participants, question)
        OutputWriter.outputPercentages(percentages, question, "percentage_results.csv")

        means = RoleAnalyzer.getResponseMeans(participants, question)
        OutputWriter.outputMeans(means, question, "mean_results.csv")

    @staticmethod
    def getResponseCounts(participants, question, roles=None):
        # roles = None
        if roles is not None:
            participants = [p for p in participants if p.roles.sharesRoleWith(roles)]

        scoreSums = []
        for x in range(len(getattr(participants[0], question.name).listed)):
            scoreSums.append(RoleAnalyzer._blankAnswerDict(getattr(participants[0], question.name)))
        
        for participant in participants:
            questionList = getattr(participant, question.name).listed

            for i in range(len(questionList)):
                currentValue = questionList[i]
                if currentValue is not None:
                    scoreSums[i][questionList[i]] += 1

        return scoreSums

    @staticmethod
    def getResponseMeans(participants, question, roles=None):
        counts = RoleAnalyzer.getResponseCounts(participants, question, roles)

        totals = [sum(dictionary.values()) for dictionary in counts]
        meanResults = []
        for i in range(len(counts)):
            dictionary = counts[i]
            sum_ = sum([int(key)*dictionary[key] for key in dictionary.keys()])
            meanResults.append(float(sum_)/totals[i])

        return meanResults

    @staticmethod
    def getResponsePercentages(participants, question, roles=None):
        counts = RoleAnalyzer.getResponseCounts(participants, question, roles)

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

    @staticmethod    
    def rankComparisons(comparisonList):
        subquestions = []
        for comparison in comparisonList:
            subquestions += comparison.splitSubquestions()

        subquestions.sort(key=lambda x: x.value, reverse=True)

        return subquestions

    @staticmethod      
    def compareRoles(roles1, roles2, participants, question):
        roles1Result = RoleAnalyzer.getResponsePercentages(participants, question, roles1)
        roles2Result = RoleAnalyzer.getResponsePercentages(participants, question, roles2)

        comparison = RoleAnalyzer.compareResults(roles1Result, roles2Result)

        return Comparison(roles1, roles2, question, comparison)

    @staticmethod
    def compareResults(result1, result2):
        if len(result1) != len(result2):
            raise Exception("Results don't seem to be of the same form.")
        
        comparisons = []
        for i in range(len(result1)):
            dictComparison = RoleAnalyzer._compareDictResult(result1[i], result2[i])
            comparisons.append(dictComparison)

        return comparisons

    @staticmethod    
    def _compareDictResult(dict1, dict2):
        
        dict1Keys = list(dict1.keys())
        dict2Keys = list(dict2.keys())

        dict1Keys.sort()
        dict2Keys.sort()

        if dict1Keys != dict2Keys:
            raise Exception("The two dictionaries you are comparing have different keys.")

        comparison = RoleAnalyzer._calculateDictDiff(dict1, dict2)

        return comparison

    @staticmethod
    def _calculateDictDiff(dict1, dict2):
        diffDict = {}

        dict1Keys = dict1.keys()

        for key in dict1.keys():
            # print("%s,%s" % (dict1[key], dict2[key]))
            difference = abs(dict1[key]-dict2[key])
            diffDict[key] = difference


        return diffDict

    @staticmethod
    def _blankAnswerDict(question):
        answerDict = {}
        for answer in question.answers:
            answerDict[answer] = 0

        return answerDict