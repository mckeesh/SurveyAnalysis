import os

class OutputWriter:
    
    @staticmethod
    def createDir(pathFromRoot):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        resultsDirectory = dir_path + pathFromRoot
    
        if not os.path.exists(resultsDirectory):
            os.makedirs(resultsDirectory)

    @staticmethod
    def outputPercentages(percentageResults, question, fileName):
        OutputWriter.createDir("/results/%s/general/percentages" % question.name)
        resultsFile = OutputWriter.createResultsFile("/results/%s/general/percentages/" % question.name, fileName)
        resultsFile.write(",%s\n" % ",".join(reversed(question.answersFullNames)))

        for i in range(len(percentageResults)):
            subquestionResultDict = percentageResults[i]
            sortedKeys = sorted(subquestionResultDict.keys(), reverse=True)

            rowToWriteList = [str(subquestionResultDict[key]) for key in sortedKeys]

            keyText = question.subquestions[i]
            resultsFile.write("%s,%s\n" % (keyText, ",".join(rowToWriteList)))

        resultsFile.close()

    @staticmethod
    def outputMeans(meanResults, question, fileName):
        dir_name = ("/results/%s/general/means/" % question.name)
        OutputWriter.createDir(dir_name)
        resultsFile = OutputWriter.createResultsFile(dir_name, fileName)

        for i in range(len(meanResults)):
            mean = meanResults[i]
            subquestion = question.subquestions[i]

            rowToWrite = "%s,%s\n" % (subquestion, mean)

            resultsFile.write(rowToWrite)

        resultsFile.close()

    @staticmethod
    def outputRankings(subquestionComparisons, directory):
        OutputWriter.createDir(directory)
        rankingsFile = OutputWriter.createResultsFile(directory, "rankings.csv")

        for subquestionComparison in subquestionComparisons:
            rankingsFile.write(str(subquestionComparison))
            rankingsFile.write("\n")

        rankingsFile.close()

    @staticmethod
    def createResultsFile(directory, fileName):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        full_directory_path = dir_path + directory
        OutputWriter.createDir(full_directory_path)
        resultsFile = full_directory_path + fileName

        f = open(resultsFile, "w")

        return f