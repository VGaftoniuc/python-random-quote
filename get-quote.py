import random

def quote_bot():

  with open("quotes.txt") as f:
    quotes = f.readlines()

  control = int(input("How many random quotes would you like to see ? "))
  last = len(quotes) - 1

  if control in range(0, last):
    end = control
  else:
    end = last

  for c in range(0, end):
    print('"' + quotes[random.randint(0, last)].strip("\n") + '"')

if __name__== "__main__":
  quote_bot()
