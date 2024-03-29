import csv
import os 

from roles import Roles
from experience import Experience
from participant import Participant
from questions import *
from project_source import ProjectSource
# from Q34Analyzer import Q34Analyzer
from QuestionAnalyzer import QuestionAnalyzer

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    resultsDirectory = dir_path + "/results/"

    if not os.path.exists(resultsDirectory):
        os.makedirs(resultsDirectory)

    participantList = []

    with open('survey.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        index = 0
        for row in reader:

            if index < 2:
                pass
            else:
                
                participant = createParticipant(row)
                if participant != None:
                    participantList.append(participant)

            index += 1

        analyzer = QuestionAnalyzer()
        analyzer.analyze(participantList)

def createParticipant(row):
    participant = Participant()

    roles = getRoles(row)
    exp = getExperience(row)
    projectSource = getProjectSource(row)

    if isValidParticipant(row):
        participant.setRoles(roles)
        participant.setExperience(exp)
        participant.setProjectSource(projectSource)

        q50_1 = getQ50_1(row)
        participant.setQ50_1(q50_1)

        q50_2 = getQ50_2(row)
        participant.setQ50_2(q50_2)

        q36 = getQ36(row)
        participant.setQ36(q36)

        q19 = getQ19(row)
        participant.setQ19(q19)

        q34 = getQ34(row)
        participant.setQ34(q34)

        return participant

    else:
        return None

def isValidParticipant(row):
    for i in range(13,24):
        if row[i] != '':
            return True

def getRoles(row):
    isSoftEng = convertStrToBoolean(row[16])
    isSysEng = convertStrToBoolean(row[17])
    isSysAdmin = convertStrToBoolean(row[18])
    isProjMaint = convertStrToBoolean(row[19])
    isProjManag = convertStrToBoolean(row[20])
    isOtherRole = convertStrToBoolean(row[21])
    isSysArch = convertStrToBoolean(row[23])
    isDevOps = convertStrToBoolean(row[24])

    return Roles([isSoftEng, isSysEng, isSysAdmin, isProjMaint, isProjManag, isOtherRole, isSysArch, isDevOps])

def getExperience(row):
    return Experience(row[13])

def getProjectSource(row):
    if row[14] == '':
        return ProjectSource(4)
    return ProjectSource(row[14])

def getQ50_1(row):
    answerList = []

    for each in range(27,36):
        answerList.append(castToInt(row[each]))

    return Q50_1(answerList)

def getQ50_2(row):
    answerList = []

    for each in range(81,87):
        answerList.append(castToInt(row[each]))

    return Q50_2(answerList)

def getQ36(row):
    answerList = []

    for each in range(57,67):
        answerList.append(castToInt(row[each]))

    return Q36(answerList)

def getQ19(row):
    answerList = []

    for each in range(72,78):
        answerList.append(castToInt(row[each]))

    return Q19(answerList)

def getQ26(row):
    return Q26(row[48])

def getQ34(row):
    answerList = []

    for each in range(49,54):
        answerList.append(castToInt(row[each]))

    return Q34(answerList)

def castToInt(string):
    if string == '':
        return None
    else:
        return int(string)

def convertStrToBoolean(string):

    if string == '':
        return False

    try:
        convertedValue = int(string)
        return bool(convertedValue)
    except ValueError as e:
        pass

    try:
        return bool(string)
    except Exception as e:
        raise e


main()