def introduction():
  print("Welcome to the Random Questions Program!")
  print("This program will ask you various interesting questions.")
  print("You can type 'exit' at any time to end the program.")

def get_question(count):
  questions = [
      "What's the best pizza topping?: ",
      "Which came first? The chicken or the egg?: ",
      "Are we living in a dream, simulation, or reality?: ",
      "Are Hotdogs sandwiches?: "
  ]
  return questions[count % 4]

def closing_statement(question_count):
  print(f"\nThank you for participating!")
  print(f"You answered {question_count} question{'s' if question_count != 1 else ''}.")

def main():
  introduction()
  question_count = 0

  while True:
      question = get_question(question_count)
      answer = input(question).strip().lower()

      if answer == "exit":
          closing_statement(question_count)
          break

      question_count += 1

if __name__ == "__main__":
  main()
