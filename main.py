import math

def print_fancy(decoration, text): #prints lines with decorations
  print(decoration*math.ceil(len(text)/len(decoration)))
  print(text)
  print(decoration*math.ceil(len(text)/len(decoration)))
  
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
  print("\nHello, " + name + "! \nThis is a multiplication and division maths quiz. \nYou can decide the length and starting difficulty. \nIf you allow it to, the quiz will gradually get harder. \nAfter 3 incorrect answers, the quiz will end. \nThe time it takes for you to answer each question will also be timed.")

def customise(): #asks for customisation, stored in function for easier assembly
  global length
  global start_difficulty
  global difficulty_scaling
  #asking for length:
  #length = input('\nHow long would you like the quiz to be? \nEnter a whole number or "endless" if you do not want the quiz to have a length limit.')
  print('\nHow long would you like the quiz to be? \nEnter a whole number or "endless" if you do not want the quiz to have a length limit.')
  length = input(" > ")
  if length.lower() != "endless":
    length = int(length)
  #asking for difficulty:
  print("\nWhat would you like the starting difficulty to be? Please enter a whole number between 2 and 20")
  while True:
    start_difficulty = int(input(" > ")) #this is a different variable to be able to restart with the same settings.
    if start_difficulty >= 2 and start_difficulty <= 20: #check if difficulty is between 2 and 20
      break
    print_fancy("*", "Please enter a whole number between 2 and 20")
  #asking for difficulty scaling
  print('\nWould you like the quiz to gradually get harder? (answer "yes" or "no") ')
  while True:
    difficulty_scaling = input(" > ")
    if difficulty_scaling.lower() == "yes" or difficulty_scaling.lower() == "no":
      break
    print_fancy("*", 'Please answer "yes" or "no"')

    
    
  

ask_name()
customise()





