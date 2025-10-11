class QuizBrain:

    def __init__(self, bank):
        self.question = 0
        self.bank = bank

    # def next_question(self):
    #     self.question +=1
    #     print(f"Q{self.question}: {self.bank[self.question -1].txt}")

    def next_question(self):
        self.question +=1
        pass


    def still_has_questions(self):
        return self.question < len(self.bank)