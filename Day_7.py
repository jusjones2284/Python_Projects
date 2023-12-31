import random
word_list = ["ardvark", "baboon", "camel"]

num = random.randint(0, 2)
randomWord = random.choice(word_list)

chosen_word = word_list[num]
word_length = len(chosen_word)
print(word_length)
print(randomWord)
letterGuess = input("Please guess a letter: \n").lower() 
# def letterGuessFun():
#   letterGuess = input("Please guess a letter: \n").lower()
#   return letterGuess 

display = []

for letter in chosen_word:
  display += "-"

# for _ in range(len(chosen_word)):
#   display += "-"


# print(display)

# numberOf = list("-") * len(chosen_word)
# letterGuessFun()
  
  end_of_game = False

while not end_of_game:
  for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position}\n \
    Current letter: {letter}\n Guessed letter: {letterGuess}")
    if letter == letterGuess:
      display[position] = letter

  print(display)
  if "_" not in display:
    end_of_game = True
    print("you win.")












# for word in word_list:
#   guessedWord = input("please guess word in word list \n")

# blanks = 0

# j = "-"

# while blanks < len(list(chosen_word)):
#   k = []
#   k.append(j) 
#   blanks +=1
#   print(len(k))

# guessedWord = input(f"Please guess the word {k}\n")


# if guessedWord == chosen_word:
#   print("you got it")

# else:
#   print("try again")


# print(chosen_word)

# print("justin".split('u'))