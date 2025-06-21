import streamlit as st

# App header
st.markdown("### 🧠 Welcome to selfScope: Your Terminal Self Check‑In bot")
st.write("We'll ask you some semi-personal questions.")

# 1. Name
name = st.text_input("What's your first name? (letters only):").strip()
if name:
    if not name.isalpha():
        st.warning("Letters only, please!")
    else:
        st.success(f"Heyo **{name}**! Moving on…")

# 2. Age
age_input = st.text_input("How old are you, dear?:")
if age_input:
    if age_input.isdigit():
        age = int(age_input)
        if age < 0:
            st.warning("Not born yet? ")
        elif 25 <= age <= 33:
            st.info("""Dang,hate to break it to you but... ummm you might want to take it easy on your knees.
                    You're old sir/ma'am hehe""")
        elif 75 <= age <= 100:
            st.info("You been around a whilw huh? Respect! Wish you a beautiful day today!")
        else:
            st.success(f"You are {age} years old.")
    else:
        st.warning("Numbers please...NUMBERS PLEASEE!! NUMBERS!!!")

# 3. Height
height_input = st.text_input("How tall are you (cm)?")
if height_input:
    if height_input.isdigit():
        height = float(height_input)
        if height >= 186:
            st.success("Dang! you should be modelling or in the NBA! You're tall my guy! (stop smiling...you're just tall)")
        elif 145 <= height < 186:
            st.info("""Blessed is the one who doesn't get confused that they are "average height" 
            and accept the FACT taht they are short. Yes...YOU are SHORT! and that's okay :)""")
        else:
            st.warning("…are you even real? 😭")
        st.write(f"**Height:** {height} cm")
    else:
        st.warning("Digits only, thanks!")

# 4. Mood
mood = st.text_input("How are you feeling today? (tired, happy, sad, over-it)").lower()
if mood:
    if mood == "":
        st.write("Numb? Same 😐")
    elif mood == "tired":
        st.write("Go take a nap! You've worked hard! (unless you've been on your phone too long!!)")
    elif mood == "sad":
        st.write("Awww sending digital hugs your way! You'll be fine!")
    elif mood == "happy":
        st.write("Love it for you! makes one of us lol")
    elif mood == "over-it":
        st.write(f"Real! Me too {name}, me too...we'll be alright! ")
    else:
        st.write(f"That’s… specific. Noted.")

# 5. Summary
if st.button("Generate SelfScope Summary"):
    if name and age_input.isdigit() and height_input.isdigit():
        st.markdown("––– 📊 **SelfScope Summary** –––")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age} years")
        st.write(f"**Height:** {height} cm")
        st.write("Thanks for checking in.")
    else:
        st.error("Make sure name, age, and height are valid first!")

# Converted terminal version to Streamlit app!
