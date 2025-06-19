import os
import json
from datetime import datetime

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(data_dir, exist_ok=True)

def _get_month_file(date_str=None):
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    month = date_str[:7]  # 'YYYY-MM'
    return os.path.join(data_dir, f"{month}.json")

def save_entry(entry):
    file_path = _get_month_file(entry.get('date'))
    entries = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                entries = json.load(f)
            except json.JSONDecodeError:
                entries = []
    # Remove any existing entry for the same date (one entry per day)
    entries = [e for e in entries if e.get('date') != entry.get('date')]
    entries.append(entry)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

def load_entries(month=None):
    entries = []
    if month:
        file_path = os.path.join(data_dir, f"{month}.json")
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    entries = json.load(f)
                except json.JSONDecodeError:
                    entries = []
    else:
        # Load all entries from all month files
        for fname in os.listdir(data_dir):
            if fname.endswith('.json'):
                with open(os.path.join(data_dir, fname), 'r', encoding='utf-8') as f:
                    try:
                        entries.extend(json.load(f))
                    except json.JSONDecodeError:
                        continue
    return entries 