def play_again_options():
    while True:
        print("Do you want to play again?")
        playAgainOptions = input("Y or N: ").strip().upper()
        if playAgainOptions == "Y":
            return True   # CHANGED: return to caller instead of calling welcomescreen()
        elif playAgainOptions == "N":
            print("Thanks for playing!")
            return False  # CHANGED: signal caller to stop
        else:
            print("Invalid input. Please enter Y or N.")


def easy_questions_answers():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) Rome", "C) Berlin", "D) Madrid"],
            "answer": "A"
        },
        {
            "question": "Which planet has the largest number of moons?",
            "options": ["A) Jupiter", "B) Saturn", "C) Neptune", "D) Uranus"],
            "answer": "B"
        },
        {
            "question": "Who wrote the play Hamlet?",
            "options": ["A) William Shakespeare", "B) Charles Dickens", "C) Leo Tolstoy", "D) Mark Twain"],
            "answer": "A"
        },
        {
            "question": "In computing, what does “HTTP” stand for?",
            "options": ["A) HyperText Transfer Protocol", "B) High Transmission Text Protocol", "C) Hyperlink Transfer Process", "D) Host Transfer Protocol"],
            "answer": "A"
        },
        {
            "question": "The painter Vincent van Gogh was born in which country?",
            "options": ["A) Netherlands", "B) France", "C) Belgium", "D) Germany"],
            "answer": "A"
        }
    ]
    currentScore = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_choice = input("Your Answer: ")
        if user_choice.upper() == q["answer"]:
            print("Correct!")
            currentScore += 1
            print(f"{currentScore} / 5")
        else:
            print("Incorrect..")
            print(f"{currentScore} / 5")
    print(
        f"Your final score:{currentScore}/5 | Final score percentage {(currentScore/5)*100}% \n")

    return play_again_options()  # CHANGED: return the user's choice to the caller


def medium_questions_answers():
    questions = [
        {
            "question": "Which gas do plants absorb from the atmosphere for photosynthesis?",
            "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Helium"],
            "answer": "B"
        },
        {
            "question": "In Greek mythology, who is the god of the sea?",
            "options": ["A) Zeus", "B) Hades", "C) Poseidon", "D) Apollo"],
            "answer": "C"
        },
        {
            "question": "Which country hosted the 2016 Summer Olympics?",
            "options": ["A) China", "B) Brazil", "C) UK", "D) Russia"],
            "answer": "B"
        },
        {
            "question": "In computer science, what does 'CSS' stand for?",
            "options": ["A) Cascading Style Sheets", "B) Computer Style Syntax", "C) Central System Script", "D) Code Style System"],
            "answer": "A"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A) Diamond", "B) Quartz", "C) Gold", "D) Obsidian"],
            "answer": "A"
        }
    ]

    currentScore = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_choice = input("Your Answer: ")
        if user_choice.upper() == q["answer"]:
            print("Correct!")
            currentScore += 1
            print(f"{currentScore} / 5")
        else:
            print("Incorrect..")
            print(f"{currentScore} / 5")
    print(
        f"Your final score:{currentScore}/5 | Final score percentage {(currentScore/5)*100}% \n")

    return play_again_options()  # CHANGED


def hard_questions_answers():
    questions = [
        {
            "question": "Which mathematician is known for formulating the laws of motion and universal gravitation?",
            "options": ["A) Isaac Newton", "B) Carl Gauss", "C) Leonhard Euler", "D) Archimedes"],
            "answer": "A"
        },
        {
            "question": "What is the chemical formula of table salt?",
            "options": ["A) NaCl", "B) KCl", "C) H2SO4", "D) CaCO3"],
            "answer": "A"
        },
        {
            "question": "In literature, who wrote 'One Hundred Years of Solitude'?",
            "options": ["A) Gabriel García Márquez", "B) Jorge Luis Borges", "C) Mario Vargas Llosa", "D) Pablo Neruda"],
            "answer": "A"
        },
        {
            "question": "Which organelle is known as the 'powerhouse of the cell'?",
            "options": ["A) Mitochondria", "B) Nucleus", "C) Ribosome", "D) Golgi apparatus"],
            "answer": "A"
        },
        {
            "question": "Which European city is famous for the architectural works of Antoni Gaudí?",
            "options": ["A) Barcelona", "B) Madrid", "C) Lisbon", "D) Paris"],
            "answer": "A"
        }
    ]

    currentScore = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_choice = input("Your Answer: ")
        if user_choice.upper() == q["answer"]:
            print("Correct!")
            currentScore += 1
            print(f"{currentScore} / 5")
        else:
            print("Incorrect..")
            print(f"{currentScore} / 5")
    print(
        f"Your final score:{currentScore}/5 | Final score percentage {(currentScore/5)*100}% \n")

    return play_again_options()  # CHANGED


def welcomescreen():
    print("Welcome to the Text-Based Quiz Game!")
    print("You will be asked a series of questions.")
    print("Select from the options and answer them correctly to score points.")
    print("There will be a total of 5 questions.")
    print("Let's get started!")
    print("Please select the difficulty level:")

    while True:  # CHANGED: single loop controls replay
        # CHANGED: ask each round
        difficultOptions = int(input("1. Easy 2. Medium 3. Hard \n"))

        if difficultOptions == 1:
            keep_playing = easy_questions_answers()
        elif difficultOptions == 2:
            keep_playing = medium_questions_answers()
        elif difficultOptions == 3:
            keep_playing = hard_questions_answers()
        else:
            print("Invalid Option")
            continue  # CHANGED: re-prompt difficulty

        if not keep_playing:  # CHANGED: stop if user chose N
            break


welcomescreen()
