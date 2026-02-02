from cs50 import SQL
from flask import Flask, render_template, request, redirect
from datetime import date, timedelta

app = Flask(__name__)

db = SQL("sqlite:///habits.db")

db.execute("""
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    longest_streak INTEGER NOT NULL DEFAULT 0
)
""")
db.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    UNIQUE(habit_id, date),
    FOREIGN KEY(habit_id) REFERENCES habits(id)
)
""")
db.execute("PRAGMA foreign_keys = ON")

def compute_current_streak(dates):
    """Compute current streak of consecutive days."""
    if not dates:
        return 0

    sorted_dates = sorted(dates)
    last_date_str = sorted_dates[-1]

    # Check if streak is still active (completed today or yesterday)
    last_date = date.fromisoformat(last_date_str)
    today = date.today()

    # If the last time we did it was before yesterday, the streak is broken
    if last_date < today - timedelta(days=1):
        return 0

    streak = 1
    current = last_date
    date_set = set(sorted_dates)

    # Count backwards to find consecutive days
    while True:
        prev_day = current - timedelta(days=1)
        prev_str = prev_day.isoformat()
        if prev_str in date_set:
            streak += 1
            current = prev_day
        else:
            break
    return streak

@app.route("/")
def index():
    """Homepage: show all habits."""
    habits = db.execute("SELECT id, name, description, longest_streak FROM habits")

    habits_data = []
    today_str = date.today().isoformat()

    for habit in habits:
        hid = habit["id"]
        # Get all completion dates for this habit
        logs = db.execute("SELECT date FROM logs WHERE habit_id = ? ORDER BY date", hid)
        dates = [row["date"] for row in logs]

        current_streak = compute_current_streak(dates)
        done_today = today_str in dates

        habits_data.append({
            "id": hid,
            "name": habit["name"],
            "description": habit.get("description"),
            "current_streak": current_streak,
            "longest_streak": habit["longest_streak"],
            "done_today": done_today
        })

    return render_template("index.html", habits=habits_data)

@app.route("/add", methods=["GET", "POST"])
def add():
    """Add a new habit."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        if not name:
            return render_template("add.html", error="Habit name is required.")

        # Check for duplicates
        existing = db.execute("SELECT id FROM habits WHERE name = ?", name)
        if existing:
            return render_template("add.html", error="You already have a habit with that name.")

        db.execute("INSERT INTO habits (name, description) VALUES (?, ?)", name, description or None)
        return redirect("/")
    else:
        return render_template("add.html")

@app.route("/habit/<int:habit_id>")
def habit_history(habit_id):
    """Display history for a specific habit."""
    habit = db.execute("SELECT name, description, longest_streak FROM habits WHERE id = ?", habit_id)

    if not habit:
        return redirect("/")
    habit = habit[0]

    logs = db.execute("SELECT date FROM logs WHERE habit_id = ? ORDER BY date", habit_id)
    dates = [row["date"] for row in logs]

    current_streak = compute_current_streak(dates)
    total_done = len(dates)

    return render_template("history.html", habit_name=habit["name"], description=habit.get("description"),
                           dates=dates, current_streak=current_streak,
                           longest_streak=habit["longest_streak"], total_done=total_done)

@app.route("/done/<int:habit_id>")
def mark_done(habit_id):
    """Mark habit as done for today."""
    habit = db.execute("SELECT longest_streak FROM habits WHERE id = ?", habit_id)

    if not habit:
        return redirect("/")

    today_str = date.today().isoformat()

    # Ensure we don't double count today
    existing = db.execute("SELECT id FROM logs WHERE habit_id = ? AND date = ?", habit_id, today_str)
    if existing:
        return redirect("/")

    db.execute("INSERT INTO logs (habit_id, date) VALUES (?, ?)", habit_id, today_str)

    # Recalculate stats to see if we broke a record
    logs = db.execute("SELECT date FROM logs WHERE habit_id = ? ORDER BY date", habit_id)
    dates = [row["date"] for row in logs]
    new_current = compute_current_streak(dates)
    current_longest = habit[0]["longest_streak"]

    if new_current > current_longest:
        db.execute("UPDATE habits SET longest_streak = ? WHERE id = ?", new_current, habit_id)

    return redirect("/")

@app.route("/delete/<int:habit_id>")
def delete_habit(habit_id):
    """Delete a habit."""
    # Delete logs first (foreign key constraint)
    db.execute("DELETE FROM logs WHERE habit_id = ?", habit_id)
    db.execute("DELETE FROM habits WHERE id = ?", habit_id)
    return redirect("/")
