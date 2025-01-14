import random

def generatePassword(smartPassword):
  password = ""

  if smartPassword == "Y":
    print("Smart password in being used")
  elif smartPassword == "N":
    print("Smart password in not being used, regular password is")
  else:
    print("Please choose a viable option...")

  return password

useSmartPassword = str(input("Generate a smart password [Y] or [N]: "))

generatePassword(useSmartPassword)
