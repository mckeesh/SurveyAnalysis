class SubquestionComparison:
    def __init__(self, trait1, trait2, question, subquestionNumber, answer, value):
        self.trait1 = trait1
        self.trait2 = trait2
        self.question = question
        self.subquestionNumber = subquestionNumber
        self.answer = answer
        self.value = value

    def __str__(self):
        # print(self.trait1)
        outString = ""
        outString += ("%s 1,%s\n" % (self.trait1.type_, self.trait1.getActive()[0]))
        outString += ("%s 2,%s\n" % (self.trait2.type_, self.trait2.getActive()[0]))
        outString += ("Question,%s\n" % self.question.name)
        outString += ("Subquestion,%s\n" % self.question.subquestions[self.subquestionNumber])
        outString += ("Answer,%s\n" % self.question.getAnswerTitle(self.answer))
        outString += ("Difference,%f\n" % self.value)

        return outString