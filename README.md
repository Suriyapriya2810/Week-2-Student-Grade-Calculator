# 📊 Week 2: Student Grade Calculator

## 📝 Project Overview
This project is a beginner-friendly Python console application designed to calculate student grades based on their marks. The program securely takes a student's name and marks, ensures the input falls within a valid range (0–100), determines the appropriate letter grade using logical conditions, and outputs a clean report featuring an encouraging message.

---

## 🛠️ Features
* **Input Validation:** Uses a `while` loop to guarantee that marks are numeric and fall strictly between 0 and 100.
* **Smart Decision Making:** Implements sequential `if-elif-else` conditional structures to evaluate grades accurately.
* **Encouraging Messages:** Provides personalized feedback depending on the student's performance category.

---

## 📐 Grading Logic Applied

The system processes student outcomes using the following numeric boundaries:

| Marks Range | Grade | Encouraging Message |
| :--- | :---: | :--- |
| **90 to 100** | **A** | Excellent work! You are a superstar! 🌟 |
| **80 to 89** | **B** | Very Good! Keep it up! 👍 |
| **65 to 79** | **C** | Good job! With a bit more effort, you can reach the top! 💪 |
| **50 to 64** | **D** | Good Try. Keep trying! 📚 |
| **35 to 49** | **D** | Passed. Let's work harder next time to improve! 📚 |
| **Below 35** | **F** | Don't be discouraged! Failures are stepping stones to success. ❤️ |

---

## 🚀 Setup & Execution Instructions

Follow these basic steps to run the application locally on your computer:

1. **Prerequisites:** Make sure you have Python installed on your machine.
2. **Download File:** Save the `grade_calculator.py` script into a folder.
3. **Open Terminal/Command Prompt:** Navigate to the folder where you saved the script.
4. **Run the Script:** Type the following command and press Enter:
   ```bash
   python grade_calculator.py
