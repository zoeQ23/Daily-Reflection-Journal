from collections import Counter
from datetime import datetime

def generate_monthly_report(entries, output_path):
    if not entries:
        raise ValueError("No entries to report.")

    entries = sorted(entries, key=lambda e: e['date'])
    month = entries[0]['date'][:7]

    def parse_time(t):
        try:
            return datetime.strptime(t, "%H:%M")
        except Exception:
            try:
                return datetime.strptime(t, "%H:%M %p")
            except Exception:
                return None

    sleep_hours = []
    moods = []
    gratitudes = []
    foods = []
    for e in entries:
        try:
            wake = parse_time(e['wake_up_time'])
            bed = parse_time(e['bedtime'])
            if wake and bed:
                delta = (wake - bed).seconds / 3600 if wake < bed else (24 - (bed.hour - wake.hour) - (bed.minute - wake.minute)/60)
                sleep_hours.append(delta)
        except Exception:
            pass
        moods.append(e.get('mood', ''))
        gratitudes.append(e.get('gratitude', ''))
        foods.append(e.get('meals', ''))

    avg_sleep = round(sum(sleep_hours)/len(sleep_hours), 2) if sleep_hours else 'N/A'
    mood_counts = Counter(moods)
    most_common_mood = mood_counts.most_common(1)[0][0] if mood_counts else 'N/A'
    gratitude_counts = Counter(gratitudes)
    most_common_gratitude = gratitude_counts.most_common(1)[0][0] if gratitude_counts else 'N/A'
    food_counts = Counter(foods)
    top_foods = ', '.join([f for f, _ in food_counts.most_common(3)]) if food_counts else 'N/A'

    html = f"""
    <html>
    <head>
        <meta charset='utf-8'>
        <title>Monthly Reflection Report: {month}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
            th, td {{ border: 1px solid #aaa; padding: 8px; text-align: center; }}
            th {{ background: #eee; }}
        </style>
    </head>
    <body>
        <h1>Monthly Reflection Report: {month}</h1>
        <h2>Summary</h2>
        <ul>
            <li><b>Average Sleep Hours:</b> {avg_sleep}</li>
            <li><b>Most Common Mood:</b> {most_common_mood}</li>
            <li><b>Top Foods:</b> {top_foods}</li>
            <li><b>Most Common Gratitude:</b> {most_common_gratitude}</li>
        </ul>
        <h2>Daily Highlights</h2>
        <table>
            <tr>
                <th>Date</th>
                <th>Mood</th>
                <th>Sleep (hrs)</th>
                <th>Highlight</th>
                <th>Gratitude</th>
                <th>Goal Progress</th>
            </tr>
    """
    for e in entries:
        wake = parse_time(e['wake_up_time'])
        bed = parse_time(e['bedtime'])
        if wake and bed:
            sleep = (wake - bed).seconds / 3600 if wake < bed else (24 - (bed.hour - wake.hour) - (bed.minute - wake.minute)/60)
            sleep = round(sleep, 2)
        else:
            sleep = 'N/A'
        html += f"""
            <tr>
                <td>{e.get('date', '')}</td>
                <td>{e.get('mood', '')}</td>
                <td>{sleep}</td>
                <td>{e.get('highlight', '')}</td>
                <td>{e.get('gratitude', '')}</td>
                <td>{e.get('goal_progress', '')}</td>
            </tr>
        """
    html += """
        </table>
    </body>
    </html>
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html) 