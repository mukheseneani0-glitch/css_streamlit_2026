# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 11:14:01 2026

@author: 22001691
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Dictionary of topics with explanations and quizzes
# Based on South African Physical Sciences curriculum for Grade 10-12
topics = {
    "Motion in One Dimension": {
        "grade": 10,
        "category": "Mechanics",
        "explanation": """
Motion in one dimension refers to movement along a straight line.
Key concepts:
- Position: Location relative to a reference point.
- Displacement: Change in position (vector quantity).
- Distance: Total path length (scalar).
- Average velocity: Displacement over time.
- Average speed: Distance over time.
- Acceleration: Change in velocity over time.
Equations:
- v = Δx / Δt
- a = Δv / Δt
- Use graphs: position-time, velocity-time, acceleration-time.
""",
        "quiz": [
            {
                "question": "What is the difference between distance and displacement?",
                "options": [
                    "Distance is a vector, displacement is scalar.",
                    "Distance is scalar, displacement is vector.",
                    "Both are vectors.",
                    "Both are scalars."
                ],
                "answer": 1
            },
            {
                "question": "If an object moves from position 0 to 10 m, then back to 5 m, what is the displacement?",
                "options": ["15 m", "10 m", "5 m", "20 m"],
                "answer": 2
            }
        ]
    },
    "Conservation of Energy": {
        "grade": 10,
        "category": "Mechanics",
        "explanation": """
Conservation of mechanical energy: In the absence of dissipative forces, total mechanical energy (kinetic + potential) is constant.
- Kinetic energy: KE = (1/2)mv²
- Gravitational potential energy: PE = mgh
- ME = KE + PE = constant
Applies to free fall, pendulums, etc.
""",
        "quiz": [
            {
                "question": "What is kinetic energy?",
                "options": [
                    "Energy due to position.",
                    "Energy due to motion.",
                    "Stored energy.",
                    "Thermal energy."
                ],
                "answer": 1
            },
            {
                "question": "In conservation of energy, what happens if friction is present?",
                "options": [
                    "Energy is conserved.",
                    "Energy is not conserved; some is lost as heat.",
                    "Energy increases.",
                    "No effect."
                ],
                "answer": 1
            }
        ]
    },
    "Transverse Waves": {
        "grade": 10,
        "category": "Waves, Sound & Light",
        "explanation": """
Transverse waves: Disturbance perpendicular to direction of propagation.
- Examples: Waves on a string, light.
- Terms: Amplitude (max displacement), wavelength (distance between crests), frequency (waves per second), period (time for one wave), speed (v = fλ).
Superposition: Waves add up.
""",
        "quiz": [
            {
                "question": "What is the relationship between speed, frequency, and wavelength?",
                "options": ["v = f / λ", "v = f λ", "v = λ / f", "v = f + λ"],
                "answer": 1
            },
            {
                "question": "In a transverse wave, the disturbance is:",
                "options": [
                    "Parallel to propagation.",
                    "Perpendicular to propagation.",
                    "Circular.",
                    "None."
                ],
                "answer": 1
            }
        ]
    },
    "Electrostatics": {
        "grade": 10,
        "category": "Electricity & Magnetism",
        "explanation": """
Electrostatics: Study of stationary charges.
- Two kinds of charge: Positive and negative.
- Like charges repel, unlike attract.
- Coulomb's law (Grade 11): F = k q1 q2 / r²
- Charge conservation and quantization.
""",
        "quiz": [
            {
                "question": "What happens when two positive charges are brought near?",
                "options": ["Attract", "Repel", "Nothing", "Merge"],
                "answer": 1
            },
            {
                "question": "Charge is measured in:",
                "options": ["Volts", "Amperes", "Coulombs", "Ohms"],
                "answer": 2
            }
        ]
    },
    "Atomic Structure": {
        "grade": 10,
        "category": "Matter & Materials",
        "explanation": """
Atomic structure:
- Atom: Protons (positive, nucleus), neutrons (neutral, nucleus), electrons (negative, orbits).
- Atomic number: Number of protons.
- Mass number: Protons + neutrons.
- Isotopes: Same protons, different neutrons.
- Electron configuration: e.g., 2.8.1 for sodium.
""",
        "quiz": [
            {
                "question": "Where are protons located?",
                "options": ["Orbit", "Nucleus", "Shell", "Outside"],
                "answer": 1
            },
            {
                "question": "What defines the element?",
                "options": ["Mass number", "Atomic number", "Neutrons", "Electrons"],
                "answer": 1
            }
        ]
    },
    "Chemical Bonding": {
        "grade": 10,
        "category": "Matter & Materials",
        "explanation": """
Chemical bonding:
- Covalent: Sharing electrons (e.g., H2).
- Ionic: Transfer electrons (e.g., NaCl).
- Metallic: Delocalized electrons in metals.
Bonds form to achieve stable electron configurations.
""",
        "quiz": [
            {
                "question": "In ionic bonding, electrons are:",
                "options": ["Shared", "Transferred", "Lost", "Gained equally"],
                "answer": 1
            },
            {
                "question": "Water (H2O) has what type of bond?",
                "options": ["Ionic", "Covalent", "Metallic", "Hydrogen"],
                "answer": 1
            }
        ]
    },
    "Reactions in Aqueous Solution": {
        "grade": 10,
        "category": "Chemical Change",
        "explanation": """
Reactions in water:
- Ions in solution (electrolytes).
- Conductivity: Due to mobile ions.
- Precipitation: Insoluble product forms.
- Types: Acid-base, redox, precipitation.
""",
        "quiz": [
            {
                "question": "What is an electrolyte?",
                "options": [
                    "Non-conductor",
                    "Solution that conducts electricity",
                    "Insulator",
                    "Pure water"
                ],
                "answer": 1
            },
            {
                "question": "Precipitation reaction produces:",
                "options": ["Gas", "Solid", "Liquid", "Plasma"],
                "answer": 1
            }
        ]
    },
    # Add more topics from Grade 11 and 12 as needed
    "Newton's Laws": {
        "grade": 11,
        "category": "Mechanics",
        "explanation": """
Newton's Laws:
1. Inertia: Object at rest stays, moving continues unless acted upon.
2. F = ma
3. Action-reaction pairs.
Applications: Free body diagrams, friction, gravity.
""",
        "quiz": [
            {
                "question": "Newton's first law is also known as:",
                "options": ["Acceleration", "Inertia", "Action-reaction", "Gravity"],
                "answer": 1
            }
        ]
    },
    # ... You can expand this dictionary with more topics
}

class PhysSciApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Physical Sciences Helper")
        self.root.geometry("800x600")

        # Welcome label
        welcome = tk.Label(root, text="Welcome to Physical Sciences Helper!\nSelect a topic to learn or take a quiz.", font=("Arial", 14))
        welcome.pack(pady=20)

        # Filter by grade
        self.grade_var = tk.StringVar(value="All")
        grade_label = tk.Label(root, text="Filter by Grade:")
        grade_label.pack()
        grade_options = ttk.Combobox(root, textvariable=self.grade_var, values=["All", 10, 11, 12])
        grade_options.pack()
        grade_options.bind("<<ComboboxSelected>>", self.update_topic_list)

        # Listbox for topics
        self.topic_listbox = tk.Listbox(root, height=15, width=50, font=("Arial", 12))
        self.topic_listbox.pack(pady=10)
        self.update_topic_list()

        # Buttons
        learn_btn = tk.Button(root, text="Learn Topic", command=self.learn_topic)
        learn_btn.pack(side=tk.LEFT, padx=20)
        quiz_btn = tk.Button(root, text="Take Quiz", command=self.take_quiz)
        quiz_btn.pack(side=tk.LEFT, padx=20)
        exit_btn = tk.Button(root, text="Exit", command=root.quit)
        exit_btn.pack(side=tk.LEFT, padx=20)

    def update_topic_list(self, event=None):
        selected_grade = self.grade_var.get()
        self.topic_listbox.delete(0, tk.END)
        for topic in sorted(topics.keys()):
            if selected_grade == "All" or topics[topic]["grade"] == int(selected_grade):
                self.topic_listbox.insert(tk.END, topic)

    def learn_topic(self):
        selected = self.topic_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection", "Please select a topic.")
            return
        topic = self.topic_listbox.get(selected[0])
        explanation = topics[topic]["explanation"]

        # New window for explanation
        learn_win = tk.Toplevel(self.root)
        learn_win.title(topic)
        learn_text = tk.Text(learn_win, wrap=tk.WORD, width=70, height=20, font=("Arial", 12))
        learn_text.insert(tk.END, explanation)
        learn_text.pack(pady=10, padx=10)
        learn_text.config(state=tk.DISABLED)  # Read-only

    def take_quiz(self):
        selected = self.topic_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection", "Please select a topic.")
            return
        topic = self.topic_listbox.get(selected[0])
        quiz_questions = topics[topic]["quiz"]
        if not quiz_questions:
            messagebox.showinfo("Quiz", "No quiz available for this topic.")
            return

        # Shuffle questions
        random.shuffle(quiz_questions)

        # Quiz window
        quiz_win = tk.Toplevel(self.root)
        quiz_win.title(f"Quiz: {topic}")
        score = [0]  # Mutable for inner function

        def next_question(index=0):
            if index >= len(quiz_questions):
                messagebox.showinfo("Quiz Complete", f"Your score: {score[0]} / {len(quiz_questions)}")
                quiz_win.destroy()
                return

            q = quiz_questions[index]
            for widget in quiz_win.winfo_children():
                widget.destroy()

            q_label = tk.Label(quiz_win, text=q["question"], font=("Arial", 12))
            q_label.pack(pady=10)

            var = tk.IntVar()
            for i, opt in enumerate(q["options"]):
                rb = tk.Radiobutton(quiz_win, text=opt, variable=var, value=i, font=("Arial", 10))
                rb.pack(anchor=tk.W)

            def submit():
                selected_ans = var.get()
                if selected_ans == q["answer"]:
                    score[0] += 1
                next_question(index + 1)

            submit_btn = tk.Button(quiz_win, text="Submit", command=submit)
            submit_btn.pack(pady=10)

        next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhysSciApp(root)
    root.mainloop()