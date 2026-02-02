# DAILY HABIT TRACKER

#### Video Demo: (https://www.youtube.com/watch?v=baEWC4EqMcA)

#### Description:
**Habit Tracker** is a web application designed to help a user track daily habits. The goal is to perform a task (like "Reading" or "Running") every day and build up a "Streak". Habits are formed by daily dedication, and this tool helps with building and tracking new daily habits.

This version of the project focuses purely on the habit-tracking logic and data persistence, omitting user authentication to create a seamless, single-user experience.

### Features
- **Habit Management:** Create new habits with names and descriptions.
- **Daily Tracking:** A simple dashboard shows today's status. One click marks a habit as "Done" for the day.
- **Streaks:** The app dynamically calculates the "Current Streak" by analyzing the consecutive dates in the database. It also remembers the "All-time Longest Streak."
- **History Logs:** Users can drill down into any habit to see a full list of every date they completed it.

### Technical Summary
- **Backend:** Python with Flask.
- **Database:** SQLite (using the CS50 SQL library).
- **Frontend:** HTML5 with Jinja2 templating.
- **Logic:** The core complexity lies in `compute_current_streak` in `application.py`. It fetches all completion dates, sorts them, and iterates backward from "today" to determine how many consecutive days the habit has been maintained.

### Technical Implementation Details
- **Database Integrity:** The application uses two SQLite tables: habits for metadata and logs for individual completion records. A UNIQUE(habit_id, date) constraint on the logs table prevents duplicate entries for the same day, while foreign keys ensure data consistency.
- **Dynamic Streak Logic:** Streaks are calculated on-the-fly by the compute_current_streak function. It retrieves raw dates from the logs table, sorts them, and iterates backward from the present. If the most recent log is older than yesterday, the streak automatically resets to zero.
- **State Management:** The main route (/) aggregates data to render the dashboard. When a habit is marked "Done," the /done route inserts a log entry and immediately checks if the new streak beats the record, updating the longest_streak field in the habits table if necessary.

### Design Choices
- **Log-Based Tracking:** Instead of a fragile counter that just increments a number, I chose to store every completion as a timestamp row. This creates an unalterable audit trail and allows for accurate recalculation of streaks if data is ever modified.
- **Frictionless Experience:** Authentication was intentionally omitted to create a "local-first" tool. By removing login screens, the app creates a seamless, private environment where users can track habits instantly.
- **Server-Side Rendering:** To keep the codebase lightweight and reliable, the UI is rendered entirely via Flask and Jinja2. This ensures that the user always sees the database's "source of truth" without the complexity of client-side state management.
- **Defensive UX:** I implemented simple safeguards to prevent errors, such as backend checks to reject duplicate habit names and a native JavaScript confirmation dialog to prevent accidental deletions.

### Challenges & Lessons Learned
The hardest part of this project was definitely handling the dates correctly. I didn't realize how tricky it would be to calculate a "streak" until I started writing the algorithm. At first, my code wouldn't recognize that a streak was broken if I skipped a day. I had to rewrite the `compute_current_streak` function a few times to make sure it properly handled "yesterday." For example, if I check the app at 10 AM and haven't done my habit yet, the streak shouldn't be zero; it should still count yesterday's streak until the day is over.

I also learned a lot about SQL constraints. Early on, I had a bug where clicking the "Done" button twice would add two entries for the same day, messing up the counts. Adding the `UNIQUE` constraint in the database schema was a much better fix than just trying to handle it with Python `if` statements.

### Future Improvements
If I had more time to work on this, there are a few features I’d really like to add:
- **Data Visualization:** Right now, the history is just a text list. It would be cool to integrate a library like Chart.js to show a calendar view or a bar graph of my progress over the month.
- **User Accounts:** Since I kept this version single-user for simplicity, adding a login system would be the next logical step so I could host it online and let my friends use it too.
- **Timezones:** Currently, the app relies on the server's time. Making it respect the user's local timezone would be important if I ever deploy this to the web.

### Files
- `application.py`: The main server logic. Handles database connections, routing, and streak mathematics.
- `habits.db`: The SQLite database storing habits and logs.
- `templates/`: Contains the HTML files (`index.html`, `add.html`, `history.html`, `layout.html`) used to render the interface.
- `requirements.txt`: Lists the dependencies (`Flask`, `cs50`).

### How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `flask run`
3. Open the provided URL in your browser.
