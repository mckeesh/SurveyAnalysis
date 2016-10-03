class GeneralAnalyzer:
    
    @staticmethod
    def compareListResults(result1, result2):
        if len(result1) != len(result2):
            raise Exception("Results don't seem to be of the same form.")
        
        listComparison = GeneralAnalyzer._compareListResult(result1, result2)

        return listComparison

    @staticmethod    
    def _compareListResult(list1, list2):
        resultList = []

        for i in range(len(list1)):
            resultList.append(abs(list1[i]-list2[i]))

        return resultList

    @staticmethod
    def compareDictResults(result1, result2):
        if len(result1) != len(result2):
            raise Exception("Results don't seem to be of the same form.")
        
        comparisons = []
        for i in range(len(result1)):
            dictComparison = GeneralAnalyzer._compareDictResult(result1[i], result2[i])
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

        comparison = GeneralAnalyzer._calculateDictDiff(dict1, dict2)

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