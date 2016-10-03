from OutputWriter import OutputWriter
from project_source import ProjectSource
from comparison import Comparison
from GeneralAnalyzer import GeneralAnalyzer

class ProjectSourceAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def analyzeEachSourceType(participants, question):

        for i in range(3):
            projectSource = ProjectSource(i+1)

            percentages = ProjectSourceAnalyzer.getResponsePercentages(participants, question, projectSource)
            OutputWriter.outputPercentages(percentages, question, "percentage_results_%s.csv" % str(projectSource))

            means = ProjectSourceAnalyzer.getResponseMeans(participants, question, projectSource)
            OutputWriter.outputMeans(means, question, "mean_results_%s.csv" % str(projectSource))


    @staticmethod
    def analyzeSourceTypeDifferencesPercentage(participants, question):
        #Eew, clean it up
        comparisons = []
        
        for i in range(3):
            projectSource1 = ProjectSource(i+1)

            for j in range(3):
                projectSource2 = ProjectSource(j+1)

                comparison = ProjectSourceAnalyzer.compareProjectSourcePercentages(projectSource1, projectSource2, participants, question)
                comparisons.append(comparison)

        return comparisons

    @staticmethod
    def analyzeSourceTypeDifferencesMeans(participants, question):
        #Eew, clean it up
        comparisons = []
        
        for i in range(3):
            projectSource1 = ProjectSource(i+1)

            for j in range(3):
                projectSource2 = ProjectSource(j+1)

                comparison = ProjectSourceAnalyzer.compareProjectSourceMeans(projectSource1, projectSource2, participants, question)
                comparisons.append(comparison)

        return comparisons

    @staticmethod
    def analyzeGeneralResults(participants, question):
        percentages = ProjectSourceAnalyzer.getResponsePercentages(participants, question)
        OutputWriter.outputPercentages(percentages, question, "percentage_results.csv")

        means = ProjectSourceAnalyzer.getResponseMeans(participants, question)
        OutputWriter.outputMeans(means, question, "mean_results.csv")

    @staticmethod
    def getResponsePercentages(participants, question, projectSource=None):
        counts = ProjectSourceAnalyzer.getResponseCounts(participants, question, projectSource)

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
    def getResponseMeans(participants, question, projectSource=None):
        counts = ProjectSourceAnalyzer.getResponseCounts(participants, question, projectSource)

        totals = [sum(dictionary.values()) for dictionary in counts]
        meanResults = []
        for i in range(len(counts)):
            dictionary = counts[i]
            sum_ = sum([int(key)*dictionary[key] for key in dictionary.keys()])
            meanResults.append(float(sum_)/totals[i])

        return meanResults

    @staticmethod
    def getResponseCounts(participants, question, projectSource=None):
        # print(experience)

        if projectSource is not None:
            participants = [p for p in participants if p.projectSource == projectSource]

        scoreSums = []
        for x in range(len(question.subquestions)):
            scoreSums.append(GeneralAnalyzer._blankAnswerDict(question))
        
        for participant in participants:
            questionList = getattr(participant, question.name).listed

            # print(questionList)

            for i in range(len(questionList)):
                currentValue = questionList[i]
                if currentValue is not None:
                    scoreSums[i][questionList[i]] += 1


        return scoreSums

    @staticmethod    
    def rankComparisons(comparisonList):
        subquestions = []
        for comparison in comparisonList:
            subquestions += comparison.splitSubquestions()

        subquestions.sort(key=lambda x: x.value, reverse=True)

        return subquestions

    @staticmethod      
    def compareProjectSourcePercentages(projectSource1, projectSource2, participants, question):
        ps1Result = ProjectSourceAnalyzer.getResponsePercentages(participants, question, projectSource1)
        ps2Result = ProjectSourceAnalyzer.getResponsePercentages(participants, question, projectSource2)

        comparison = GeneralAnalyzer.compareDictResults(ps1Result, ps2Result)

        return Comparison(projectSource1, projectSource2, question, comparison)

    @staticmethod      
    def compareProjectSourceMeans(projectSource1, projectSource2, participants, question):
        ps1Result = ProjectSourceAnalyzer.getResponseMeans(participants, question, projectSource1)
        ps2Result = ProjectSourceAnalyzer.getResponseMeans(participants, question, projectSource2)

        comparison = GeneralAnalyzer.compareListResults(ps1Result, ps2Result)

        return Comparison(projectSource1, projectSource2, question, comparison)