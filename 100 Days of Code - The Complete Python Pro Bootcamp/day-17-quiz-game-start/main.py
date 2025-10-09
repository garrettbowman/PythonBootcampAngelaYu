from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for entry in question_data:
    question_bank.append(Question(entry["text"], entry["answer"]))


# print(question_bank[0].txt)
# print(question_bank[0].answer)

continue_playing = True
brain = QuizBrain(question_bank)
score = 0
for question in question_bank:
    print(f"Q{brain.question +1}: {brain.bank[brain.question].txt}")

    userinput = str(input(f"True or False:")).lower()
    print(f"The correct answer is {brain.bank[brain.question].answer}")
    if userinput == brain.bank[brain.question].answer.lower():
        score +=1
        print(f"Your score is currently: {score}.")
    else:
        pass

    brain.next_question()

print("That is all folks! Thanks for playing.")