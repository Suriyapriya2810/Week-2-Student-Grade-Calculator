print("=== STUDENT GRADE CALCULATOR ===")

# Step 1: Get the student's name
name = input("Enter student name: ")

# Step 2: Get and validate the marks using a while loop
while True:
    marks_input = input("Enter marks (0-100): ")
    marks = float(marks_input)  # Convert the input text to a number
    
# Check if the marks are within the valid 0 to 100 range
    if marks >= 0 and marks <= 100:
        break  # Exit the loop if marks are valid
    else:
        print("❌ Invalid input! Marks must be between 0 and 100. Try again.")
# Step 3: Determine the grade and message using basic if-elif-else conditions

if marks >= 90:
    grade = "A"
    message = "Excellent work! You are a superstar! 🌟"
elif marks >= 80:
    grade = "B"
    message = "Very Good! Keep it up! 👍"
elif marks >= 65:
    grade = "C"
    message = "Good job! With a bit more effort, you can reach the top! 💪"
elif marks >= 50:
    grade = "D"
    message = "Good Try. keep Trying! 📚"
elif marks >= 35:
    grade = "D"
    message = "Passed. Let's work harder next time to improve! 📚"
else:
    grade = "F"
    message = "Don't be discouraged! Failures are stepping stones to success. Try again! ❤️"

# Step 4: Print the final formatted report

print("\n==============================")
print("📊 RESULT FOR:", name)
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
print("==============================")
