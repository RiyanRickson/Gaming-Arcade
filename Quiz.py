def quiz_game()
{
    quiz = {
        "Which data type is used to store whole numbers?  :": "int",
        "Which data type stores decimal values?  :": "float",
        "Which data type stores text?  :": "str",
        "Which data type stores True or False?  :": "bool",
        "Which data type uses key-value pairs?  :": "dictionary",
        "Which collection does not allow duplicate values?  :": "set",
        "Which brackets are used for lists?  :": "[]",
        "Which brackets are used for tuples?  :": "()",
        "Which function converts text to uppercase?  :": "upper()",
        "Which function converts text to lowercase?  :": "lower()",
        "Which operator is used to join strings?  :": "+",
        "Which keyword is used to import a module?  :": "import",
        "Which function returns the number of elements in a list?  :": "len()",
        "Which loop is used when the number of iterations is known?  :": "for",
        "Which loop is used when the number of iterations is unknown?  :": "while",
        "Which keyword is used to define a function?  :": "def",
        "Which function gives the maximum value?  :": "max()",
        "Which function gives the minimum value?  :": "min()",
        "Which function converts data to string?  :": "str()",
        "Which function converts data to integer?  :": "int()",
        "Which function gives absolute value?  :": "abs()",
        "Which operator is used for addition?  :": "+",
        "Which operator is used for subtraction?  :": "-",
        "Which operator is used for multiplication?  :": "*",
        "Which operator is used for division  :": "/",
        "Which operator is used for floor division?  :": "//",
        "Which operator is used for modulus?  :": "%",
    
    }
    
    score = 0
    print("Welcome to the Quiz Game Related to basic PYTHON\n")
    
    for question, answer in quiz.items():
        user_answer = input(question).strip().lower()
        if user_answer == answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong Answer! The Correct Answer is {answer}\n")
    
    print(f"Quiz Finished Related to basic PYTHON !! Your total score: {score}/{len(quiz)}")
}
