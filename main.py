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
  print("Hello " + name + ", is a 3 part quiz to test your knowledge about hardware, software, and coding.")
  time.sleep(2)
  print("Part 1 will be about python, part 2 will be about software, and part 3 will be about hardware, and each part has 10 questions.")
  time.sleep(3)
  
  #show the user other user's scores to show them what scores they need to get in order to win something
  print("Here are the top 3 scores we have recieved so far:")

  time.sleep(2)
  print("1. Joe: 29/30")
  time.sleep(1.5)
  print("2. Beatrice: 28/30")
  time.sleep(1.5)
  print("3. Nate: 26/30")
  time.sleep(1.5)

  print("You will need to make it onto this leaderboard in order to win a prize.")
  print("Part one will commence in 5 seconds. Good luck. ")
  time.sleep(5)


  #Part 1
  print("Welcome to Part 1.")
  time.sleep(2)
  #create a variable to count the amount of correct answers
  part1_correct_answers = 0
  print("Question 1: ")


  #Part 2
  print("Welcome to part 2.")
  time.sleep(2)
  #create a variable to count the amount of correct answers
  part2_correct_answers = 0

  #Part 3
  print("Welcome to part 3.")
  time.sleep(2)
  #create a variable to count the amount of correct answers
  part3_correct_answers = 0


  #Closing remarks: Scores, Leaderboards, Prizes
  print("Thanks for participating in Lucas's Tech Shop's computer parts giveaway quiz. ")
  time.sleep(2)
  
  #show user his scores
  print("Here are your quiz results: ")
  time.sleep(2)
  