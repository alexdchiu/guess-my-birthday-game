from random import randint
name = input("Hi! What is your name?")

months = [
  "January", 
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
]

for count in range(5):
  month = randint(0,11)
  year = randint(1924,2004)
  print("Guess", count + 1, ": ", name, "were you born in", months[month], year)
  response = input("yes or no?")
  if response == "yes":
    print("I knew it!")
    break
  elif response == "no" and count < 4:
    print("Drat! Lemme try again!")
  else:
    print ("I have other things to do. Good bye.")