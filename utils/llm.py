from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.prompts import (HEALTH_PLAN_PROMPT,QUESTION_PROMPT)
load_dotenv()

def get_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0.2)
    return llm

def generate_health_plan(user_data):
    llm = get_llm()
    prompt = HEALTH_PLAN_PROMPT.format(
        age=user_data["age"],
        gender=user_data["gender"],
        height=user_data["height"],
        weight=user_data["weight"],
        diet_type=user_data["diet_type"],
        goal=user_data["goal"],
        activity_level=user_data["activity_level"],
        food_preferences=user_data["food_preferences"],
        allergies=user_data["allergies"],
        meals_per_day=user_data["meals_per_day"],
        sleep_hours=user_data["sleep_hours"],
        water_intake=user_data["water_intake"],
        additional_information=user_data[
            "additional_information"])

    response = llm.invoke(prompt)
    return response.text


def ask_follow_up_question(user_data,question):
    llm = get_llm()
    prompt = QUESTION_PROMPT.format(
        age=user_data["age"],
        gender=user_data["gender"],
        height=user_data["height"],
        weight=user_data["weight"],
        diet_type=user_data["diet_type"],
        goal=user_data["goal"],
        activity_level=user_data["activity_level"],
        question=question)
    response = llm.invoke(prompt)
    return response.text