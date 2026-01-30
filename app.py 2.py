# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 10:37:57 2026

@author: 22001691
"""

# app.py
import streamlit as st

# █████████ PHYSICAL SCIENCES TOPICS (CAPS Grades 10–12) █████████

CAPS_TOPICS = [
    {
        "id": 1,
        "title": "Matter and Materials",
        "grade": 10,
        "subject": "Chemistry",
        "notes": (
            "1. Classification of matter:\n"
            "   - Pure substances: elements (e.g., Fe, O₂) and compounds (e.g., H₂O, CO₂)\n"
            "   - Mixtures: homogeneous (air) and heterogeneous (sand + salt)\n\n"
            "2. States of matter:\n"
            "   - Solid: fixed shape and volume\n"
            "   - Liquid: fixed volume, no fixed shape\n"
            "   - Gas: no fixed shape or volume\n\n"
            "3. Atoms:\n"
            "   - Protons (+), neutrons (0), electrons (–)\n"
            "   - Atomic number (Z) = number of protons\n"
            "   - Mass number (A) = protons + neutrons\n\n"
            "4. Periodic table:\n"
            "   - Groups: vertical columns (similar properties)\n"
            "   - Periods: horizontal rows\n"
            "   - Metals, non-metals and metalloids"
        ),
        "study_tip": (
            "● Draw a mind map: matter → pure substances vs mixtures → elements/compounds → states.\n"
            "● Use flashcards for: element symbols, common ions (Na⁺, Cl⁻, SO₄²⁻), and periodic table groups 1–8, 0.\n"
            "● Relate examples to everyday life: tap water (mixture), pure gold (element), salt water (solution)."
        ),
        "homework": [
            "List 5 examples of elements and 5 examples of compounds you use at home.",
            "Define: element, compound, mixture. Give one example of each.",
            "Draw the periodic table layout and label groups 1, 2, 7 and 0."
        ],
        "classwork": [
            "In pairs, classify 10 common substances as elements, compounds or mixtures.",
            "Draw and label a simple diagram of an atom (protons, neutrons, electrons)."
        ],
        "quiz": [
            {
                "question": "An element is made of only one type of...",
                "options": ["Atom", "Molecule", "Ion"],
                "answer": 0
            },
            {
                "question": "What does the atomic number (Z) represent?",
                "options": ["Number of neutrons", "Number of protons", "Number of electrons"],
                "answer": 1
            },
            {
                "question": "Where are metals found on the periodic table?",
                "options": ["Right side", "Left side", "Centre only"],
                "answer": 1
            }
        ]
    },
    {
        "id": 2,
        "title": "Chemical Bonding",
        "grade": 10,
        "subject": "Chemistry",
        "notes": (
            "1. Ionic Bonding:\n"
            "   - Occurs between metal and non-metal\n"
            "   - Electrons are transferred\n"
            "   - Forms positive and negative ions (e.g., Na⁺, Cl⁻)\n\n"
            "2. Covalent Bonding:\n"
            "   - Occurs between non-metals\n"
            "   - Electrons are shared\n"
            "   - Form molecules (e.g., H₂O, CO₂)\n\n"
            "3. Metallic Bonding:\n"
            "   - Between metal atoms\n"
            "   - ‘Sea of electrons’ model\n\n"
            "4. Properties:\n"
            "   - Ionic compounds: high melting point, conduct when molten/dissolved\n"
            "   - Covalent compounds: low melting point, do not conduct electricity"
        ),
        "study_tip": (
            "● Draw dot-cross (Lewis) diagrams for simple ionic compounds (NaCl, MgO) and covalent molecules (H₂O, CO₂).\n"
            "● Compare ionic vs covalent: complete a table with columns: type of atoms, bonding, particles, properties.\n"
            "● Use the periodic table to predict which atoms will form positive or negative ions (lose or gain electrons)."
        ),
        "homework": [
            "Draw dot-cross diagrams for NaCl and H₂O.",
            "List 3 physical properties of ionic compounds and 3 of covalent compounds.",
            "Explain why metals are good conductors of electricity using the ‘sea of electrons’ model."
        ],
        "classwork": [
            "In groups, match the following to ionic or covalent: HCl, CO₂, NaBr, MgCl₂, O₂.",
            "Use balls and sticks (or paper) to build 3D models of simple molecules (H₂O, CO₂, NH₃)."
        ],
        "quiz": [
            {
                "question": "Which type of bond forms in NaCl?",
                "options": ["Ionic", "Covalent", "Metallic"],
                "answer": 0
            },
            {
                "question": "In covalent bonding, electrons are...",
                "options": ["Transferred", "Shared", "Lost"],
                "answer": 1
            },
            {
                "question": "Which of these is a typical property of ionic compounds?",
                "options": ["Low melting point", "High melting point", "Do not dissolve in water"],
                "answer": 1
            }
        ]
    },
    {
        "id": 3,
        "title": "Mechanics: Motion in 1D",
        "grade": 10,
        "subject": "Physics",
        "notes": (
            "1. Scalars vs vectors:\n"
            "   - Scalar: magnitude only (distance, speed, time, mass)\n"
            "   - Vector: magnitude and direction (displacement, velocity, acceleration, force)\n\n"
            "2. Definitions:\n"
            "   - Distance: total length of path (scalar, m)\n"
            "   - Displacement: change in position (vector, m)\n"
            "   - Speed: distance/time (scalar, m/s)\n"
            "   - Velocity: displacement/time (vector, m/s)\n"
            "   - Acceleration: rate of change of velocity (vector, m/s²)\n\n"
            "3. Equations of motion (constant acceleration):\n"
            "   ● v = u + at\n"
            "   ● s = ut + ½at²\n"
            "   ● v² = u² + 2as\n"
            "   where u = initial velocity, v = final velocity, a = acceleration, s = displacement, t = time"
        ),
        "study_tip": (
            "● Memorise the 3 equations of motion and practice using them in simple problems.\n"
            "● Draw position–time and velocity–time graphs for objects: at rest, moving with constant velocity, accelerating.\n"
            "● Use the gradient (slope) of v–t graph to find acceleration; area under v–t graph gives displacement."
        ),
        "homework": [
            "Define: distance, displacement, speed, velocity, acceleration (with units).",
            "A car starts from rest and accelerates at 3 m/s² for 10 s. Calculate its final velocity.",
            "Draw a velocity–time graph for an object that moves with constant velocity of 15 m/s for 10 s."
        ],
        "classwork": [
            "Solve 5 problems using the equations of motion (include one where the object is decelerating).",
            "In pairs, interpret motion graphs and write a short description of each motion scenario."
        ],
        "quiz": [
            {
                "question": "Which of these is a vector quantity?",
                "options": ["Distance", "Speed", "Displacement"],
                "answer": 2
            },
            {
                "question": "What does the gradient of a velocity–time graph represent?",
                "options": ["Velocity", "Acceleration", "Displacement"],
                "answer": 1
            },
            {
                "question": "A car accelerates from 10 m/s to 40 m/s in 6 seconds. Its acceleration is...",
                "options": ["5 m/s²", "6 m/s²", "7 m/s²"],
                "answer": 0
            }
        ]
    },
    {
        "id": 4,
        "title": "Energy",
        "grade": 10,
        "subject": "Physics",
        "notes": (
            "1. Forms of energy:\n"
            "   - Kinetic energy (Eₖ): energy of motion → Eₖ = ½mv²\n"
            "   - Gravitational potential energy (Eₚ): energy due to height → Eₚ = mgh\n"
            "   - Mechanical energy: Eₘ = Eₖ + Eₚ\n\n"
            "2. Law of conservation of mechanical energy:\n"
            "   - In the absence of friction and air resistance, total mechanical energy remains constant.\n"
            "   - Eₖ₁ + Eₚ₁ = Eₖ₂ + Eₚ₂\n\n"
            "3. Power:\n"
            "   - Power = energy / time (measured in watts, W)\n"
            "   - P = W / t"
        ),
        "study_tip": (
            "● Practice calculating Eₖ and Eₚ using the formulas.\n"
            "● Set up energy conservation problems: write Eₖ₁ + Eₚ₁ = Eₖ₂ + Eₚ₂ and solve.\n"
            "● Identify where Eₖ and Eₚ are maximum and minimum in real examples (e.g., roller coaster, falling object)."
        ),
        "homework": [
            "A 10 kg object is moving at 5 m/s. Calculate its kinetic energy.",
            "A 5 kg object is held at a height of 4 m above the ground. Calculate its gravitational potential energy (g ≈ 10 m/s²).",
            "A machine does 1 200 J of work in 30 s. Calculate its power."
        ],
        "classwork": [
            "Calculate the mechanical energy at the top and bottom of a simple pendulum (assume no friction).",
            "Work in groups to design a simple roller coaster track and label where Eₖ is max and Eₚ is max."
        ],
        "quiz": [
            {
                "question": "In which situation is kinetic energy changing into gravitational potential energy?",
                "options": ["A ball falling downwards", "A ball thrown upwards", "A ball at rest on the ground"],
                "answer": 1
            },
            {
                "question": "What is the unit of energy?",
                "options": ["Joule (J)", "Watt (W)", "Newton (N)"],
                "answer": 0
            },
            {
                "question": "A 2 kg object is moving at 10 m/s. Its kinetic energy is...",
                "options": ["20 J", "100 J", "200 J"],
                "answer": 1
            }
        ]
    }
    # Add more topics (Grades 11 & 12) below this line in the same format
]

# █████████ STREAMLIT APP LAYOUT █████████

st.set_page_config(page_title="Physical Sciences (Gr 10–12)", layout="centered")

st.title("Physical Sciences")
st.subheader("Grade 10 – 12 (CAPS Aligned)")

# Topic selection
topic_names = [f"{topic['title']} (Gr {topic['grade']} - {topic['subject']})" for topic in CAPS_TOPICS]
selected_topic_name = st.selectbox("🔍 Choose a topic", topic_names, index=0)

# Find the selected topic
selected_index = topic_names.index(selected_topic_name)
selected_topic = CAPS_TOPICS[selected_index]

# Display topic details
st.markdown("---")
st.header(f"📘 {selected_topic['title']}")
st.caption(f"Grade {selected_topic['grade']} | Subject: {selected_topic['subject']}")

# Notes
st.subheader("📝 Notes")
st.text_area("", selected_topic["notes"], height=200, disabled=True)

# Key study tips
st.subheader("🔑 Study Tips")
st.text_area("", selected_topic["study_tip"], height=120, disabled=True)

# Homework
st.subheader("🏠 Homework")
for i, hw in enumerate(selected_topic["homework"], 1):
    st.markdown(f"{i}. {hw}")

# Classwork
st.subheader("📘 Classwork")
for i, cw in enumerate(selected_topic["classwork"], 1):
    st.markdown(f"{i}. {cw}")

# Quiz section
st.subheader("🎯 Quiz")
quiz = selected_topic["quiz"]
quiz_user_answers = []

for i, q in enumerate(quiz):
    selected = st.radio(q["question"], q["options"], key=f"q{selected_topic['id']}_q{i}")
    quiz_user_answers.append(selected)

# Show quiz results
if st.button("📥 Submit Quiz"):
    st.markdown("### ✅ Quiz Results")
    score = 0
    for i, q in enumerate(quiz):
        correct = q["options"][q["answer"]]
        user = quiz_user_answers[i]
        if user == correct:
            st.markdown(f"**Q{i+1}**: {q['question']}")
            st.success(f"✅ {user}")
            score += 1
        else:
            st.markdown(f"**Q{i+1}**: {q['question']}")
            st.error(f"❌ Your answer: {user} (Correct: {correct})")
    
    st.markdown(f"**Score**: {score} / {len(quiz)}")