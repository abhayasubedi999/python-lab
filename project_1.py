# You are Python tutor and you want to track students progress record. Make a GUI based python app with requirements:​

# Student information has to be stored in json file with at least attributes like name, email, heading of each exercises, project_1 & project_2. [There are 14 exercise given to student.]​

# UI should have name, email, progress, completed & pending exercise​

# There has to be option to enroll new student, edit/remove existing student, mark exercise as complete.​

# There should be option to send mail for sending for progress report.​

# There should also be option to load initial student name and email in bulk from csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants
EXERCISES = [f"Exercise_{i+1}" for i in range(14)]
DATA_FILE = "students.json"

# Load student data from JSON
try:
    with open(DATA_FILE, "r") as f:
        students = json.load(f)
except FileNotFoundError:
    students = {}


# Save student data to JSON
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


# GUI Class
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Progress Tracker")

        # Form fields
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()

        # Widgets
        ttk.Label(root, text="Name").grid(row=0, column=0)
        ttk.Entry(root, textvariable=self.name_var).grid(row=0, column=1)

        ttk.Label(root, text="Email").grid(row=1, column=0)
        ttk.Entry(root, textvariable=self.email_var).grid(row=1, column=1)

        ttk.Button(root, text="Enroll New Student", command=self.enroll_student).grid(
            row=2, column=0, columnspan=2
        )
        ttk.Button(root, text="Load Students from CSV", command=self.load_csv).grid(
            row=3, column=0, columnspan=2
        )

        self.student_listbox = tk.Listbox(root)
        self.student_listbox.grid(row=4, column=0, columnspan=2)
        self.student_listbox.bind("<<ListboxSelect>>", self.display_progress)

        self.progress_label = ttk.Label(root, text="")
        self.progress_label.grid(row=5, column=0, columnspan=2)

        self.exercise_checkboxes = []
        self.exercise_vars = []
        for i, ex in enumerate(EXERCISES):
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(root, text=ex, variable=var)
            chk.grid(row=6 + i // 2, column=i % 2)
            self.exercise_vars.append(var)
            self.exercise_checkboxes.append(chk)

        ttk.Button(root, text="Update Progress", command=self.update_progress).grid(
            row=13, column=0, columnspan=2
        )
        ttk.Button(root, text="Send Email Report", command=self.send_email).grid(
            row=14, column=0, columnspan=2
        )
        ttk.Button(root, text="Remove Student", command=self.remove_student).grid(
            row=15, column=0, columnspan=2
        )

        self.refresh_student_list()

    def enroll_student(self):
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        if not name or not email:
            messagebox.showwarning("Input Error", "Name and Email are required")
            return
        if email in students:
            messagebox.showwarning("Duplicate", "Student already exists")
            return
        students[email] = {
            "name": name,
            "email": email,
            "exercises": {ex: False for ex in EXERCISES},
            "project_1": False,
            "project_2": False,
        }
        save_data()
        self.refresh_student_list()

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    email = row["email"]
                    if email not in students:
                        students[email] = {
                            "name": row["name"],
                            "email": email,
                            "exercises": {ex: False for ex in EXERCISES},
                            "project_1": False,
                            "project_2": False,
                        }
            save_data()
            self.refresh_student_list()

    def refresh_student_list(self):
        self.student_listbox.delete(0, tk.END)
        for student in students.values():
            self.student_listbox.insert(
                tk.END, f"{student['name']} ({student['email']})"
            )

    def display_progress(self, event):
        selection = self.student_listbox.curselection()
        if selection:
            index = selection[0]
            email = list(students.keys())[index]
            data = students[email]
            completed = sum(data["exercises"].values())
            pending = 14 - completed
            self.progress_label.config(
                text=f"Completed: {completed}, Pending: {pending}"
            )
            for i, ex in enumerate(EXERCISES):
                self.exercise_vars[i].set(data["exercises"][ex])

    def update_progress(self):
        selection = self.student_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "No student selected")
            return
        index = selection[0]
        email = list(students.keys())[index]
        for i, ex in enumerate(EXERCISES):
            students[email]["exercises"][ex] = self.exercise_vars[i].get()
        save_data()
        self.display_progress(None)

    def remove_student(self):
        selection = self.student_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        email = list(students.keys())[index]
        del students[email]
        save_data()
        self.refresh_student_list()
        self.progress_label.config(text="")

    def send_email(self):
        selection = self.student_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "No student selected")
            return
        index = selection[0]
        email = list(students.keys())[index]
        student = students[email]

        msg = MIMEMultipart()
        msg["From"] = "your_email@example.com"
        msg["To"] = student["email"]
        msg["Subject"] = "Your Progress Report"

        body = f"Hello {student['name']},\n\nHere is your progress:\n"
        completed = sum(student["exercises"].values())
        body += f"Completed Exercises: {completed}/14\n"
        body += f"Pending Exercises: {14 - completed}\n"
        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP("smtp.example.com", 587) as server:
                server.starttls()
                server.login("your_email@example.com", "your_password")
                server.send_message(msg)
            messagebox.showinfo("Email Sent", "Progress report sent successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")


# Start app
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
