def project_speech():
  print("For starters, What is your name?")
  urname = input()
  print(f"Wow your name is {urname}! I have a cousin with that name!")
  print("What Highschool did you graduate from?")
  school = input()
  print(f"Ooh yikes... I've heard some unsavory rumors about {school}.")
  print(f"So {urname}, what college did you attend or are currently attending?")
  college = input()
  print(f"Cool, {college} is actually a really solid institution.")
  print(f"So between {school} and {college} what institution was more fun and enjoyable.")
  choice = input()
  print("Interesting, I think I can see why you prefer that one")
  print(f"Thank you for this chat {urname}. I enjoyed learning that you went to {school} and {college}, but prefer {choice} the most")

def main():
  print("Hello! I am PROJECT OPERATIONAL OBJECT PROGRAM, or 'poop' for short. I will be asking a few simple questions about yourself.")
  project_speech()

if __name__ == "__main__":
  main()
