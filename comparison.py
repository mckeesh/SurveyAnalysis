from subquestion import SubquestionComparison

class Comparison:

    def __init__(self, trait1, trait2, question, data):
        self.trait1 = trait1
        self.trait2 = trait2
        self.question = question
        self.data = data

    #list of dictionaries with the differences between each response
    def setData(data):
        self.data = data

    def splitSubquestions(self):
        if self.data is None:
            raise Exception("Data must be set to split into subquestions.")
        
        subquestions = []
        i = 0
        for dictionary in self.data:
            for key in dictionary.keys():
                subquestions.append(SubquestionComparison(self.trait1, self.trait2, self.question, i, key, dictionary[key]))
            i += 1
        return subquestions

    def toString(self, comparison, csv=False):
        result = comparison.data
        resultString = ""
        for i in range(len(result)):
            resultString += ("Sub-question %d\n" % i)
            sortedItems = sorted(result[i].items())
            if not csv:
                for key, value in sortedItems:
                    resultString += "%s: %s\n" % (key, value)
                resultString += "\n"
            else:
                for key in result[i].keys():
                    resultString += ("%s,%s\n" % key, value)
                resultString += "\n"

        return resultString
