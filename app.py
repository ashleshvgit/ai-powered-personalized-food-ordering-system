import streamlit as st
from utils.llm import (generate_health_plan,ask_follow_up_question)
from utils.response_handler import add_message

st.set_page_config(
    page_title="AI Health Assistant By Ashlesh",page_icon="🩺",layout="wide")

st.title("AI Personalized Health & Wellness Assistant")

st.write("Provide your basic information and wellness goals "
    "to receive a personalized general wellness plan.")

st.warning("This application provides general wellness and "
    "nutrition information. It does not diagnose medical "
    "conditions or prescribe medicines. Consult a qualified "
    "healthcare professional for personalized medical advice.")

st.header("Your Profile")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age",min_value=13,max_value=100,value=25)


with col2:
    gender = st.selectbox("Gender",["Female","Male","Prefer not to say"])

col3, col4 = st.columns(2)
with col3:
    height = st.number_input("Height (cm)",min_value=100.0,max_value=250.0,value=165.0)

with col4:
    weight = st.number_input("Weight (kg)",min_value=25.0,max_value=300.0,value=60.0)



st.header("Diet Information")

diet_type = st.selectbox("Diet Type",["Vegetarian","Non-Vegetarian","Vegan","Eggetarian"])
food_preferences = st.text_input("Food Preferences",placeholder=("Example: South Indian food, rice, fruits, curd"))
allergies = st.text_input("Food Allergies / Foods to Avoid",placeholder=("Example: peanuts, shellfish, lactose"))



st.header("Your Goal")
goal = st.selectbox("What is your primary goal?",["Weight Loss", "Weight Gain", "Weight Maintenance", "General Fitness", "Healthy Eating"])
activity_level = st.selectbox("Activity Level",["Sedentary","Lightly Active","Moderately Active","Very Active"])


st.header("Lifestyle")
col5, col6 = st.columns(2)
with col5:
    meals_per_day = st.selectbox("Meals Per Day",[2, 3, 4, 5, 6])

with col6:
    sleep_hours = st.number_input("Average Sleep (hours)",min_value=1.0, max_value=16.0, value=7.0,step=1.0)


water_intake = st.number_input("Approximate Water Intake (liters/day)",
    min_value=0.0,max_value=10.0,value=2.0)


additional_information = st.text_area("Anything else you want the assistant to know?",
    placeholder=("Example: I prefer simple home-cooked meals. "
        "I don't like very spicy food."))

if st.button("Generate My Wellness Plan",type="primary"):
    user_data = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "diet_type": diet_type,
        "goal": goal,
        "activity_level": activity_level,
        "food_preferences": food_preferences,
        "allergies": allergies,
        "meals_per_day": meals_per_day,
        "sleep_hours": sleep_hours,
        "water_intake": water_intake,
        "additional_information":additional_information}

    with st.spinner("Creating your personalized wellness plan..."):
        try:
            plan = generate_health_plan(user_data)
            st.session_state["user_data"] = user_data
            st.session_state["health_plan"] = plan
            st.session_state["messages"] = []
            st.success("Your wellness plan has been generated!")

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")


if "health_plan" in st.session_state:
    st.divider()
    st.header("Your Personalized Wellness Plan")
    st.markdown(st.session_state["health_plan"])

if "health_plan" in st.session_state:
    st.divider()
    st.header("Ask Your Follow-up Questions")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask something about your wellness plan...")
    if question:
        with st.chat_message("user"):
            st.markdown(question)

        add_message(st.session_state.messages,"user",question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    answer = ask_follow_up_question(st.session_state["user_data"],question)
                    st.markdown(answer)

                except Exception as e:
                    answer = ("Sorry, I couldn't process ""your question.")
                    st.error(f"Error: {str(e)}")


        add_message(st.session_state.messages,"assistant",answer)