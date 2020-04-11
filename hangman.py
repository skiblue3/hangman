import random
import string

print("H A N G M A N")

word_list = ['python', 'java', 'kotlin', 'javascript']
game_word = random.choice(word_list)

def list_to_str(lists):
  str1 = ""
  for a in lists:
    str1+=a
  return str1

list1 = list(game_word)
solve = list('-'*len(game_word))
lives = 0
play = 1

guesstemp =[]

def menu():
  str2 = input('Type "play" to play the game, "exit" to quit:')
  if str2.lower() == 'play':
    return 1
  else:
    return 0

play =  menu()
while play == 1:
  while True:
    print()
    solvetemp = list_to_str(solve)
    print(solvetemp)
    if solve == list1:
      print("You guessed the word!\nYou survived!\n")
      break
    guess = input("Input a letter:")

    if len(guess) != 1:
      print("You should print a single letter")
      continue
    elif guess not in string.ascii_lowercase:
      print("It is not an ASCII lowercase letter ")
      continue

    elif guess in guesstemp:
      print("You already typed this letter")
      continue

    for i in range(len(list1)):
      if (guess == list1[i]):
        solve[i] = list1[i]

    if guess not in game_word:
      print("No such letter in the word")
      lives += 1

    guesstemp.append(guess)
    if lives == 8:
      print("You are hanged!\n")
      break
  play = menu()
