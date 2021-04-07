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
  print("Part 1 will be about python, part 2 will be about software/malware, and part 3 will be about hardware, and each part has 10 questions.")
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
  time.sleep(1)
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

  #use while statement to ensure code doesnt break easily
  while p1_q1.lower().strip() != "a" and p1_q1.lower().strip() != "b" and p1_q1.lower().strip() != "c" and p1_q1.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
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
  p1_q2 = input("Question 2: What does the * symbol do?: ")

  #use while statement to ensure code doesnt break easily
  while p1_q2.lower().strip() != "a" and p1_q2.lower().strip() != "b" and p1_q2.lower().strip() != "c" and p1_q2.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p1_q2 = input("Question 2: What does the * symbol do?: ")
    

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

  #use while statement to ensure code doesnt break easily
  while p1_q3.lower().strip() != "a" and p1_q3.lower().strip() != "b" and p1_q3.lower().strip() != "c" and p1_q3.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p1_q1 = input("Question 3: Which of these string methods removes all whitespace from an input?: ")

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

  #use while statement to ensure code doesnt break easily
  while p1_q4.lower().strip() != "a" and p1_q4.lower().strip() != "b" and p1_q4.lower().strip() != "c" and p1_q4.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
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

  #use while statement to ensure code doesnt break easily
  while p1_q5.lower().strip() != "a" and p1_q5.lower().strip() != "b" and p1_q5.lower().strip() != "c" and p1_q5.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
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

  #use while statement to ensure code doesnt break easily
  while p1_q6.lower().strip() != "true" and p1_q6.lower().strip() != "false":
    print("Please input either \"True\" or \"False\".")
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
  print("A. 1variablename")
  time.sleep(1)
  print("B. variable_name")
  time.sleep(1)
  print("C. My_variable_name")
  time.sleep(1)
  print("D. variablename")
  print("")
  #user input to ask the question
  p1_q7 = input("Question 7: Which of these are not a valid variable name?: ")

  #use while statement to ensure code doesnt break easily
  while p1_q7.lower().strip() != "a" and p1_q7.lower().strip() != "b" and p1_q7.lower().strip() != "c" and p1_q7.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p1_q7 = input("Question 7: Which of these symbols is used to make a comment?: ")

  #use if/elif statement to determine whether the question is correct
  if p1_q7.lower().strip() == "a" :
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

  #Question eight
  #print the options for multiple choice
  time.sleep(2)
  print("A. **")
  time.sleep(1)
  print("B. //")
  time.sleep(1)
  print("C. %")
  time.sleep(1)
  print("D. ^")
  print("")
  #user input to ask the question
  p1_q8 = input("Question 8: Which of these are not a Python operator?: ")

  #use while statement to ensure code doesnt break easily
  while p1_q8.lower().strip() != "a" and p1_q8.lower().strip() != "b" and p1_q8.lower().strip() != "c" and p1_q8.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p1_q8 = input("Question 8: Which of these are not a Python operator?: ")

  #use if/elif statement to determine whether the question is correct
  if p1_q8.lower().strip() == "d" :
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
  time.sleep(0.5)
  #create a variable to count the amount of correct answers
  part2_correct_answers = 0

  #Question one
  #print the options for multiple choice
  print("A. iOS")
  time.sleep(1)
  print("B. Linux")
  time.sleep(1)
  print("C. Windows")
  time.sleep(1)
  print("D. Mac OS")
  print("")
  #user input to ask the question
  p2_q1 = input("Question 1: What is the most widely used operating system in the world?: ")

  #use while statement to ensure code doesnt break easily
  while p2_q1.lower().strip() != "a" and p2_q1.lower().strip() != "b" and p2_q1.lower().strip() != "c" and p2_q1.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p2_q1 = input("Question 1: What is the most widely used operating system in the world?: ")

  #use if/elif statement to determine whether the question is correct
  if p2_q1.lower().strip() == "c" :
    #add 1 point if correct
    part2_correct_answers += 1
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
  print("A. Steve Jobs")
  time.sleep(1)
  print("B. Bill Gates")
  time.sleep(1)
  print("C. Steve \"Woz\" Wozniak")
  time.sleep(1)
  print("D. Both A and B")
  print("")
  #user input to ask the question
  p2_q2 = input("Question 1: Who founded Apple?: ")

  #use while statement to ensure code doesnt break easily
  while p2_q2.lower().strip() != "a" and p2_q2.lower().strip() != "b" and p2_q2.lower().strip() != "c" and p2_q2.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p2_q2 = input("Question 1: Who founded Apple?: ")

  #use if/elif statement to determine whether the question is correct
  if p2_q2.lower().strip() == "d" :
    #add 1 point if correct
    part2_correct_answers += 1
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
  print("A. Apple")
  time.sleep(1)
  print("B. Xerox")
  time.sleep(1)
  print("C. Samsung")
  time.sleep(1)
  print("D. Microsoft")
  print("")
  #user input to ask the question
  p2_q3 = input("Question 4: Which company was the first to have a graphics user interface (GUI) and mouse?: ")

  #use while statement to ensure code doesnt break easily
  while p2_q3.lower().strip() != "a" and p2_q3.lower().strip() != "b" and p2_q3.lower().strip() != "c" and p2_q3.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p2_q3 = input("Question 4: Which company was the first to have a graphics user interface (GUI) and mouse?: ")

  #use if/elif statement to determine whether the question is correct
  if p2_q3.lower().strip() == "b" :
    #add 1 point if correct
    part2_correct_answers += 1
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
  print("A. A malware that replicates itself to spread, and destroys data files on your computer")
  time.sleep(1)
  print("B. A malware that hides its true intentions of causing harm to your computer by pretending to be something it isn't")
  time.sleep(1)
  print("C. A malware that holds yours files \"hostage\", and demands a ransom in return for them")
  time.sleep(1)
  print("D. A monitoring spyware that tracks every key typed on the keyboard")
  print("")
  #user input to ask the question
  p2_q4 = input("Question 4: What is keylogging malware?: ")

  #use while statement to ensure code doesnt break easily
  while p2_q4.lower().strip() != "a" and p2_q4.lower().strip() != "b" and p2_q4.lower().strip() != "c" and p2_q4.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p2_q4 = input("Question 4:: What is keylogging malware?: ")

  #use if/elif statement to determine whether the question is correct
  if p2_q4.lower().strip() == "c" :
    #add 1 point if correct
    part2_correct_answers += 1
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
  print("A. A malware that replicates itself to spread, and destroys data files on your computer")
  time.sleep(1)
  print("B. A malware that hides its true intentions of causing harm to your computer by pretending to be something it isn't")
  time.sleep(1)
  print("C. A malware that holds yours files \"hostage\", and demands a ransom in return for them")
  time.sleep(1)
  print("D. A monitoring spyware that tracks every key typed on the keyboard")
  print("")
  #user input to ask the question
  p2_q5 = input("Question 5: What is trojan malware?: ")

  #use while statement to ensure code doesnt break easily
  while p2_q5.lower().strip() != "a" and p2_q5.lower().strip() != "b" and p2_q5.lower().strip() != "c" and p2_q5.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p2_q5 = input("Question 5: What is trojan malware?: ")

  #use if/elif statement to determine whether the question is correct
  if p2_q5.lower().strip() == "c" :
    #add 1 point if correct
    part2_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")

  #Question six
  #print the options for multiple choice
  print("A. Chrome OS")
  time.sleep(1)
  print("B. Call of Duty: Modern Warfare")
  time.sleep(1)
  print("C. Nvidia GForce Experience")
  time.sleep(1)
  print("D. Razer Cortex")
  print("")
  #user input to ask the question
  p2_q6 = input("Question 5: Which of these is an example of application software?: ")

  #use while statement to ensure code doesnt break easily
  while p2_q6.lower().strip() != "a" and p2_q6.lower().strip() != "b" and p2_q6.lower().strip() != "c" and p2_q6.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p2_q6 = input("Question 5: Which of these is an example of application software?: ")

  #use if/elif statement to determine whether the question is correct
  if p2_q6.lower().strip() == "b" :
    #add 1 point if correct
    part2_correct_answers += 1
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
  print("A. Software dedicated to performing everyday computing tasks")
  time.sleep(1)
  print("B. Software that provides the platform for all the other software and hardware on the computer to operate.")
  time.sleep(1)
  print("C. Software used to create multimedia")
  time.sleep(1)
  print("D. Software used for organize/consume media files, such as images, video, and music")
  print("")
  #user input to ask the question
  p2_q7 = input("Question 7: What is multimedia  software?: ")

  #use while statement to ensure code doesnt break easily
  while p2_q7.lower().strip() != "a" and p2_q7.lower().strip() != "b" and p2_q7.lower().strip() != "c" and p2_q7.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p2_q7 = input("Question 7: What is multimedia  software?: ")

  #use if/elif statement to determine whether the question is correct
  if p2_q7.lower().strip() == "d" :
    #add 1 point if correct
    part2_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")

  #Question eight
  #print the options for multiple choice
  print("A. Software dedicated to performing everyday computing tasks")
  time.sleep(1)
  print("B. Software that provides the platform for all the other software and hardware on the computer to operate.")
  time.sleep(1)
  print("C. Software used to create multimedia")
  time.sleep(1)
  print("D. Software used for browsing and viewing the internet")
  print("")
  #user input to ask the question
  p2_q8 = input("Question 8: What is design  software?: ")

  #use while statement to ensure code doesnt break easily
  while p2_q8.lower().strip() != "a" and p2_q8.lower().strip() != "b" and p2_q8.lower().strip() != "c" and p2_q8.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p2_q8 = input("Question 8: What is design  software?: ")

  #use if/elif statement to determine whether the question is correct
  if p2_q8.lower().strip() == "c" :
    #add 1 point if correct
    part2_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")

  #Part 3
  print("")
  print("Welcome to part 3.")
  time.sleep(0.5)
  
  #create a variable to count the amount of correct answers
  part3_correct_answers = 0

  #Question one
  #print the options for multiple choice
  print("A. Motherboard")
  time.sleep(1)
  print("B. Central Processing Unit (CPU)")
  time.sleep(1)
  print("C. Monitor")
  time.sleep(1)
  print("D. Graphics Card")
  print("")
  #user input to ask the question
  p3_q1 = input("Question 1: What part is considered to be the brain of a computer?: ")

  #use while statement to ensure code doesnt break easily
  while p3_q1.lower().strip() != "a" and p3_q1.lower().strip() != "b" and p3_q1.lower().strip() != "c" and p3_q1.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p3_q1 = input("Question 1: ")

  #use if/elif statement to determine whether the question is correct
  if p3_q1.lower().strip() == "b" :
    #add 1 point if correct
    part3_correct_answers += 1
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
  print("A. DPI")
  time.sleep(1)
  print("B. Thread count")
  time.sleep(1)
  print("C. RPM")
  time.sleep(1)
  print("D. Storage capacity")
  print("")
  #user input to ask the question
  p3_q1 = input("Question 2: Which of these specifications relates to a mouse?: ")

  #use while statement to ensure code doesnt break easily
  while p3_q2.lower().strip() != "a" and p3_q2.lower().strip() != "b" and p3_q2.lower().strip() != "c" and p3_q2.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p3_q2 = input("Question 1: Which of these specifications relates to a mouse?: ")

  #use if/elif statement to determine whether the question is correct
  if p3_q2.lower().strip() == "b" :
    #add 1 point if correct
    part3_correct_answers += 1
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
  print("A. Dots per inch")
  time.sleep(1)
  print("B. Disks per interval")
  time.sleep(1)
  print("C. Drives per interface")
  time.sleep(1)
  print("D. It doesn't mean anything. ")
  print("")
  #user input to ask the question
  p3_q3 = input("Question 3: What does DPI stand for?: ")

  #use while statement to ensure code doesnt break easily
  while p3_q3.lower().strip() != "a" and p3_q3.lower().strip() != "b" and p3_q3.lower().strip() != "c" and p3_q3.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p3_q3 = input("Question 3: What does DPI mean?: ")

  #use if/elif statement to determine whether the question is correct
  if p3_q3.lower().strip() == "a" :
    #add 1 point if correct
    part3_correct_answers += 1
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
  print("A. Inputs info into the computer by pushing buttons and keys to input characters and functions")
  time.sleep(1)
  print("B. Supply power to different parts of the computer")
  time.sleep(1)
  print("C. Proving short term memory for the computer")
  time.sleep(1)
  print("D. Connecting all the components of a computer together to work on a single platform")
  print("")
  #user input to ask the question
  p3_q4 = input("Question 4: What is the primary function of the motherboard?: ")

  #use while statement to ensure code doesnt break easily
  while p3_q4.lower().strip() != "a" and p3_q4.lower().strip() != "b" and p3_q4.lower().strip() != "c" and p3_q4.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p3_q4 = input("Question 4: What is the primary function of the motherboard?: ")

  #use if/elif statement to determine whether the question is correct
  if p3_q4.lower().strip() == "b" :
    #add 1 point if correct
    part3_correct_answers += 1
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
  print("A. Mouse")
  time.sleep(1)
  print("B. Monitor")
  time.sleep(1)
  print("C. RAM")
  time.sleep(1)
  print("D. Connections/Ports")
  print("")
  #user input to ask the question
  p3_q5 = input("Question 5: Which of these is not a peripheral component?: ")

  #use while statement to ensure code doesnt break easily
  while p3_q5.lower().strip() != "a" and p3_q5.lower().strip() != "b" and p3_q5.lower().strip() != "c" and p3_q5.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    p3_q5 = input("Question 5: Which of these is not a peripheral component?: ")

  #use if/elif statement to determine whether the question is correct
  if p3_q5.lower().strip() == "c" :
    #add 1 point if correct
    part3_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")

  #Question six
  #print the options for multiple choice
  print("A. Refresh rate")
  time.sleep(1)
  print("B. Revolutions per minute (RPM)")
  time.sleep(1)
  print("C. Interface")
  time.sleep(1)
  print("D. Storage Capacity")
  print("")
  #user input to ask the question
  p3_q6 = input("Question 6: Which of these is not a specification related to the hard drive?: ")

  #use while statement to ensure code doesnt break easily
  while p3_q6.lower().strip() != "a" and p3_q6.lower().strip() != "b" and p3_q6.lower().strip() != "c" and p3_q6.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    #re-ask the question so the user can give a proper answer and get out of the while loop
    p3_q6 = input("Question 6: Which of these is not a specification related to the hard drive?: ")

  #use if/elif statement to determine whether the question is correct
  if p3_q6.lower().strip() == "a" :
    #add 1 point if correct
    part3_correct_answers += 1
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
  print("A. Graphics Processing Unit(GPU)")
  time.sleep(1)
  print("B. Headphones/Speaker")
  time.sleep(1)
  print("C. Hard Drive")
  time.sleep(1)
  print("D. Power Supply")
  print("")
  #user input to ask the question
  p3_q7 = input("Question 7: Which of these is not an internal component?: ")

  #use while statement to ensure code doesnt break easily
  while p3_q7.lower().strip() != "a" and p3_q7.lower().strip() != "b" and p3_q7.lower().strip() != "c" and p3_q7.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    #re-ask the question so the user can give a proper answer and get out of the while loop
    p3_q7 = input("Question 7: Which of these is not an internal component?: ")

  #use if/elif statement to determine whether the question is correct
  if p3_q7.lower().strip() == "b" :
    #add 1 point if correct
    part3_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")

  #Question eight
  #print the options for multiple choice
  print("A. Refresh Rate")
  time.sleep(1)
  print("B. Cache")
  time.sleep(1)
  print("C. Resolution")
  time.sleep(1)
  print("D. Frequency Range")
  print("")
  #user input to ask the question
  p3_q8 = input("Question 8: Which is a specification is a specification related to speakers and headphones?: ")

  #use while statement to ensure code doesnt break easily
  while p3_q8.lower().strip() != "a" and p3_q8.lower().strip() != "b" and p3_q8.lower().strip() != "c" and p3_q8.lower().strip() != "d":
    print("Please type the letter corresponding with your answer.")
    #re-ask the question so the user can give a proper answer and get out of the while loop
    p3_q8 = input("Question 8: Which is a specification is a specification related to speakers and headphones?: ")

  #use if/elif statement to determine whether the question is correct
  if p3_q8.lower().strip() == "d" :
    #add 1 point if correct
    part3_correct_answers += 1
    time.sleep(1)
    print("")
    print("Correct.")
    print("")
  else:
    print("")
    print("Wrong.")
    print("")
  
  #Closing remarks: Print scores, let the user know if they have qualified to win anything
  print("Thanks for participating in Lucas's Tech Shop's computer parts giveaway quiz. ")
  time.sleep(1.5)
  
  #show user his scores
  print("Here are your quiz results: ")
  time.sleep(2)

#elif statement if they dont want to take the quiz. 
elif answer.lower().strip() == "no":
  print("")
  time.sleep(2)
  print("Have a good day. ")  