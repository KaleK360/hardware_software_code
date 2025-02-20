def main():
  print("This program adds two numbers. ")
  (num1) = input("Enter first number: ")
  (num2) = input("Enter second number: ")
  total = int(num1) + int(num2)
  print("{} + {} = {}".format(num1, num2, total))
  loop()

def loop():
  print("Type 'Con' to continue, 'End' to end the program")
  choice = input()
  lchoice = choice.lower()
  if lchoice == "con":
    main()
  elif lchoice == "end":
    exit()
  else:
    loop()

if __name__ == "__main__":
  main()
