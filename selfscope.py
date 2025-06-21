import streamlit as st

# App header
st.markdown("### 🧠 Welcome to selfScope: Your Terminal Self Check‑In bot")
st.write("We'll ask you some semi-personal questions.")

# 1. Name
name = st.text_input("Your name (letters only):").strip()
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
            st.info("Middle‑age mode activated. 🧓")
        elif 75 <= age <= 100:
            st.info("Respect the wisdom, Old‑timer! ✨")
        else:
            st.success(f"You are {age} years old.")
    else:
        st.warning("Stick to numbers, please!")

# 3. Height
height_input = st.text_input("How tall are you (cm)?")
if height_input:
    if height_input.isdigit():
        height = float(height_input)
        if height >= 186:
            st.success("Dang, tall enough for modeling or the NBA!")
        elif 145 <= height < 186:
            st.info("Short‑ish but cute!")
        else:
            st.warning("…are you real? 😭")
        st.write(f"**Height:** {height} cm")
    else:
        st.warning("Digits only, thanks!")

# 4. Mood
mood = st.text_input("How are you feeling today?").lower()
if mood:
    if mood == "":
        st.write("Numb? Same 😐")
    elif mood == "tired":
        st.write("Go take a nap—or touch some grass.")
    elif mood == "happy":
        st.write("Love it for you! 😊")
    elif mood == "over-it":
        st.write("Me too. Digital tears?")
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
