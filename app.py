# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 11:24:24 2026

@author: 22001691
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random

# Topic data (expanded slightly, feel free to add more)
topics = {
    "Motion in One Dimension": {
        "grade": 10,
        "explanation": """Motion in one dimension means movement along a straight line.

Key quantities:
• Position (x) — where the object is
• Displacement (Δx) — change in position (vector)
• Distance — total path travelled (scalar)
• Speed — distance/time (scalar)
• Velocity — displacement/time (vector)
• Acceleration — change in velocity/time (vector)

Important equations:
v = u + at
Δx = ut + ½at²
v² = u² + 2aΔx
(Where u = initial velocity, v = final velocity)

Graphs:
• Position-time → slope = velocity
• Velocity-time → slope = acceleration, area = displacement
""",
        "quiz": [
            {"q": "Displacement is a __________ quantity.", 
             "options": ["scalar", "vector", "both", "neither"], "ans": 1},
            {"q": "If a car travels 100 km east then 40 km west, what is the displacement?", 
             "options": ["140 km", "60 km east", "60 km west", "100 km east"], "ans": 1},
        ]
    },
    "Newton's Laws of Motion": {
        "grade": 11,
        "explanation": """Newton's Three Laws:

1. First Law (Inertia): An object continues in its state of rest or uniform motion unless acted upon by a net external force.

2. Second Law: F_net = m × a  
   (The net force equals mass times acceleration)

3. Third Law: For every action there is an equal and opposite reaction.

Tips:
• Always draw free-body diagrams
• Weight = mg (downward)
• Normal force, friction, tension, applied force, etc.
""",
        "quiz": [
            {"q": "Newton's First Law is also called the law of", 
             "options": ["acceleration", "inertia", "action-reaction", "gravity"], "ans": 1},
            {"q": "If F_net = 0, then acceleration is", 
             "options": ["increasing", "zero", "negative", "infinite"], "ans": 1},
        ]
    },
    "Work, Energy & Power": {
        "grade": 10,
        "explanation": """Work (W) = F × Δx × cosθ   (Joules)

Energy:
• Kinetic energy: KE = ½mv²
• Gravitational potential energy: PE = mgh

Conservation of mechanical energy (no friction/air resistance):
KE_initial + PE_initial = KE_final + PE_final

Power = Work / time   (Watts = J/s)
""",
        "quiz": [
            {"q": "The unit of energy is", 
             "options": ["Newton", "Joule", "Watt", "Pascal"], "ans": 1},
            {"q": "When a ball falls freely, its potential energy is converted to", 
             "options": ["kinetic energy", "heat", "sound", "light"], "ans": 0},
        ]
    },
    # ← You can keep adding more topics here
}

class PhysSciHelper:
    def __init__(self, root):
        self.root = root
        self.root.title("Physical Sciences Helper - Limpopo Edition")
        self.root.geometry("780x580")
        self.root.resizable(True, True)

        tk.Label(root, text="Physical Sciences Study App", font=("Segoe UI", 16, "bold")).pack(pady=12)

        frame = tk.Frame(root)
        frame.pack(pady=8)

        tk.Label(frame, text="Select Grade:", font=("Segoe UI", 11)).pack(side=tk.LEFT, padx=8)
        self.grade_var = tk.StringVar(value="All")
        grade_combo = ttk.Combobox(frame, textvariable=self.grade_var, 
                                  values=["All", "10", "11", "12"], width=8, state="readonly")
        grade_combo.pack(side=tk.LEFT)
        grade_combo.bind("<<ComboboxSelected>>", self.refresh_topics)

        self.topic_list = tk.Listbox(root, height=14, width=45, font=("Segoe UI", 11), selectmode=tk.SINGLE)
        self.topic_list.pack(pady=12, padx=20, fill=tk.BOTH, expand=False)
        self.topic_list.bind("<<ListboxSelect>>", self.on_select)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text=" Read Explanation ", command=self.show_explanation,
                  width=18, font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=12)
        tk.Button(btn_frame, text=" Start Quiz ", command=self.start_quiz,
                  width=18, font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=12)
        tk.Button(btn_frame, text=" Exit ", command=root.destroy,
                  width=10, font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=12)

        self.refresh_topics()

    def refresh_topics(self, event=None):
        grade = self.grade_var.get()
        self.topic_list.delete(0, tk.END)
        for topic, data in sorted(topics.items()):
            if grade == "All" or str(data["grade"]) == grade:
                self.topic_list.insert(tk.END, f"{topic}  (Gr {data['grade']})")

    def get_selected_topic(self):
        selection = self.topic_list.curselection()
        if not selection:
            return None
        item = self.topic_list.get(selection[0])
        # Remove the (Gr xx) part
        return item.split("  (Gr")[0].strip()

    def show_explanation(self):
        topic = self.get_selected_topic()
        if not topic:
            messagebox.showinfo("No selection", "Please select a topic first.")
            return

        win = tk.Toplevel(self.root)
        win.title(topic)
        win.geometry("680x520")

        tk.Label(win, text=topic, font=("Segoe UI", 14, "bold")).pack(pady=10)

        text = scrolledtext.ScrolledText(win, wrap=tk.WORD, font=("Segoe UI", 11), padx=10, pady=10)
        text.insert(tk.END, topics[topic]["explanation"].strip())
        text.config(state="disabled")
        text.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

        tk.Button(win, text="Close", command=win.destroy, width=10).pack(pady=10)

    def start_quiz(self):
        topic = self.get_selected_topic()
        if not topic:
            messagebox.showinfo("No selection", "Please select a topic first.")
            return

        questions = topics[topic].get("quiz", [])
        if not questions:
            messagebox.showinfo("No quiz", "No quiz questions available for this topic yet.")
            return

        random.shuffle(questions)

        quiz_win = tk.Toplevel(self.root)
        quiz_win.title(f"Quiz: {topic}")
        quiz_win.geometry("680x480")

        score = [0]
        current_q = [0]

        def show_question():
            for widget in quiz_win.winfo_children():
                widget.destroy()

            if current_q[0] >= len(questions):
                tk.Label(quiz_win, text=f"Quiz complete!\nScore: {score[0]} / {len(questions)}",
                         font=("Segoe UI", 13, "bold")).pack(pady=40)
                tk.Button(quiz_win, text="Close", command=quiz_win.destroy, width=12).pack(pady=20)
                return

            q = questions[current_q[0]]

            tk.Label(quiz_win, text=f"Question {current_q[0]+1}/{len(questions)}", font=("Segoe UI", 11)).pack(pady=6)
            tk.Label(quiz_win, text=q["q"], font=("Segoe UI", 12), wraplength=620, justify="left").pack(pady=12)

            var = tk.IntVar(value=-1)
            for i, opt in enumerate(q["options"]):
                tk.Radiobutton(quiz_win, text=opt, variable=var, value=i, font=("Segoe UI", 11),
                               anchor="w", justify="left").pack(fill=tk.X, padx=40)

            def check_answer():
                ans = var.get()
                if ans == -1:
                    messagebox.showwarning("No choice", "Please select an option.")
                    return

                correct = q["ans"]
                if ans == correct:
                    score[0] += 1
                    feedback = "Correct!"
                    color = "green"
                else:
                    feedback = f"Wrong. Correct answer: {q['options'][correct]}"
                    color = "red"

                tk.Label(quiz_win, text=feedback, fg=color, font=("Segoe UI", 11, "bold")).pack(pady=12)

                tk.Button(quiz_win, text="Next →", command=lambda: [current_q.__setitem__(0, current_q[0]+1), show_question()],
                          width=12).pack(pady=10)

            tk.Button(quiz_win, text="Submit", command=check_answer, width=12).pack(pady=8)

        show_question()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = PhysSciHelper(root)
        root.mainloop()
    except Exception as e:
        print("Error starting app:", e)
        input("Press Enter to close...")