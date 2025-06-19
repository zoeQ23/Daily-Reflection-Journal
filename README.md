# 📝 Daily Reflection Journal

**Daily Reflection Journal** is a desktop journaling application built with Python and Tkinter. It helps users reflect on daily experiences—like mood, meals, sleep, and productivity—through a simple guided interface. At the end of each month, the app automatically generates a structured summary report based on the collected data.

This project was created from scratch as a personal tool and coding practice while learning Python using the Cursor AI coding assistant.


## Features

- Daily journaling via a desktop GUI
- Track mood, sleep, meals, weather, goals, and more
- Automatic generation of monthly summary reports
- Organized local data storage (JSON or CSV)
- Modular project structure using folders like `ui`, `data`, `report`, `storage`


## How to Run

1. **Clone the repository**

```bash
git clone https://github.com/zoeQ23/Daily-Reflection-Journal.git
cd Daily-Reflection-Journal
````

2. **(Optional) Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Launch the application**

```bash
python main.py
```

A Tkinter window will open, allowing you to input your daily reflections.


## Project Structure

```
Daily-Reflection-Journal/
│
├── main.py                 # App entry point
├── requirements.txt        # Python dependencies
│
├── ui/                     # GUI layout and components
├── data/                   # Stores user logs (daily entries)
├── report/                 # Generates monthly summaries
├── storage/                # File I/O logic and helpers
├── venv/                   # (Optional) Virtual environment
```


## Sample Daily Questions

* What did you eat today?
* What time did you wake up and go to bed?
* How was your mood?
* What was the weather like?
* Did you complete your goals?
* How many people did you talk to?
* What are you grateful for?


## Built With

* Python 3
* Tkinter (for GUI)
* Cursor (AI-native coding editor)


## Future Improvements

* Export report to PDF
* Add simple visualizations (e.g., mood trend graph)
* Password-protected journal
* Add weather integration or reminder notifications


## 👩🏻‍💻 Author

Created by [zoeQ23](https://github.com/zoeQ23) — as a personal passion project while learning backend development and exploring journaling tools.
