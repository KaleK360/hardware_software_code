def main():
  print("This program adds two numbers. ")
  num1 = input("Enter first number: ")
  num2 = input("Enter second number: ")
  total = num1 + num2
  print("{} + {} = {}".format(num1, num2, total))
  print("Type 'Con' to continue, 'End' to end te program")
  choice = input()
  lchoice = choice.lower()
  if lchoice == "con":
    main()
  elif lchoice == "end":
    exit()

if __name__ == "__main__":
  main()
