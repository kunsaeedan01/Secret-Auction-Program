from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

restart = "yes"
auction = {}

while restart == "yes":
  name = input("What is your name?")
  bid = int(input("What is your bid?"))
  auction[name] = bid
  restart = input("Is there are another person?")
  if restart == "yes":
    clear()

list_for_compare = []


for key in auction:
  list_for_compare.append(auction[key])

highest = max(list_for_compare)
winner = ""

for key in auction:
  if auction[key] == highest:
    winner = key

print(f"Winner is {winner} with a bid ${highest}")







