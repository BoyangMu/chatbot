from flask import Flask, request, jsonify, render_template
import openai
import os
import re
import requests
from dotenv import load_dotenv
from datetime import datetime
from openai import OpenAI

load_dotenv()
app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
weather_api_key = os.getenv("WEATHER_API_KEY")

reminders = []  # Store reminders in memory for now

def handle_task_command(message):
    if message.startswith("/time"):
        return f"The current time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    if message.startswith("/weather"):
        match = re.search(r"/weather\s+(.+)", message)
        if match:
            city = match.group(1)
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
            res = requests.get(url).json()
            if res.get("cod") != 200:
                return "Sorry, I couldn't find the weather for that city."
            weather = res["weather"][0]["description"]
            temp = res["main"]["temp"]
            return f"Weather in {city}: {weather}, {temp}°C"
        return "Please provide a city like `/weather London`"

    if message.startswith("/remind me to"):
        match = re.search(r"/remind me to (.+) at (.+)", message)
        if match:
            task, time = match.groups()
            reminders.append((task, time))
            return f"Reminder set: {task} at {time}"
        return "Please format like `/remind me to buy milk at 5pm`"

    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    # Handle task commands
    task_response = handle_task_command(user_input)
    if task_response:
        return jsonify({"response": task_response})

    # Fallback to GPT
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that also understands commands like /time, /weather, and /remind."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error: {str(e)}"

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)