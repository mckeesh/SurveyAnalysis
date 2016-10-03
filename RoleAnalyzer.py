from OutputWriter import OutputWriter
from roles import Roles
from comparison import Comparison
from GeneralAnalyzer import GeneralAnalyzer

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

                    means = ExperienceAnalyzer.getResponseMeans(participants, question, roles1)
                    OutputWriter.outputMeans(means, question, "mean_results_%s.csv" % experience.readable())

        else:
            for i in range(8):
                roles = [False]*8
                roles[i] = True
                roles1 = Roles(roles)

                percentages = RoleAnalyzer.getResponsePercentages(participants, question, roles1)
                OutputWriter.outputPercentages(percentages, question, "percentage_results_%s.csv" % Roles.getRoleTitles()[i])

                means = RoleAnalyzer.getResponseMeans(participants, question, roles1)
                OutputWriter.outputMeans(means, question, "mean_results_%s.csv" % Roles.getRoleTitles()[i])

    @staticmethod
    def analyzeRoleDifferencesPercentage(participants, question, ignoreOtherRole=True):
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

                        comparison = RoleAnalyzer.compareRolesPercentages(roles1, roles2, participants, question)
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

                    comparison = self.compareRolesPercentages(roles1, roles2, participants)
                    comparisons.append(comparison)

        return comparisons

    @staticmethod
    def analyzeRoleDifferencesMeans(participants, question, ignoreOtherRole=True):
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

                        comparison = RoleAnalyzer.compareRolesMeans(roles1, roles2, participants, question)
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

                    comparison = self.compareRolesMeans(roles1, roles2, participants)
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
            scoreSums.append(GeneralAnalyzer._blankAnswerDict(getattr(participants[0], question.name)))
        
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
    def compareRolesPercentages(roles1, roles2, participants, question):
        r1Result = RoleAnalyzer.getResponsePercentages(participants, question, roles1)
        r2Result = RoleAnalyzer.getResponsePercentages(participants, question, roles2)

        comparison = GeneralAnalyzer.compareDictResults(r1Result, r2Result)

        return Comparison(roles1, roles2, question, comparison)

    @staticmethod      
    def compareRolesMeans(roles1, roles2, participants, question):
        r1Result = RoleAnalyzer.getResponseMeans(participants, question, roles1)
        r2Result = RoleAnalyzer.getResponseMeans(participants, question, roles2)

        comparison = GeneralAnalyzer.compareListResults(r1Result, r2Result)

        return Comparison(roles1, roles2, question, comparison)