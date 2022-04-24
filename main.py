#importing modules
import random
import math
import time

#defining reused functions
def print_fancy(decoration, text): #prints lines of decorations around text
  print(decoration*math.ceil(len(text)/len(decoration)))
  print(text)
  print(decoration*math.ceil(len(text)/len(decoration)))

def int_input(prompt, error): #a function so that I can repeat it, prompt for prompt, error for the error message
  while True:
    n = input(prompt)
    try:
      n = int(n)
      return n
    except ValueError:
      print_fancy("*", error)


#defining component functions
      
def ask_name(): #everything is stored in a function for easier assembly of the final program - this asks for name
  print_fancy("-=-","Welcome to my maths quiz!")
  global name
  print("\nWhat is your name?")
  while True:
    name = input(" > ").strip()
    if name.replace(" ","").isalpha():
      break
    else:
      print_fancy ("*","Please only enter letters")
  print("\nHello, " + name + "! \nThis is a basic multiplication and division maths quiz. \nYou can decide the length and starting difficulty. \nIf you allow it to, the quiz will gradually get harder. \nAfter 3 incorrect answers, the quiz will end. \nThe time it takes for you to answer each question will also be timed.")

def customise(): #asks for customisation, stored in function for easier assembly
  global length
  global start_difficulty
  global difficulty_scaling
  #asking for length:
  #length = input('\nHow long would you like the quiz to be? \nEnter a whole number or "endless" if you do not want the quiz to have a length limit.')
  print("-" * 50 + '\nHow many questions would you like the quiz to be? \nEnter a whole number or "endless" if you do not want the quiz to have a length limit.')
  while True: #this loop asks for length until endless or an integer is answered
    length = input(" > ").lower()
    if length == "endless":
      break
    else:
      try: 
        length = int(length)
        if length > 0: #checks if the length is positive
          break
        else:
          print_fancy("*", 'Please enter a positive whole number or "endless"')
      except ValueError:
        print_fancy("*", 'Please enter a positive whole number or "endless"')
  #asking for difficulty:
  print("-" * 50 + "\nWhat would you like the starting difficulty to be? Please enter a whole number between 5 and 20")
  while True: #this loop asks for the difficulty until a number between 5 and 20 is input
    start_difficulty = int_input(" > ", "Please enter a whole number between 5 and 20") #this is a different variable to be able to restart with the same settings.
    if start_difficulty >= 5 and start_difficulty <= 20: #check if difficulty is between 5 and 20
      break
    print_fancy("*", "Please enter a whole number between 5 and 20")
  #asking for difficulty scaling:
  print("-" * 50 + '\nWould you like the quiz to gradually get harder? (answer "yes" or "no") ')
  while True: #This loop keeps asking for difficulty scaling until the end user answers 'yes' or 'no'
    difficulty_scaling = input(" > ").lower()
    if difficulty_scaling == "yes" or difficulty_scaling == "no":
      break
    print_fancy("*", 'Please answer "yes" or "no"')

def question(): #asks a question
  global score
  global difficulty
  operators = ("x", "÷") #stores operators
  operator = operators[random.randint(0,1)]
  if operator == "x":
    a = random.randint(1, math.floor(difficulty))
    b = random.randint(1, math.floor(difficulty))
  else:
    b = random.randint(1, math.floor(difficulty))
    a = b * random.randint(1, math.floor(difficulty))
  question = str(a) + " " + operator + " " + str(b)
  answer = int_input("What is {}?".format(question) + "\n > ", "Please answer with a whole number")
  if answer == round(eval(question.replace('x', '*').replace('÷', '/'))): #checks if the answer is correct, changes 'x' to '*' and '÷' to '/' so that eval() works
    print_fancy("=", "Correct!")
    score += 1
    if difficulty_scaling == "yes": #increases difficulty if difficulty scaling is on
      difficulty += 1/4
    print("Your score is currently {}".format(score))
    return "correct"
  else: #if the answer is incorrect
    print_fancy("/", "Incorrect")
    print("The correct answer was {}".format(round(eval(question.replace('x', '*').replace('÷', '/')))))
    return "incorrect"

def start_quiz(): #The actual quiz
  global score
  global difficulty
  global total_time
  global questions_asked
  #sets/resets questions asked, score, difficulty, total time, and lives
  total_time = 0
  questions_asked = 0
  score = 0
  lives = 3
  difficulty = start_difficulty
  #print statements to debug, they should be 0, starting_difficulty, 0, 3, 0 respectively:
  """
  print("Score: {}".format(score))
  print("Difficulty: {}".format(difficulty))
  print("total_time: {}".format(total_time))
  print("lives: {}".format(lives))
  print("questions_asked: {}".format(questions_asked))
  """
  print("-"*50)
  print_fancy("-=-", "Press enter to start the quiz")
  input()
  while True: #continuously asks questions
    start_time = time.time()
    print("-"*50)
    questions_asked += 1
    if length == "endless": #tells user how many questions have been asked, and if it isn't endless, shows how many are left
      print("Question {}:".format(questions_asked))
    else:
      print("Question {}/{}:".format(questions_asked, length))
    if question() == "incorrect":
      lives -=1
      if lives > 1: #if statement to fix plural/singular grammar mistake
        print("You have {} incorrect answers left".format(lives))
      elif lives == 1:
        print("You have 1 incorrect answer left")
    time_taken = round(time.time() - start_time, 2)
    total_time += time_taken
    print("Time: {} seconds".format(time_taken))
    if lives < 1 or questions_asked == length: #ends the loop after all lives are gone or enough questions has been asked
      break
  #the following code takes place after the quiz has ended
  print("-"*50)
  print_fancy("♦", "Congratulations!")
  print("You scored {} points! \nYou spent an average of {} seconds per question." .format(score, round(total_time/questions_asked, 2)))
  print('\nWould you like to replay the quiz with the same settings? (please answer "yes" or "no")')
  while True: #continuously asks question until a valid answer is entered
    replay = input(" > ").lower()
    if replay == "no": #thanks user, breaks loop so the quiz ends
      print_fancy("-=-", "Thank you for playing my quiz!")
      break
    elif replay == "yes": #recalls itself (start_quiz()) to repeat quiz, then breaks so that if the user decides to stop later on, the program ends
      start_quiz()
      break
    else:
      print_fancy("*", 'Please enter "yes" or "no"')
     
  
ask_name()
customise()
start_quiz()