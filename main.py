from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in question_data: # Add to question bank
    question_text = x["text"]
    question_answer = x["answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

question_number = 0
score_change = 0
while question_number < len(question_bank):
    question = question_bank[question_number]
    quiz_brain = QuizBrain(question_bank, question_number)
    score_change += quiz_brain.current_question(question.text, question.answer)
    print(f"Score: {score_change}/{question_number + 1}\n")
    question_number += 1
print(f"You completed the trivia challenge! Your final score is {score_change}/{question_number}.")