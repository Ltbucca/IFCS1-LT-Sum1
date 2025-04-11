# IFCS1-Luke Tomlinson
## Summative 1: Task 2

# LINEAR EQUATION TEST with a Python Script ➕➖➕🐍🐍🐍

### Overview

The project provides a Python-based tool to test your knowledge and understanding of simple linear equations. This guide will help you set up and run the linear equation test on your local machine.

### Prerequisites

Before you begin, make sure the following are installed:

- **Python 3.13**

### Installation Steps

1. Install Python 3.x

   - Windows: Download from [python.org](https://www.python.org/downloads/windows/) 
   - macOS: Download from [python.org](https://www.python.org/downloads/mac-osx/)

   After downloading, run the installer and follow the on-screen instructions. Make sure to tick the box that says "Add Python to PATH" during installation.

### How to Run This Test 🏃‍♂🏃‍♂🏃‍♂

- Open a terminal or command prompt.
- Navigate to the folder where you saved the file.
- Run the script by typing:

```bash
python3 linear_equation_test.py
```

You should have the following tkinter GUI pop up:

- Windows:
![GUI Windows Setup](https://github.com/user-attachments/assets/71d0c42b-a07b-446c-8647-810fe496342a)
<br />

- macOS:
<img width="867" alt="Linear Equation Test App" src="https://github.com/user-attachments/assets/36eaafb9-4054-4b99-be3f-d330167237b2" />
<br />

   To save duplicating information moving forward the guide will concentrate on the mac version of the GUI but every action is the same in the Windows version.

  
To begin click on the `Start Test` button or hit the Return key:

<img width="543" alt="Screenshot 2025-04-11 at 19 30 37" src="https://github.com/user-attachments/assets/b003d650-3781-4ace-a915-dd629760e148" />


You should see a randomly generated simple equation pop-up:

<img width="695" alt="Equation Question 1" src="https://github.com/user-attachments/assets/9e35c0aa-0b97-4a1c-9869-cec57b52031f" />


Enter your best answer to two decimal places or less in the answer box: 

<img width="673" alt="Screenshot 2025-04-11 at 19 32 35" src="https://github.com/user-attachments/assets/dae86c5a-5db5-4e05-a3d5-4f86acea2852" />

Click `Calculate` button or hit the Return key to check your answer:

<img width="672" alt="Screenshot 2025-04-11 at 19 35 01" src="https://github.com/user-attachments/assets/bf9e0536-b312-43b7-ae67-e2919feed101" />

If the answer given is correct the following message is displayed for 4 seconds:

<img width="735" alt="Screenshot 2025-04-11 at 19 37 28" src="https://github.com/user-attachments/assets/cd61ac5c-34ca-4f9a-9bf0-ad85948c0211" />

If the answer proves to be incorrect the following message is displayed for 4 seconds:

<img width="794" alt="Screenshot 2025-04-11 at 19 36 33" src="https://github.com/user-attachments/assets/f2bba22b-0043-4593-a3d7-d56812ab24ba" />

If no valid answer is entered a message box will appear:

<img width="406" alt="Screenshot 2025-04-11 at 19 40 23" src="https://github.com/user-attachments/assets/e8724612-270b-4b3a-b05d-3c868a3f6424" />

After completing 5 questions a message box will appear with your final score:

<img width="712" alt="Screenshot 2025-04-11 at 19 43 00" src="https://github.com/user-attachments/assets/acd9d1ed-5d25-4453-b52a-d599bcba057c" />

To take another test just repeat the process:
<img width="828" alt="Screenshot 2025-04-11 at 19 44 42" src="https://github.com/user-attachments/assets/41cf2c20-881f-4b2c-91dc-f518414f640e" />

## Technical Documentation

### Project Structure

```
IFCS1-LT-Sum1/Summative-1-Task-1/
├── linear_equation_test_app.py        # Main script for linear equation test app
```

### linear_equation_test_app.py

This script creates a simple GUI-based test for solving basic linear equations using the tkinter module. It includes:

A DPI-awareness function for improved display scaling on Windows.

A main application class ```LinearEquationTest``` that initialises and displays the test window.

A Test frame class that manages question generation, input validation, scoring, and user feedback.

### Key Features:

### DPI Support
A helper function `set_dpi_awareness()` ensures clear visuals on high-resolution screens.

### GUI Construction with Tkinter
The application window is built using `tkinter.Tk`, and UI components (labels, buttons, entries) are arranged with grid layout.

### Linear Equation Quiz
Questions are randomly generated in one of three formats:<br />
`ax = b`<br />
`ax + c = b`<br />
`ax - c = b`<br />
The user is prompted to solve for `x`.

### Test Control
The user can start# the test with a button or by pressing the Enter key. Answers are checked for correctness, and feedback is shown with emojis for encouragement.

### Scoring System
Each correct answer increases the score, and the final percentage is displayed when the test is complete.

### Error Handling
The `check_answer()` method uses a `try/except` block to catch and handle invalid input (non-numeric answers).

### Example Flow:

1 - Launch the app.<br /><br />
2 - Click "Start Test" to begin.<br /><br />
3 - Solve the equation shown.<br /><br />
4 - Enter the answer rounded to two decimal places.<br /><br />
5 - Receive feedback and see progress.<br /><br />
6 - Final results are shown after completing the set number of questions (default: 5).

### Dependencies

- The script uses only Python’s built-in libraries: `tkinter` and `random`.
- No external packages or installations are required.

### Links

tkinter: [python.org](https://docs.python.org/3/library/tkinter.html).








