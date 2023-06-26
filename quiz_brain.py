class QuizBrain:

    def __init__(self, question_bank, question_number):
        self.question_number = question_number
        self.question_list = question_bank

    def current_question(self, display_question, answer_key):
        ask_question_answer = input(f"Q{self.question_number + 1}: {display_question} "
                                 f"True or false?\n").capitalize()
        if ask_question_answer == answer_key:
            print("Correct!")
            return 1
        else:
            print("Incorrect")
            return 0