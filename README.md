# 🧠 GPT + Task Chatbot

An AI-powered chatbot that combines the flexibility of OpenAI's GPT with built-in task commands like reminders, weather checks, and time lookup — all within a simple web interface built using Flask.

---

## 🚀 Features

- 💬 **Chat with GPT-4** using OpenAI's API
- ⏰ `/time` – Get the current system time
- 🌦️ `/weather [city]` – Get real-time weather data using WeatherAPI
- 📝 `/remind me to [task] at [time]` – Set and store reminders (persisted in SQLite)
- 🌐 Simple web frontend styled with Tailwind CSS or Bootstrap
- 🗂️ Organized backend using Flask, SQLAlchemy, and dotenv

---

## 🧰 Tech Stack

- **Backend**: Python, Flask, OpenAI API, SQLAlchemy, WeatherAPI
- **Frontend**: HTML, JavaScript, Tailwind CSS or Bootstrap
- **Database**: SQLite
- **Deployment**: Render-compatible with `Procfile`

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/gpt-task-chatbot.git
cd gpt-task-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your API Keys

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key
WEATHER_API_KEY=your_weatherapi_key
```

### 5. Run the App

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🛠 Example Commands

```
/time
/weather London
/remind me to call mom at 6pm
```

Or just ask:  
> What's the capital of France?

---

## 🌍 Deployment

To deploy on **Render**:

1. Add environment variables (`OPENAI_API_KEY`, `WEATHER_API_KEY`)
2. Add a `Procfile` in your project root:

```
web: gunicorn app:app
```

3. Push to GitHub and connect the repo to [Render.com](https://render.com)

---

## 📄 License

MIT — feel free to use and adapt!

---

## 🙌 Acknowledgments

- [OpenAI](https://platform.openai.com/)
- [WeatherAPI](https://www.weatherapi.com/)
- [Flask](https://flask.palletsprojects.com/)