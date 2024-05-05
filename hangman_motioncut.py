import random
import string

def get_valid_word_and_hint(category):
    words_and_hints = {
        'animals': [('elephant', 'Large mammal with a trunk'), ('lion', 'King of the jungle'), ('zebra', 'Black and white striped animal'), ('dolphin', 'Intelligent marine mammal'), ('penguin', 'Flightless bird from Antarctica'), ('giraffe', 'Tallest living land animal'), ('kangaroo', 'Marsupial from Australia'), ('crocodile', 'Reptile with a powerful jaw'), ('butterfly', 'Colorful winged insect'), ('monkey', 'Primate with a long tail')],
        'countries': [('india', 'Home of the Taj Mahal'), ('canada', 'North American country with maple leaf flag'), ('france', 'Home of the Eiffel Tower'), ('australia', 'Country with the Great Barrier Reef'), ('brazil', 'Known for the Amazon rainforest'), ('egypt', 'Home of the ancient pyramids'), ('china', 'Most populous country in the world'), ('japan', 'Land of the rising sun'), ('italy', 'Home of the Roman Empire'), ('germany', 'Known for its beer and cars')],
        'movies': [('starwars', 'Epic space opera film series'), ('matrix', 'Sci-fi movie about a simulated reality'), ('lordoftherings', 'Fantasy film trilogy based on J.R.R. Tolkien\'s novels'), ('inception', 'Sci-fi movie about dream sharing'), ('titanic', 'Tragic love story set on the ill-fated ship'), ('jurassicpark', 'Dinosaurs come to life in this thriller'), ('avengers', 'Marvel superhero movie'), ('harrypotter', 'Fantasy film series based on J.K. Rowling\'s books'), ('gladiator', 'Historical drama set in ancient Rome'), ('casablanca', 'Classic romantic drama set in World War II')],
        'food': [('pizza', 'Italian dish with tomato sauce and cheese'), ('burger', 'Popular sandwich with a patty'), ('pasta', 'Italian dish made from dough'), ('sushi', 'Japanese dish with vinegared rice and raw fish'), ('tacos', 'Mexican dish with a folded tortilla'), ('icecream', 'Frozen dessert made from dairy products'), ('chocolate', 'Sweet treat made from cacao beans'), ('sandwich', 'Food item consisting of two slices of bread with fillings'), ('hotdog', 'Grilled sausage in a bun'), ('popcorn', 'Popular snack made from corn kernels')]
    }
    word_and_hint = random.choice(words_and_hints[category])
    word = word_and_hint[0].upper()
    hint = word_and_hint[1]
    return word, hint

def display_hangman(incorrect_guesses):
    hangman_pics = ['''
       +---+
           |
           |
           |
           |
           |
     =========''', '''
       +---+
       O   |
           |
           |
           |
           |
     =========''', '''
       +---+
       O   |
       |   |
           |
           |
           |
     =========''', '''
       +---+
       O   |
      /|   |
           |
           |
           |
     =========''', '''
       +---+
       O   |
      /|\  |
           |
           |
           |
     =========''', '''
       +---+
       O   |
      /|\  |
      /    |
           |
           |
     =========''', '''
       +---+
       O   |
      /|\  |
      / \  |
           |
     =========''']
    print(hangman_pics[incorrect_guesses])

def hangman():
    print("Choose a category: ")
    print("1. Animals")
    print("2. Countries")
    print("3. Movies")
    print("4. Food")
    category = input("Enter the category number: ")

    if category == '1':
        word, hint = get_valid_word_and_hint('animals')
    elif category == '2':
        word, hint = get_valid_word_and_hint('countries')
    elif category == '3':
        word, hint = get_valid_word_and_hint('movies')
    elif category == '4':
        word, hint = get_valid_word_and_hint('food')
    else:
        print("Invalid category. Exiting the game.")
        return

    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    incorrect_guesses = 0

    lives = 6
    difficulty_level = input("Choose difficulty level (1: Easy, 2: Medium, 3: Hard): ")
    if difficulty_level == '2':
        lives = 4
    elif difficulty_level == '3':
        lives = 2

    while len(word_letters) > 0 and incorrect_guesses < lives:
        display_hangman(incorrect_guesses)
        print(f'You have {lives - incorrect_guesses} lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                incorrect_guesses += 1
                print('Letter is not in the word.')
                if len(word_letters) > 0:
                    hint_prompt = input("Would you like a hint? (y/n) ")
                    if hint_prompt.lower() == 'y':
                        print(f"Hint: {hint}")

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    if incorrect_guesses == lives:
        display_hangman(incorrect_guesses)
        print(f'You died, sorry. The word was {word}')
    else:
        print(f'Congratulations! You guessed the word {word}!')

if __name__ == '__main__':
    hangman()