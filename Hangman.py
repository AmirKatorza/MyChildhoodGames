import random 

HANGMAN_ASCII_ART = """
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __ 
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
					 """

HANGMAN_PHOTOS = {
	0: """
	x-------x
	""",
	
	1: """
	x-------x
	|
	|
	|
	|
	|
	""",
	
	2: """
	 x-------x
	 |       |
	 |       0
	 |
	 |
	 |
	 """,  
	
	3: """
	x-------x
	|       |
	|       0
	|       |
	|
	|
	""",
	
	4: """
	x-------x
	|       |
	|       0
	|      /|\\
	|
	|
	""",

	5: """
	x-------x
	|       |
	|       0
	|      /|\\
	|      /
	|
	""",

	6: """
	x-------x
	|       |
	|       0
	|      /|\\
	|      / \\
	|
	"""
	}

def check_win(secret_word, old_letters_guessed):
  
	"""Checks whether list of letters contains all characters of chosen word.
  :param secret_word: word value
  :param old_letters_guessed: list of letters
  :type secret_word: str
  :type old_letters_guessed: list
  :return: 'True' if all characters of a word included in list, 'False' otherwise.
  :rtype: bool
  """
	flag = True
	for char in secret_word:
		if char in old_letters_guessed:
			continue
		else:
			flag = False
			break
	return flag

def show_hidden_word(secret_word, old_letters_guessed):
	"""Shows the corrects letters guessed by user in the hidden word.
  :param secret_word: word value
  :param old_letters_guessed: list of letters
  :type secret_word: str
  :type old_letters_guessed: list
  :return: A string with letters and blanks according to user guesses.
  :rtype: str
  """
	new_str = []
	for char in secret_word:
		if char in old_letters_guessed:
			new_str.append(char)
		else: 
			new_str.append('_')
	return ' '.join(new_str)

def check_valid_input(letter_guessed, old_letters_guessed):
	"""Checks whether input is valid.
  :param letter_guessed: input value by user
  :param old_letters_guessed: list of letters
  :type secret_word: str
  :type old_letters_guessed: list
  :return: 'True' if input is only one char, not been guessed before and valid alphabet letter, 'False' otherwise.
  :rtype: bool
  """
	if (len(letter_guessed) > 1) or (not letter_guessed.isalpha()) or (letter_guessed.lower() in old_letters_guessed):
		return False
	else:
		return True
		
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	"""Updates the list of guessed letters if input is valid, prints old letters guessed by user if input is not valid.
  :param letter_guessed: input value by user
  :param old_letters_guessed: list of letters
  :type secret_word: str
  :type old_letters_guessed: list
  :return: True if input is valid and list was updated, False otherwise.
  :rtype: bool
  """
	if check_valid_input(letter_guessed, old_letters_guessed):
		old_letters_guessed.append(letter_guessed.lower())
		return True
	else:
		print("X\n")
		separator = '-> '
		print(separator.join(sorted(old_letters_guessed, key=str.lower)) + "\n")
		return False

def check_letter_in_word(letter_guessed, secret_word):
	"""Checks whether user input letter includes in the secret word.
  :param letter_guessed: letter value
  :param secret_word: word value
  :type letter_guessed: str
  :type secret_word: str
  :return: 'True' if letter is included, 'False' otherwise.
  :rtype: bool
  """
	return letter_guessed.lower() in secret_word
	
def choose_word(file_path, index):
  """Checks whether user input letter includes in the secret word.
  :param file_path: file path value
  :param index: index value
  :type file_path: str
  :type index: int
  :return: Word selected out of file to be guessed by user.
  :rtype: str
  """
  try:
      words_input_file = open(r'%s' % file_path, "r")
      words_data = words_input_file.read()
      words_item_list = words_data.split(' ')
      chosen_word = words_item_list[index % len(words_item_list) - 1]
      # words_input_file.close()
      return chosen_word
  except:
      print(f"IO Error with file path {file_path}")
      new_file_path = input("Please enter correct file path: ")
      choose_word(new_file_path, index) #recursion

def print_hangman(num_of_tries):
	"""Prints the hangman photo according to number of tries.
  :param num_of_tries: number of tries value
  :type num_of_tries: int
  :return: None
  """
	print(HANGMAN_PHOTOS[num_of_tries])
	
def print_welcome_screen():
	"""Prints welcome screen.
  :return: None
  """
	print(HANGMAN_ASCII_ART)

def inputNumber(message):
	"""Checks whether input number is valid, stops once a valid whole number was typed.
  :param message: message for user
  :type message: str
  :return: a valid whole number
  :rtype: int
  """
	while True:
		try:
			userInput = int(input(message))       
		except ValueError:
			print("Not an integer! Try again.")
			continue
		if userInput < 0:
			print("Not a possitive number! Try again.")
			continue
		else:	
			return userInput 
			break 

MAX_TRIES = 6 # Max number of errors

def play_hangman():
    
	print_welcome_screen() # Print the welcome screen
	game_file_path = input("Enter file path: ") # Ask user to type file path
	index_num =  inputNumber("Enter index: ") # Ask User to enter a valid whole number
  # index_num = random.randint(0, 1000)
	secret_word = choose_word(game_file_path, index_num) # Choose a secret word from file
	
	old_letters_guessed = [] # Init list of letters
	num_of_tries = 0 # Init num of tries
	
	print("Let's start!") # Notify start of game
	print_hangman(num_of_tries) # Init hangman status	
	print(show_hidden_word(secret_word, old_letters_guessed) + "\n") # Print secret word blanks
		
	while (not check_win(secret_word, old_letters_guessed)) and (num_of_tries < 6): # Run while no win was achieved and number of errors is less then 6
		letter_guessed = input("Guess a letter: ") # Ask user to gues a letter
		if not try_update_letter_guessed(letter_guessed, old_letters_guessed): # Validate input
			continue # If input is not valid run again
		elif check_letter_in_word(letter_guessed, secret_word): # If input is valid check if letter in secret word 
			print(show_hidden_word(secret_word, old_letters_guessed) + "\n") # If letter is correct show guessed letters in secret word
			continue # Run again
		else: # Letter guessed is not correct
			print(":(\n")
			num_of_tries += 1 # Update number of tries
			print_hangman(num_of_tries) # Print hangman status
			print(show_hidden_word(secret_word, old_letters_guessed) + "\n")
	
	if num_of_tries == 6: # Exit from while loop after 6 trial errors
		print("LOSE") # Lose
	else: # Exit from while loop because of correct guesses
		print("WIN") # Win