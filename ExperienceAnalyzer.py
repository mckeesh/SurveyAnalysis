from OutputWriter import OutputWriter
from experience import Experience
from comparison import Comparison

class ExperienceAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def analyzeEachExpLevel(participants, question):

        for i in range(6):
            experience = Experience(i+1)

            percentages = ExperienceAnalyzer.getResponsePercentages(participants, question, experience)
            OutputWriter.outputPercentages(percentages, question, "percentage_results_%s.csv" % experience.readable())

            means = ExperienceAnalyzer.getResponseMeans(participants, question)
            OutputWriter.outputMeans(means, question, "mean_results_%s.csv" % experience.readable())


    @staticmethod
    def analyzeExpDifferences(participants, question):
        #Eew, clean it up
        comparisons = []
        
        for i in range(6):
            exp1 = Experience(i+1)

            for j in range(6):
                exp2 = Experience(j+1)

                comparison = ExperienceAnalyzer.compareExperience(exp1, exp2, participants, question)
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
            scoreSums.append(ExperienceAnalyzer._blankAnswerDict(question))
        
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
    def compareExperience(exp1, exp2, participants, question):
        exp1Result = ExperienceAnalyzer.getResponsePercentages(participants, question, exp1)
        exp2Result = ExperienceAnalyzer.getResponsePercentages(participants, question, exp2)

        comparison = ExperienceAnalyzer.compareResults(exp1Result, exp2Result)

        return Comparison(exp1, exp2, question, comparison)

    @staticmethod
    def compareResults(result1, result2):
        if len(result1) != len(result2):
            raise Exception("Results don't seem to be of the same form.")
        
        comparisons = []
        for i in range(len(result1)):
            dictComparison = ExperienceAnalyzer._compareDictResult(result1[i], result2[i])
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

        comparison = ExperienceAnalyzer._calculateDictDiff(dict1, dict2)

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