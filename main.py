import random
import re
import characters
import hp_books
import rules

def main():
    print("==============================================")
    print("======= Harry Potter Character Guesser =======")
    print("==============================================")
    print("")
    print("What would you like to do?")
    print("[Rules] [Search] [Quiz]")
    menu_input = input(">> ")
    menu_options(menu_input.lower())

def menu_options(val):
    if val == "rules":
        rules.print_rules()
        print("What would you like to do?")
        print("[Search] [Quiz]")
        menu_input = input(">> ")
        menu_options(menu_input.lower())
    elif val == "search":
        print("")
        print("==============================================")
        print("======== Harry Potter Character Search =======")
        print("==============================================")
        print("Which book would you like to search within?")
        character_search()
    elif val == "quiz":
        print("")
        print("==============================================")
        print("======== Harry Potter Character Quiz =========")
        print("==============================================")
        character_quiz()
    else:
        print("I didn't understand. Please only type Rules, Search, or Quiz")
        menu_input = input(">> ")
        menu_options(menu_input.lower())

def book_selection():
    print("Please type the letter corresponding to the options below:")
    print("[A] Book 1: Harry Potter and the Sorcerer's Stone")
    print("[B] Book 2: Harry Potter and the Chamber of Secrets")
    print("[C] Book 3: Harry Potter and the Prisoner of Azkaban")
    print("[D] Book 4: Harry Potter and the Goblet of Fire")
    print("[Z] Whole Series (not supported)")
    search_input = input(">> ")

    if search_input.lower() == ("a" or "b" or "c" or "d"):
        book = hp_books.harry_potter_books_alpha[search_input.lower()]
    else:
        print("I didn't understand. Please only type the letter that corresponds to.")
        book_selection()
    
    return get_book_text(book)

def character_search():
    book_text = book_selection()
    book_words = re.findall(r'\w+', book_text)
    print("==============================================")
    char_search = input("Enter the First and Last name of the character you want to search: ")

    count = get_number_of_words(book_words, char_search)

    print("")
    if char_search.lower() == "voldemort":
        print(f"He who shall not be named appears {count} times.")
    elif count == 0:
        print(f"No results for {char_search}.")
    else:
        print(f"{char_search} appears {count} times.")
    
    search_again = input("Would you like to search again? [Yes] [No]: ")
    if search_again.lower() == "yes":
        character_search()
    else:
        pass

def character_quiz():
    book_text = get_random_book()
    book_updated_text = get_book_text(book_text)
    book_words = re.findall(r'\w+', book_updated_text)

    character_one = get_random_character(book_words)
    character_two = get_random_character(book_words)

    if character_one == character_two:
        character_two = get_random_character()
    
    winner = decide_winner(book_words, character_one, character_two)

    print(f"Who appears more within {hp_books.harry_potter_books_dict[book_text]}?")
    print(f"[A] {character_one} or [B] {character_two}")
    answer = input("Please type A or B: ")

    if answer.lower() == "a":
        if winner == "Character One":
            print("Correct!")
            print(f"{character_one} appears in {hp_books.harry_potter_books_dict[book_text]} {get_number_of_words(book_words, character_one)} times.")
            print(f"{character_two} appears in {hp_books.harry_potter_books_dict[book_text]} {get_number_of_words(book_words, character_two)} times.")
        else:
            print("Incorrect...")
            print(f"{character_one} appears in {hp_books.harry_potter_books_dict[book_text]} {get_number_of_words(book_words, character_one)} times.")
            print(f"{character_two} appears in {hp_books.harry_potter_books_dict[book_text]} {get_number_of_words(book_words, character_two)} times.")
    elif answer.lower() == "b":
        if winner == "Character Two":
            print("Correct!")
            print(f"{character_one} appears in {hp_books.harry_potter_books_dict[book_text]} {get_number_of_words(book_words, character_one)} times.")
            print(f"{character_two} appears in {hp_books.harry_potter_books_dict[book_text]} {get_number_of_words(book_words, character_two)} times.")
        else:
            print("Incorrect...")
            print(f"{character_one} appears in {hp_books.harry_potter_books_dict[book_text]} {get_number_of_words(book_words, character_one)} times.")
            print(f"{character_two} appears in {hp_books.harry_potter_books_dict[book_text]} {get_number_of_words(book_words, character_two)} times.")

    play_again = input("Would you like to receive a new question? [Yes] [No]: ")
    if play_again.lower() == "yes":
        print("==============================================")
        print("")
        character_quiz()
    else:
        pass

def decide_winner(book, character1, character2):
    char_one_words = get_number_of_words(book, character1)
    
    char_two_words = get_number_of_words(book, character2)
    
    if char_one_words > char_two_words:
        return "Character One"
    else:
        return "Character Two"

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_number_of_words(words, character):
    count = 0

    # First and Last Name
    # if " " in character:
    first_name = character.split()[0]
    last_name = character.split()[1]
    for i in range(len(words)-2):
            # First Last
            if ((first_name.lower() == words[i].lower()) and (last_name.lower() == words[i+1].lower())):
                count += 1
            # ____ Last
            elif ((first_name.lower() != words[i].lower()) and (last_name.lower() == words[i+1].lower())):
                count += 1
            # First _____
            elif ((first_name == words[i].lower()) and (last_name != words[i+1].lower())):
                count += 1
            
    # Only one name given
    # else:
    #    for i in range(len(words)):
    #        if words[i].lower() == character.lower():
    #            count += 1
    
    return count

def get_random_character(words):
    random_num = random.randrange(0, len(characters.list_of_characters)-1)
    random_char = characters.list_of_characters[random_num]

    random_char_words = get_number_of_words(words, random_char)

    if random_char_words == 0:
        get_random_character(words)
    else:
        return random_char

def get_random_book():
    random_num = random.randrange(0, len(hp_books.harry_potter_books_num))
    return hp_books.harry_potter_books_num[random_num]

main()