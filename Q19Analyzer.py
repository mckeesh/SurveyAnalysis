from comparison import Comparison
import questions
from OutputWriter import OutputWriter
from RoleAnalyzer import RoleAnalyzer
from ExperienceAnalyzer import ExperienceAnalyzer

class Q19Analyzer:
    
    def __init__(self):
        pass


    def analyze(self, participants):
        question = questions.Q19
        OutputWriter.createDir("/results/%s/" % question.name)

        #By Role
        RoleAnalyzer.analyzeGeneralResults(participants, question)
        RoleAnalyzer.analyzeEachRole(participants, question)
        
        comparisons = RoleAnalyzer.analyzeRoleDifferences(participants, question)
        rankedSubquestionComparisons = RoleAnalyzer.rankComparisons(comparisons)
        top = rankedSubquestionComparisons[0]
        OutputWriter.outputRankings(rankedSubquestionComparisons, "/results/%s/by_role/" % question.name)

        # By Experience
        ExperienceAnalyzer.analyzeGeneralResults(participants, question)
        ExperienceAnalyzer.analyzeEachExpLevel(participants, question)
        comparisons = ExperienceAnalyzer.analyzeExpDifferences(participants, question)

        rankedSubquestionComparisons = ExperienceAnalyzer.rankComparisons(comparisons)
        top = rankedSubquestionComparisons[0]
        OutputWriter.outputRankings(rankedSubquestionComparisons, "/results/%s/by_exp/" % question.name)