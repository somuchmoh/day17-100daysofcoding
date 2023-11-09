from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question()
    new_question.__int__(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain()
quiz.__int__(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz. Your final score is {quiz.score}/12")