from subquestion import Subquestion

class Comparison:

    def __init__(self, role1, role2, questionName, data):
        self.role1 = role1
        self.role2 = role2
        self.question = questionName
        self.data = data

    #list of dictionaries with the differences between each response
    def setData(data):
        self.data = data

    def splitSubquestions(self):
        if self.data is None:
            raise Exception("Data must be set to split into subquestions.")
        
        subquestions = []
        for dictionary in self.data:
            for key in dictionary.keys():
                subquestions.append(Subquestion(self.role1, self.role2, self.question, key, dictionary[key]))

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
