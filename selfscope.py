print("===================================================================================")
print ("🧠 WELCOME TO SELFSCOPE — your Terminal Self Check-In & Identity Profiler.")
print("We'll be collecting highly personal data in the least secure way possible (hehe)")
print("===================================================================================\n")

# INTRO
while True:
   name = input("So first things first...who dare come into this system?: ").strip()
   if name == "":
       print("I need a name...let's try this again shall we?\n")
   elif not name.isalpha():
       print("LETTERS!!! Letters darling...your name consists of letters\n")
   else:
       break


print(f"Heyo {name}! Let's get into it!\n")

# CHECK-IN QUESTIONS
while True:
 age_input = input("How old are you, dear?: ")

 if age_input.isdigit():
    age = int(age_input)
    print(f"You are {age} years old!\n")

    if age < 0:
     print("Hey...correct me if I'm wrong (I'm not) but you've not even been born yet...\n")

    elif 25 <= age <= 33:
     print("That middle age catching up to ya huh? hehe...YOU'RE getting OOOLLLDDDDD!!!\n")

    elif 75 <= age <= 100:
     print("Dang! You've been around the block a while Oldtimer! Respect!\n")

    break

 else:
  print(f"Let's just stick to numbers...please\n")

# HEIGHT
while True:
  height_input = (input("How tall are you (in cm)?: "))

  if height_input.isdigit():
      height = float(height_input)
      print(f"You are {height} cm tall!")

      if height >= 186:
          print("Dang, my guyyyy...You better be modelling or in the NBA with this height haha. Jk Jk")
          print("You are tall!")
      elif 145 <= height <= 179:
          print("Awwww I could literally fit you into my pocket...so cute! You're short not 'average'")
          print("and that's okay! ")
      elif height <= 136:
          print("Ummmm...thanks for telling me your height?? Are you even real? 😭")
      print(f"You are {str(height)} cm tall\n")
      break

  else:
     print("Use digits...DIGITSSS! Give me your height in NUMBERS. *sigh* try again dear")

# MOOD CHECK
while True:
  mood = input("How are you ACTUALLY feeling today? (e.g tired,happy,over-it): ").lower()

  if mood == "":
     print("Nothing...you feel numb huh? Actually...same :(\n")
  elif mood == "tired":
     print("Awwww I feel you dear...maybe take a nap. Go for a lil walk or touch some grass :)\n")
     break
  elif mood == "happy":
     print("YESSSSSSS! I'm so glad to hear that! Love it for you dear :)\n")
     break
  elif mood == "over-it":
     print("Dang...that makes me and you twin. Why don't we wrap this up and go cry together (digital tears of course)\n")
     break
  else:
     print("Huh...that’s an oddly specific emotion. Noted. Moving on.\n")
     break


# SUMMARY
print("=============================================================================")
print("                 📊 GENERATING YOUR SELFSCOPE SUMMARY                          ")
print("=============================================================================")

print(f" Name: {name}")
print(f" Age: {age} years old")
print(f" Height: {height} cm")

print("==============================================================================")
print("Thanks for using selfScope — your digital mirror of judgment and a lil support")




