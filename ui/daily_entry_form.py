import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from storage.data_manager import save_entry, load_entries
from report.report_generator import generate_monthly_report

MOOD_OPTIONS = ["Very Happy", "Happy", "Neutral", "Sad", "Stressed"]
WEATHER_OPTIONS = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy", "Other"]
WORK_PROGRESS_OPTIONS = ["Smooth", "Challenging", "Didn't work"]

# Set reports directory to user's Desktop
REPORTS_DIR = os.path.join(os.path.expanduser('~'), 'Desktop')
os.makedirs(REPORTS_DIR, exist_ok=True)

class DailyEntryForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Daily Reflection Journal")
        self.geometry("400x600")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        row = 0
        # Date (auto-filled)
        tk.Label(self, text="Date:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        tk.Entry(self, textvariable=self.date_var, state="readonly").grid(row=row, column=1, padx=10, pady=5)
        row += 1

        # Wake-up Time
        tk.Label(self, text="Wake-up Time:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.wakeup_var = tk.StringVar()
        tk.Entry(self, textvariable=self.wakeup_var).grid(row=row, column=1, padx=10, pady=5)
        row += 1

        # Bedtime
        tk.Label(self, text="Bedtime:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.bedtime_var = tk.StringVar()
        tk.Entry(self, textvariable=self.bedtime_var).grid(row=row, column=1, padx=10, pady=5)
        row += 1

        # Mood
        tk.Label(self, text="Mood:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.mood_var = tk.StringVar(value=MOOD_OPTIONS[2])
        ttk.Combobox(self, textvariable=self.mood_var, values=MOOD_OPTIONS, state="readonly").grid(row=row, column=1, padx=10, pady=5)
        row += 1

        # Weather
        tk.Label(self, text="Weather:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.weather_var = tk.StringVar(value=WEATHER_OPTIONS[0])
        ttk.Combobox(self, textvariable=self.weather_var, values=WEATHER_OPTIONS, state="readonly").grid(row=row, column=1, padx=10, pady=5)
        row += 1

        # Meals / Food Highlights
        tk.Label(self, text="Meals / Food Highlights:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.meals_var = tk.StringVar()
        tk.Entry(self, textvariable=self.meals_var).grid(row=row, column=1, padx=10, pady=5)
        row += 1

        # Number of Social Interactions
        tk.Label(self, text="# Social Interactions:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.social_var = tk.StringVar()
        tk.Entry(self, textvariable=self.social_var).grid(row=row, column=1, padx=10, pady=5)
        row += 1

        # Work Progress
        tk.Label(self, text="Work Progress:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.work_var = tk.StringVar(value=WORK_PROGRESS_OPTIONS[0])
        ttk.Combobox(self, textvariable=self.work_var, values=WORK_PROGRESS_OPTIONS, state="readonly").grid(row=row, column=1, padx=10, pady=5)
        row += 1

        # Gratitude
        tk.Label(self, text="Gratitude:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.gratitude_var = tk.StringVar()
        tk.Entry(self, textvariable=self.gratitude_var).grid(row=row, column=1, padx=10, pady=5)
        row += 1

        # Highlight of the Day
        tk.Label(self, text="Highlight of the Day:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.highlight_var = tk.StringVar()
        tk.Entry(self, textvariable=self.highlight_var).grid(row=row, column=1, padx=10, pady=5)
        row += 1

        # Goal Progress
        tk.Label(self, text="Goal Progress:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.goal_var = tk.StringVar()
        tk.Entry(self, textvariable=self.goal_var).grid(row=row, column=1, padx=10, pady=5)
        row += 1

        # Submit Button
        tk.Button(self, text="Submit", command=self.submit_entry).grid(row=row, column=0, columnspan=2, pady=10)
        row += 1
        # Generate Report Button
        tk.Button(self, text="Generate Monthly Report", command=self.generate_report).grid(row=row, column=0, columnspan=2, pady=10)

    def submit_entry(self):
        try:
            entry = {
                "date": self.date_var.get(),
                "wake_up_time": self.wakeup_var.get(),
                "bedtime": self.bedtime_var.get(),
                "mood": self.mood_var.get(),
                "weather": self.weather_var.get(),
                "meals": self.meals_var.get(),
                "social_interactions": int(self.social_var.get()),
                "work_progress": self.work_var.get(),
                "gratitude": self.gratitude_var.get(),
                "highlight": self.highlight_var.get(),
                "goal_progress": self.goal_var.get(),
            }
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for social interactions.")
            return

        # Basic validation
        if not entry["wake_up_time"] or not entry["bedtime"]:
            messagebox.showerror("Input Error", "Please fill in wake-up time and bedtime.")
            return

        save_entry(entry)
        messagebox.showinfo("Success", "Entry saved!")
        self.clear_form()

    def clear_form(self):
        self.wakeup_var.set("")
        self.bedtime_var.set("")
        self.mood_var.set(MOOD_OPTIONS[2])
        self.weather_var.set(WEATHER_OPTIONS[0])
        self.meals_var.set("")
        self.social_var.set("")
        self.work_var.set(WORK_PROGRESS_OPTIONS[0])
        self.gratitude_var.set("")
        self.highlight_var.set("")
        self.goal_var.set("")
        self.date_var.set(datetime.now().strftime("%Y-%m-%d"))

    def generate_report(self):
        month = simpledialog.askstring("Generate Report", "Enter month (YYYY-MM):", parent=self)
        if not month:
            return
        entries = load_entries(month)
        if not entries:
            messagebox.showerror("No Data", f"No entries found for {month}.")
            return
        output_path = os.path.join(REPORTS_DIR, f"report_{month}.html")
        try:
            generate_monthly_report(entries, output_path)
            messagebox.showinfo("Report Generated", f"HTML report saved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate report: {e}")

def launch_daily_entry_form():
    app = DailyEntryForm()
    app.mainloop() 