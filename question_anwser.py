fObj = open('pluto.txt')

def questions_and_answers():
    #questions = []
    #answers = []
    correctAnswerCount = 0
    result = 0

    with open("pluto.txt", 'r'):
        fLines = fObj.readlines()

    IsQuestion = True

    for line in fLines:
        if IsQuestion:
            print(line.strip())
        else:
            answer= input("Please provide your answer:")
            if answer.strip() == line.strip():
                correctAnswerCount = correctAnswerCount + 1
                print("You got it Correct!!")
            else:
                print("That is incorrect")

        IsQuestion = not IsQuestion

        # if line.startswith('Q'):
        #     questions.append(line[3:])
        # elif line.startswith('A'):
        #     answers.append(line[3:])
        if correctAnswerCount == 3:
            result = "100%"
        elif correctAnswerCount == 2:
            result = "66%"
        else:
            result = "33%"

    return result

print("Your result is", questions_and_answers())
