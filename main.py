

import math

def print_fancy(decoration, text): #prints lines with decorations
  print(decoration*math.ceil(len(text)/len(decoration)))
  print(text)
  print(decoration*math.ceil(len(text)/len(decoration)))
  
def ask_name(): #everything is stored in a function for easier assembly of the final program
  print_fancy("-=-","Welcome to my maths quiz!")
  global name
  while True:
    name = input("\nWhat is your name? \n > ").strip()
    if name.replace(" ","").isalpha():
      break
    else:
      print("Invalid name, please only enter letters")
  print("\nHello, " + name + "! \nThis is a multiplication and division maths quiz. \nYou can decide the length and starting difficulty. \nIf you allow it to, the quiz will gradually get harder. \nThe time it takes for you to answer each question will also be timed.")
  

ask_name()





