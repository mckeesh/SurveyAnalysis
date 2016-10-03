from OutputWriter import OutputWriter
from experience import Experience
from comparison import Comparison
from GeneralAnalyzer import GeneralAnalyzer

class ExperienceAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def analyzeEachExpLevel(participants, question):

        for i in range(6):
            experience = Experience(i+1)

            percentages = ExperienceAnalyzer.getResponsePercentages(participants, question, experience)
            OutputWriter.outputPercentages(percentages, question, "percentage_results_%s.csv" % experience.readable())

            means = ExperienceAnalyzer.getResponseMeans(participants, question, experience)
            OutputWriter.outputMeans(means, question, "mean_results_%s.csv" % experience.readable())


    @staticmethod
    def analyzeExpDifferencesPercentages(participants, question):
        #Eew, clean it up
        comparisons = []
        
        for i in range(6):
            exp1 = Experience(i+1)

            for j in range(6):
                exp2 = Experience(j+1)

                comparison = ExperienceAnalyzer.compareExperiencePercentages(exp1, exp2, participants, question)
                comparisons.append(comparison)

        return comparisons

    @staticmethod
    def analyzeExpDifferencesMeans(participants, question):
        #Eew, clean it up
        comparisons = []
        
        for i in range(6):
            exp1 = Experience(i+1)

            for j in range(6):
                exp2 = Experience(j+1)

                comparison = ExperienceAnalyzer.compareExperienceMeans(exp1, exp2, participants, question)
                comparisons.append(comparison)

        return comparisons

    @staticmethod
    def analyzeGeneralResults(participants, question):
        percentages = ExperienceAnalyzer.getResponsePercentages(participants, question)
        OutputWriter.outputPercentages(percentages, question, "percentage_results.csv")

        means = ExperienceAnalyzer.getResponseMeans(participants, question)
        OutputWriter.outputMeans(means, question, "mean_results.csv")

    @staticmethod
    def getResponsePercentages(participants, question, experience=None):
        counts = ExperienceAnalyzer.getResponseCounts(participants, question, experience)

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
    def getResponseMeans(participants, question, experience=None):
        counts = ExperienceAnalyzer.getResponseCounts(participants, question, experience)

        totals = [sum(dictionary.values()) for dictionary in counts]
        meanResults = []
        for i in range(len(counts)):
            dictionary = counts[i]
            sum_ = sum([int(key)*dictionary[key] for key in dictionary.keys()])
            meanResults.append(float(sum_)/totals[i])

        return meanResults

    @staticmethod
    def getResponseCounts(participants, question, experience=None):
        # print(experience)

        if experience is not None:
            participants = [p for p in participants if p.experience == experience]

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
    def compareExperiencePercentages(exp1, exp2, participants, question):
        exp1Result = ExperienceAnalyzer.getResponsePercentages(participants, question, exp1)
        exp2Result = ExperienceAnalyzer.getResponsePercentages(participants, question, exp2)

        comparison = GeneralAnalyzer.compareDictResults(exp1Result, exp2Result)

        return Comparison(exp1, exp2, question, comparison)

    @staticmethod      
    def compareExperienceMeans(exp1, exp2, participants, question):
        exp1Result = ExperienceAnalyzer.getResponseMeans(participants, question, exp1)
        exp2Result = ExperienceAnalyzer.getResponseMeans(participants, question, exp2)

        comparison = GeneralAnalyzer.compareListResults(exp1Result, exp2Result)

        return Comparison(exp1, exp2, question, comparison)