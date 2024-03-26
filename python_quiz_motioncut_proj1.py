questions_list = []
correct_answers_list=[]
score = 0
options_list = []

print("What is your name?\n")
name = input("Enter your name: ")

print("\nRules: \n 1. For every correct answer, you score 1 point. \n 2. For every incorrect answer, you get a hint and another chance but \n your score is deducted by 0.5. \n 3. If you are unable to answer correctly 2 times, you get the correct answer \n but no points are added. \n 4. You get your final scores at the end. \n 5. If you ever wish to quit the quiz, type 'quit' (without the quotations).\n")

questions_list = [
    "Which animal is known as the \"ship of the desert\"?",
    "How many days are there in a week?",
    "Which animal has a long trunk?",
    "Which mammal is the largest mammal in the world?",
    "What is the capital of India?",
    "What is the national flower of India?",
    "What is the planet that we live on?",
    "What is the hardest natural substance on Earth?",
    "How many bones are in the human body?",
    "Balloons are filled with which gas?",
    "What is the doctor who treats heart-related diseases?",
    "What galaxy do we live in?",
    "Who is the Founder of Tesla and SpaceX?",
    "Which company made ChatGPT?",
    "What is India's national bird?",
]

options_list = [
    {"choices": ["Lion", "Elephant", "Camel", "Snake"]},
    {"choices": [5, 6, 7, 8]},
    {"choices": ["Elephant", "Giraffe", "Rhino", "Hippopotamus"]},
    {"choices": ["Blue Whale", "Elephant", "Giraffe", "Lion"]},
    {"choices": ["Mumbai", "Kolkata", "New Delhi", "Chennai"]},
    {"choices": ["Rose", "Lotus", "Jasmine", "Tulip"]},
    {"choices": ["Earth", "Mars", "Venus", "Jupiter"]},
    {"choices": ["Diamond", "Sapphire", "Emerald", "Quartz"]},
    {"choices": [100, 200, 206, 300]},
    {"choices": ["Helium", "Oxygen", "Nitrogen", "Hydrogen"]},
    {"choices": ["Cardiologist", "Surgeon", "Pediatrician", "Dermatologist"]},
    {"choices": ["Milky Way", "Andromeda", "Triangulum", "Large Magellanic Cloud"]},
    {"choices": ["Jeff Bezos", "Elon Musk", "Bill Gates", "Mark Zuckerberg"]},
    {"choices": ["Google", "OpenAI", "Microsoft", "Meta"]},
    {"choices": ["Peacock", "Kingfisher", "Parrot", "Owl"]},
]

correct_answers_list = ["Camel",
                        7,
                        "Elephant",
                        "Blue Whale",
                        "New Delhi",
                        "Lotus",
                        "Earth",
                        "Diamond",
                        206,
                        "Helium", 
                        "Cardiologist",
                        "Milky Way",
                        "Elon Musk",
                        "OpenAI", 
                        "Peacock",
                        ]

def display_question(question, options):
    print(question)
    for choice in options["choices"]:
        print(choice)

def get_valid_answer(question, options, hint=None):
    attempts = 2
    while attempts > 0:
        answer = input(f"Enter your answer for '{question}' (or 'quit' to exit):\n")
        if answer == "quit":
            return answer
        elif all(type(choice) == int for choice in options["choices"]) and answer.isdigit():
            return int(answer)
        elif all(type(choice) == str for choice in options["choices"]) and answer in [str(choice) for choice in options["choices"]]:
            return answer
        else:
            attempts -= 1
            if attempts == 0:
                print("Incorrect answer. You have exhausted your attempts.")
            else:
                print("Invalid answer. Please choose from the following options:")
                display_question(question, options)
    return None  

hint_mapping ={
                "Which animal is known as the \"ship of the desert\"?" : "It lives in deserts and stores water in its humps.",
                "How many days are there in a week?": "Think about the days between weekend days.",
                "Which animal has a long trunk?": "It has a long neck and eats leaves.",
                "Which mammal is the largest mammal in the world?": "It lives in oceans and can grow very big.",
                "What is the capital of India?": "It's a major city in northern India.",
                "What is the national flower of India?": "It grows in water and is considered sacred in India.",
                "What is the planet that we live on?": "Think about the name of our solar system and its planets.",
                "What is the hardest natural substance on Earth?": "It's found in pencils and can scratch most other minerals.",
                "How many bones are in the human body?": "An adult human has more bones than a baby.",
                "Balloons are filled with which gas?": "It's lighter than air and makes balloons float.",
                "What doctor treats heart-related diseases?": "They specialize in the heart and circulatory system.",
                "What galaxy do we live in?": "It's a spiral galaxy with billions of stars.",
                "Who is the Founder of Tesla and SpaceX?": "He's a famous entrepreneur known for electric cars and space exploration.",
                "Which company made ChatGPT?": "It's an AI research company focused on developing large language models.",
                "What is India's national bird?": "It's a colorful bird known for its vibrant plumage.",
                }

for question, option in zip(questions_list, options_list):
    display_question(question, option)
    answer = get_valid_answer(question, option, hint_mapping.get(question))  

    if answer is None:  
        print(f"Incorrect answer. The correct answer is: {correct_answers_list[questions_list.index(question)]}")
    elif answer == "quit":
        break
    elif answer == correct_answers_list[questions_list.index(question)]:
        score += 1
        print("Correct answer! Well Done!")
    else:
        hint = hint_mapping.get(question)
        if hint:
            print(f"Incorrect answer. Hint: {hint}")
            answer = get_valid_answer(question, option, hint)  
            if answer == correct_answers_list[questions_list.index(question)]:
                score += 0.5
                print("Correct answer! You got it with a hint.")
            else:
                print(f"Incorrect answer. The correct answer is: {correct_answers_list[questions_list.index(question)]}")
        else:
            print(f"Incorrect answer. The correct answer is: {correct_answers_list[questions_list.index(question)]}")

print("\n")
print(f"{name}'s final score is: {score} points!")
                           