# Magic 8-Ball
# The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.

# Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

# Magic 8-Ball, should I do this project?

# We’ll be using the following 9 possible answers for our Magic 8-Ball:

# Yes - definitely.
# It is decidedly so.
# Without a doubt.
# Reply hazy, try again.
# Ask again later.
# Better not tell you now.
# My sources say no.
# Outlook not so good.
# Very doubtful.
# The output of the program will have the following format:

# [Name] asks: [Question]
# Magic 8-Ball’s answer: [Answer]
# For example:

# Joe asks: Is this real life?
# Magic 8-Ball's answer: Better not tell you now
# Let’s get started!

import random
name = 'Local Dude'
question = ""
answer = ""

random_number = random.randint(1,15)

#print (random_number)

if random_number == 1:
  answer = 'Yes - definetely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = 'Better not tell you know'
elif random_number == 7:
  answer= "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Je sais pas groooooos!"
elif random_number == 11:
  answer = "non sérieux je suis juste une boule"
elif random_number == 12:
  answer = "tu me soules tellement je réponds en français"
elif random_number == 13:
  answer = "Warum ? Raus ! Schnell !"
elif random_number == 14:
  answer = "Traverse la rue"
elif random_number == 15:
  answer = "Bon moi je vais au bar"
else: 
  answer = "Error"

if name == "":
  print ("Question: " + question)
elif question == "":
  print ("Sorry you must ask a question")
else:
  print (name + ' asks: ' + question)
  print ("Magic 8-Ball's answer: " + answer)