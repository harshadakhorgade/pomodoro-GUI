# Pomodoro Timer 🕒

## Overview
This project implements a **Pomodoro Timer** using Python and the `tkinter` library. It allows you to manage work and break intervals effectively using the popular **Pomodoro Technique**. 

The timer cycles between:
1. **Work sessions** (default: 25 minutes).
2. **Short breaks** (default: 5 minutes).
3. **Long breaks** (default: 20 minutes after 4 work sessions).

The interface dynamically updates the timer and provides visual cues for work, short breaks, and long breaks.

---

## Features 🚀
- **Work Timer:** Focused time for productivity.
- **Short Breaks:** Relaxation time after work sessions.
- **Long Breaks:** Extended rest after completing multiple cycles.
- **Visual Progress:** Marks (`✔`) appear after each completed work session.
- **Reset Timer:** Restart the cycle anytime.

---

## Installation 🛠️
1. Ensure you have Python installed (version 3.7+ recommended).
2. Install the required libraries:
   ```bash
   pip install tkinter
   ```
3. Save the code to a file named `main.py`.
4. Place a `tomato.png` image in the same directory as the script.

---

## Usage 🎯
1. Run the script:
   ```bash
   python main.py
   ```
2. The Pomodoro Timer window will open.
3. Click `Start` to begin the timer.
4. Use `Reset` to restart the timer.

---

## Code Structure 📂

### Constants
- `WORK_MIN`, `SHORT_BREAK_MIN`, `LONG_BREAK_MIN`: Define durations in minutes.
- Colors like `PINK`, `RED`, `GREEN`, and `YELLOW` enhance the UI.

### Functions
1. **`reset_timer`:** Resets the timer and progress marks.
2. **`start_timer`:** Starts the countdown for work or break sessions.
3. **`count_down`:** Manages the countdown and updates the UI dynamically.

### UI Components
- Built using `tkinter`:
  - **Labels** for headings and session types.
  - **Buttons** for starting and resetting the timer.
  - **Canvas** for the timer display with an image.

---

## Screenshots 🌟
### Main Screen
![Pomodoro Timer](tomato.png)  
*The timer with a "Tomato" theme!*

---

## The Pomodoro Technique ⏳
1. **Work for 25 minutes.** Focus entirely on the task.
2. **Take a 5-minute break.** Recharge your mind.
3. **Repeat.** After four sessions, take a 20-minute break.

This technique boosts productivity and prevents burnout.

---



---

### Built With ❤️ Using
- **Python** 🐍
- **tkinter** 🎨

Happy Productivity! 💻
