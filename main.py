import time
""" 
********************************************************
Filename:       main.py
Name:           Computer Parts Giveaway
Description:    Quiz people on basic course material with prizes for the top performers

Author:         Pei.L
Created On:     26/03/2021
********************************************************
"""

print("*****Lucas's Tech Store Giveaway Quiz*****")

#ask user if they would like you participate in the game/quiz
answer = input("Do you want to take this quiz to enter yourself into the computer parts giveaway? Yes/No: ")

#while loop to ensure that the user inputs "yes", or "no"
#use .lower() and .strip() to get rid of whitespace and make everything lower case so that the code doesn't break easily
while answer.lower().strip() != "yes" and answer.lower().strip() != "no":
  #using time.sleep() to slow down the game in order to make it easier to read, or else all the text will jump out at you
  time.sleep(2)
  print("Type a proper answer please.")
  time.sleep(2)
  answer = input("Would you like to play? Yes or No: ")

#if statement to start the quiz if user inputs "yes"
if answer.lower().strip() == "yes":
  print("")
  time.sleep(2)
  #ask user for their name
  name = input("What is your name?: ")
  time.sleep(2)
  
  #introduce the quiz and provide some basic info
  print("")
  print("Hello " + name.capitalize() + ", is a 3 part quiz to test your knowledge about hardware, software, and coding.")
  time.sleep(2)
  print("")
  print("Part 1 will be about python, part 2 will be about software, and part 3 will be about hardware, and each part has 10 questions.")
  time.sleep(3)
  
  #show the user other user's scores to show them what scores they need to get in order to win something
  print("")
  print("Here are the top 3 scores we have recieved so far:")

  time.sleep(2)
  print("1. Joe: 29/30")
  time.sleep(1)
  print("2. Beatrice: 28/30")
  time.sleep(1)
  print("3. Nate: 26/30")
  time.sleep(2)

  print("")
  print("You will need to make it onto this leaderboard in order to win a prize.")
  print("Part one will commence in 5 seconds. Good luck. ")
  time.sleep(5)

  #Part 1
  print("")
  print("Welcome to Part 1.")
  time.sleep(2)
  
  #create a variable to count the amount of correct answers
  part1_correct_answers = 0
  
  #Question one
  #print the options for multiple choice
  print("")
  time.sleep(2)
  print("A. %")  
  time.sleep(1)
  print("B. #")
  time.sleep(1)
  print("C. @")
  time.sleep(1)
  print("D. ^")
  time.sleep(1)
  print("")
  #user input to ask the question
  p1_q1 = input("Question 1: Which of these symbols is used to make a comment?: ")

  #use if/elif statement to determine whether the question is correct
  if p1_q1.lower().strip() == "b" :
    #add one point if correct
    part1_correct_answers += 1 
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")

  #Question two
  #print the options for multiple choice
  time.sleep(2)
  print("A. Multiply")  
  time.sleep(1)
  print("B. Divide")
  time.sleep(1)
  print("C. Create a blank line")
  time.sleep(1)
  print("D. Convert integers to strings")
  print("")
  #user input to ask the question
  p1_q2 = input("Question 2: What does the * symbol do?:  ")

  #use if/elif statement to determine whether the question is correct
  if p1_q2.lower().strip() == "a" :
    #add 1 point if correct
    part1_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")
  
  #Question three
  #print the options for multiple choice
  time.sleep(2)
  print("A. s.strip() ")  
  time.sleep(1)
  print("B. s.upper() ")
  time.sleep(1)
  print("C. s.rstrip([chars])")
  time.sleep(1)
  print("D. s.lstrip([chars]) ")
  print("")
  #user input to ask the question
  p1_q3 = input("Question 3: Which of these string methods removes all whitespace from an input?: ")

  #use if/elif statement to determine whether the question is correct
  if p1_q3.lower().strip() == "a" :
    #add 1 point if correct
    part1_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")

  #Question four
  #print the options for multiple choice
  time.sleep(2)
  print("A. An error that occurs while running the program. This usually happens when your program does an operation that is impossible to carry out. ")  
  time.sleep(1)
  print("B. An error that prevents your code from doing what you want it to do.")
  time.sleep(1)
  print("C. An error where Python doesn't know what to do, as there isn't sufficient whitespace. ")
  time.sleep(1)
  print("D. An error in a code due to it not following the rules of the Python language.")
  print("")
  #user input to ask the question
  p1_q4 = input("Question 4: What is a syntax error?: ")

  #use if/elif statement to determine whether the question is correct
  if p1_q4.lower().strip() == "d" :
    #add 1 point if correct
    part1_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")

  #Question five 
  #print the options for multiple choice
  time.sleep(2)
  print("A. A flaw in your code that causes Python to stop running because it is doing the same thing over and over again")
  time.sleep(1)
  print("B. An infinitly large code that is too large for python to run")
  time.sleep(1)
  print("C. A loop that keeps repeating itself over and over again")
  time.sleep(1)
  print("D. A loophole for infinite cash")
  print("")
  #user input to ask the question
  p1_q5 = input("Question 5: What is an infinite loop?: ")

  #use if/elif statement to determine whether the question is correct
  if p1_q5.lower().strip() == "c" :
    #add 1 point if correct
    part1_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")

  #Question six 
  #user input to ask the question
  p1_q6 = input("Question 6: True or Fale: Booleans can only be assigned a \"True\" or \"False\" variable: ")

  #use if/elif statement to determine whether the question is correct
  if p1_q6.lower().strip() == "true" :
    #add 1 point if correct
    part1_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")

  #Question seven
  #print the options for multiple choice
  time.sleep(2)
  print("A. ")
  time.sleep(1)
  print("B. ")
  time.sleep(1)
  print("C. ")
  time.sleep(1)
  print("D. ")
  print("")
  #user input to ask the question
  p1_q7 = input("Question 7: ")

  #use if/elif statement to determine whether the question is correct
  if p1_q7.lower().strip() == "c" :
    #add 1 point if correct
    part1_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")

  #Part 2
  print("")
  print("Welcome to part 2.")
  time.sleep(2)
  #create a variable to count the amount of correct answers
  part2_correct_answers = 0

  #Part 3
  print("")
  print("Welcome to part 3.")
  time.sleep(2)
  #create a variable to count the amount ofa correct answers
  part3_correct_answers = 0


  #Closing remarks: Scores, Leaderboards, Prizes
  print("Thanks for participating in Lucas's Tech Shop's computer parts giveaway quiz. ")
  time.sleep(2)
  
  #show user his scores
  print("Here are your quiz results: ")
  time.sleep(2)

#elif statement if they dont want to take the quiz. 
elif answer.lower().strip() == "no":
  print("")
  time.sleep(2)
  print("Have a good day. ")