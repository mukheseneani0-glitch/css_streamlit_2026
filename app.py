# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 11:30:27 2026

@author: 22001691
"""

# Save this as app.py
# Then: pip install streamlit
# Run locally: streamlit run app.py
# Deploy: push to GitHub → connect to https://streamlit.io/cloud

import streamlit as st
import random

# Same topics data (you can expand this)
topics = {
    "Motion in One Dimension": {
        "grade": 10,
        "explanation": """
Motion in one dimension means movement along a straight line.

Key quantities:
- Position (x) — where the object is
- Displacement (Δx) — change in position (vector)
- Distance — total path travelled (scalar)
- Speed — distance/time (scalar)
- Velocity — displacement/time (vector)
- Acceleration — change in velocity/time (vector)

Important equations:
v = u + at  
Δx = ut + ½at²  
v² = u² + 2aΔx

Graphs help a lot:
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
        "explanation": """
Newton's Three Laws:

1. First Law (Inertia): An object continues in its state of rest or uniform motion unless a net external force acts on it.

2. Second Law: F_net = m × a

3. Third Law: Action-reaction pairs are equal and opposite.

Always draw free-body diagrams when solving problems!
        """,
        "quiz": [
            {"q": "Newton's First Law is also called the law of", 
             "options": ["acceleration", "inertia", "action-reaction", "gravity"], "ans": 1},
            {"q": "If F_net = 0, then acceleration is", 
             "options": ["increasing", "zero", "negative", "infinite"], "ans": 1},
        ]
    },
    # Add more topics the same way...
}

st.title("Physical Sciences Helper – Grade 10–12")
st.write("Select a topic to learn or test yourself!")

grade = st.selectbox("Filter by Grade", ["All", 10, 11, 12])

available_topics = [t for t, d in topics.items() if grade == "All" or d["grade"] == int(grade)]
selected_topic = st.selectbox("Choose Topic", available_topics)

if selected_topic:
    data = topics[selected_topic]
    
    tab1, tab2 = st.tabs(["📖 Explanation", "🧪 Quiz"])

    with tab1:
        st.markdown(data["explanation"])

    with tab2:
        questions = data.get("quiz", [])
        if not questions:
            st.info("No quiz yet for this topic.")
        else:
            random.shuffle(questions)
            score = 0
            for i, q in enumerate(questions, 1):
                st.subheader(f"Question {i}")
                st.write(q["q"])
                choice = st.radio("Choose:", q["options"], key=f"q{i}_{selected_topic}")
                if choice == q["options"][q["ans"]]:
                    score += 1
                    st.success("Correct!")
                elif choice is not None:
                    st.error(f"Wrong. Correct is: **{q['options'][q['ans']]}**")

            if st.button("Show Final Score"):
                st.balloons()
                st.success(f"You scored **{score} / {len(questions)}** !")

st.markdown("---")
st.caption("Made for learners in Limpopo & beyond • Add more topics in the code!")