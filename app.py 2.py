# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 10:28:25 2026

@author: 22001691
"""

# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# CAPS Physical Sciences Topics (Grade 10–12)
topics = [
    {
        "id": 1,
        "title": "Matter and Materials",
        "grade": 10,
        "subject": "Chemistry",
        "notes": (
            "Matter is made of tiny particles. We classify matter into pure substances and mixtures.\n\n"
            "- Elements: cannot be broken down by chemical means.\n"
            "- Compounds: made of two or more elements chemically bonded.\n"
            "- Mixtures: can be homogeneous (uniform) or heterogeneous (not uniform).\n\n"
            "States of matter: solids, liquids, gases — explained by the kinetic molecular theory.\n\n"
            "Atoms: made of protons, neutrons, electrons. The periodic table shows elements with similar properties in groups."
        ),
        "key_to_study": (
            "Draw a mind map: types of matter, states of matter, and parts of the atom.\n"
            "Practice naming simple compounds and writing their formulae.\n"
            "Use flashcards for periodic table groups and common ions."
        ),
        "quiz": [
            {
                "question": "Which state of matter has particles with the least energy?",
                "options": ["Solid", "Liquid", "Gas"],
                "answer": 0  # index of correct answer
            },
            {
                "question": "What holds atoms together in a compound?",
                "options": ["Chemical bonds", "Gravity", "Wind"],
                "answer": 0
            },
            {
                "question": "An element cannot be broken down into simpler substances by chemical means. True or false?",
                "options": ["True", "False"],
                "answer": 0
            }
        ],
        "homework": [
            "List 5 examples of pure substances and 5 examples of mixtures you find at home.",
            "Draw and label a diagram of the water molecule (H₂O).",
            "Write the formula for: sodium chloride, water, carbon dioxide."
        ],
        "classwork": [
            "In small groups, classify 10 common substances into elements, compounds, or mixtures.",
            "Draw a simple kinetic model of solid, liquid, and gas."
        ]
    },
    {
        "id": 2,
        "title": "Chemical Bonding",
        "grade": 10,
        "subject": "Chemistry",
        "notes": (
            "Chemical bonds are attractions between atoms to form compounds.\n\n"
            "- Ionic bonding: metal gives electrons to non-metal (forms ions).\n"
            "- Covalent bonding: atoms share electrons (non-metal to non-metal).\n"
            "- Metallic bonding: metal atoms in a 'sea of electrons'.\n\n"
            "Atoms become stable when they have a full outer shell (like noble gases)."
        ),
        "key_to_study": (
            "Use Lewis diagrams to show bonding in simple compounds (e.g., NaCl, H₂O, CH₄).\n"
            "Compare properties of ionic (high mp, conducts when molten) and covalent (low mp, doesn't conduct) compounds.\n"
            "Practice drawing dot-cross diagrams."
        ),
        "quiz": [
            {
                "question": "Which type of bonding occurs in NaCl?",
                "options": ["Ionic", "Covalent", "Metallic"],
                "answer": 0
            },
            {
                "question": "In covalent bonding, atoms usually...",
                "options": ["Give electrons", "Share electrons", "Lose electrons"],
                "answer": 1
            },
            {
                "question": "Which compound consists of metal and non-metal atoms?",
                "options": ["CO₂", "NH₃", "MgO"],
                "answer": 2
            }
        ],
        "homework": [
            "Draw Lewis diagrams for: H₂O, CO₂, and NaCl.",
            "Explain the difference between ionic and covalent bonds in two sentences.",
            "Find the formula for magnesium oxide and aluminium chloride."
        ],
        "classwork": [
            "Build simple models (using circles or beads) to show ionic and covalent bonds.",
            "In pairs, match the bond type to the correct compound: NaCl, HCl, O₂."
        ]
    },
    {
        "id": 3,
        "title": "Mechanics: Motion in 1D",
        "grade": 10,
        "subject": "Physics",
        "notes": (
            "Motion in one dimension along a straight line.\n\n"
            "- Displacement: change in position (vector).\n"
            "- Distance: total path length (scalar).\n"
            "- Speed: distance/time (scalar).\n"
            "- Velocity: displacement/time (vector).\n"
            "- Acceleration: rate of change of velocity.\n\n"
            "Graphs: position vs. time, velocity vs. time, acceleration vs. time.\n\n"
            "Equations of motion (for constant acceleration):\n"
            "  v = u + at\n"
            "  s = ut + ½at²\n"
            "  v² = u² + 2as"
        ),
        "key_to_study": (
            "Learn the definitions and units of displacement, velocity, and acceleration.\n"
            "Practice drawing and interpreting position-time and velocity-time graphs.\n"
            "Use the equations of motion for uniform acceleration to solve problems."
        ),
        "quiz": [
            {
                "question": "Which is a vector quantity?",
                "options": ["Distance", "Speed", "Displacement"],
                "answer": 2
            },
            {
                "question": "What does the gradient of a velocity-time graph represent?",
                "options": ["Velocity", "Acceleration", "Displacement"],
                "answer": 1
            },
            {
                "question": "If a car accelerates from 10 m/s to 30 m/s in 5 s, its acceleration is...",
                "options": ["2 m/s²", "4 m/s²", "8 m/s²"],
                "answer": 1
            }
        ],
        "homework": [
            "Define: displacement, velocity, acceleration (with units).",
            "Calculate the acceleration of a car that goes from 20 m/s to 50 m/s in 10 s.",
            "Draw a velocity-time graph for a car that accelerates at 3 m/s² for 6 s, then moves at constant speed."
        ],
        "classwork": [
            "Solve word problems using the three equations of motion.",
            "Work in pairs to interpret graphs of motion from real-life examples."
        ]
    },
    # Add more topics for Grade 10, 11, and 12 (Chemistry & Physics) here...
]

@app.route('/')
def index():
    return render_template('index.html', topics=topics)

@app.route('/topic/<int:topic_id>')
def topic_detail(topic_id):
    topic = next((t for t in topics if t["id"] == topic_id), None)
    if topic is None:
        return "Topic not found", 404
    return render_template('topic.html', topic=topic)

@app.route('/quiz/<int:topic_id>', methods=['GET', 'POST'])
def quiz(topic_id):
    topic = next((t for t in topics if t["id"] == topic_id), None)
    if topic is None or "quiz" not in topic:
        return "Quiz not available", 404
    
    if request.method == 'POST':
        answers = request.form.getlist('answer')
        score = 0
        results = []
        for i, q in enumerate(topic['quiz']):
            user_ans = int(answers[i]) if i < len(answers) else -1
            correct = q['answer']
            correct_text = q['options'][correct]
            user_text = q['options'][user_ans] if 0 <= user_ans < len(q['options']) else "No answer"
            is_correct = user_ans == correct
            if is_correct:
                score += 1
            results.append({
                "question": q["question"],
                "user_answer": user_text,
                "correct_answer": correct_text,
                "is_correct": is_correct
            })
        return render_template('quiz_result.html', topic=topic, results=results, score=score)
    
    return render_template('quiz.html', topic=topic)

if __name__ == '__main__':
    app.run(debug=True)
