from comparison import Comparison
import questions
from OutputWriter import OutputWriter
from RoleAnalyzer import RoleAnalyzer
from ExperienceAnalyzer import ExperienceAnalyzer
from ProjectSourceAnalyzer import ProjectSourceAnalyzer

class QuestionAnalyzer:
    
    def __init__(self):
        pass


    def analyze(self, participants):
        active_questions = [   questions.Q19, \
                        questions.Q36, \
                        questions.Q50_1, \
                        questions.Q50_2 ]

        for question in active_questions:
            OutputWriter.createDir("/results/%s/" % question.name)

            #By Role
            RoleAnalyzer.analyzeGeneralResults(participants, question)
            RoleAnalyzer.analyzeEachRole(participants, question)
            comparisons = RoleAnalyzer.analyzeRoleDifferencesPercentage(participants, question)
            rankedSubquestionComparisons = RoleAnalyzer.rankComparisons(comparisons)
            OutputWriter.outputRankings(rankedSubquestionComparisons, "/results/%s/by_role/percent/" % question.name)
            comparisonsMean = RoleAnalyzer.analyzeRoleDifferencesMeans(participants, question)
            rankedSubquestionComparisonsMean = RoleAnalyzer.rankComparisons(comparisonsMean)
            OutputWriter.outputRankings(rankedSubquestionComparisonsMean, "/results/%s/by_role/mean/" % question.name)

            # By Experience
            ExperienceAnalyzer.analyzeGeneralResults(participants, question)
            ExperienceAnalyzer.analyzeEachExpLevel(participants, question)
            comparisons = ExperienceAnalyzer.analyzeExpDifferencesPercentages(participants, question)
            rankedSubquestionComparisons = ExperienceAnalyzer.rankComparisons(comparisons)
            OutputWriter.outputRankings(rankedSubquestionComparisons, "/results/%s/by_exp/percent/" % question.name)
            comparisonsMean = ExperienceAnalyzer.analyzeExpDifferencesMeans(participants, question)
            rankedSubquestionComparisonsMean = ExperienceAnalyzer.rankComparisons(comparisonsMean)
            OutputWriter.outputRankings(rankedSubquestionComparisonsMean, "/results/%s/by_exp/mean/" % question.name)

            ProjectSourceAnalyzer.analyzeGeneralResults(participants, question)
            ProjectSourceAnalyzer.analyzeEachSourceType(participants, question)
            comparisons = ProjectSourceAnalyzer.analyzeSourceTypeDifferencesPercentage(participants, question)
            rankedSubquestionComparisons = ProjectSourceAnalyzer.rankComparisons(comparisons)
            OutputWriter.outputRankings(rankedSubquestionComparisons, "/results/%s/by_source/percent/" % question.name)
            comparisonsMean = ProjectSourceAnalyzer.analyzeSourceTypeDifferencesMeans(participants, question)
            rankedSubquestionComparisonsMean = ProjectSourceAnalyzer.rankComparisons(comparisonsMean)
            OutputWriter.outputRankings(rankedSubquestionComparisonsMean, "/results/%s/by_source/mean/" % question.name)