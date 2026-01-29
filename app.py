# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 11:40:41 2026

@author: 22001691
"""

# app.py
# Run locally: streamlit run app.py
# Deploy to Streamlit Cloud: Push to GitHub → connect at streamlit.io/cloud

import streamlit as st
import random

# Expanded topics dictionary
topics = {
    "Motion in One Dimension": {
        "grade": 10,
        "explanation": """
Motion along a straight line.

Key quantities:
- Position, displacement (Δx = vector), distance (scalar)
- Velocity (vector), speed (scalar)
- Acceleration (vector)

Equations:
v = u + at  
Δx = ut + ½at²  
v² = u² + 2aΔx  
(average velocity = Δx/Δt)

Use consistently: positive direction, signs for vectors.
        """,
        "quiz": [
            {"q": "Displacement is a __________ quantity.", 
             "options": ["scalar", "vector", "both", "neither"], "ans": 1},
            {"q": "If an object moves 10 m east then 6 m west, displacement is:", 
             "options": ["16 m east", "4 m east", "4 m west", "16 m west"], "ans": 1},
            {"q": "The slope of a position-time graph gives:", 
             "options": ["acceleration", "velocity", "displacement", "time"], "ans": 1},
            {"q": "If acceleration is constant and negative, velocity is:", 
             "options": ["increasing", "decreasing", "constant", "zero"], "ans": 1}
        ]
    },
    "Waves and Pulses": {
        "grade": 10,
        "explanation": """
Pulses and waves transfer energy without transferring matter.

- Pulse: single disturbance in a medium.
- Transverse pulse: particles move perpendicular to pulse direction.
- Amplitude: maximum displacement from rest position.
- Superposition: when pulses meet, displacements add (constructive/destructive).
- Transverse wave: continuous, has crests/troughs, wavelength (λ), frequency (f), period (T=1/f), speed v = fλ.

Pulses on string/spring: demonstrate reflection (fixed/free end), superposition.
        """,
        "quiz": [
            {"q": "A pulse is:", 
             "options": ["continuous wave", "single disturbance", "electromagnetic", "longitudinal only"], "ans": 1},
            {"q": "In a transverse pulse, particles move:", 
             "options": ["parallel to pulse direction", "perpendicular to pulse direction", "circular", "stationary"], "ans": 1},
            {"q": "When two identical pulses meet head-on and overlap perfectly, it is:", 
             "options": ["destructive interference", "constructive interference", "reflection", "refraction"], "ans": 1},
            {"q": "The principle that explains pulses passing through each other is:", 
             "options": ["reflection", "superposition", "diffraction", "polarisation"], "ans": 1}
        ]
    },
    "Newton's Laws of Motion": {
        "grade": 11,
        "explanation": """
1. Law of Inertia: Object at rest/motion stays unless net force acts.
2. F_net = ma (resultant force causes acceleration).
3. Action-reaction: Equal & opposite forces on different objects.

Free-body diagrams essential. Includes friction, weight (mg), normal force, tension.
        """,
        "quiz": [
            {"q": "Newton's First Law is the law of:", 
             "options": ["acceleration", "inertia", "action-reaction", "gravity"], "ans": 1},
            {"q": "If net force is zero, acceleration is:", 
             "options": ["increasing", "zero", "negative", "maximum"], "ans": 1},
            {"q": "The reaction force to gravity on you is:", 
             "options": ["your weight on Earth", "Earth's pull on you", "normal force from ground", "friction"], "ans": 0}
        ]
    },
    "Faraday's Law": {
        "grade": 11,
        "explanation": """
Electromagnetic induction: changing magnetic flux induces emf/current.

Faraday's Law: Induced emf (ε) = - rate of change of magnetic flux (ε = -ΔΦ/Δt).

Magnetic flux Φ = B·A·cosθ (B = field, A = area, θ = angle).

Induced current if circuit closed (Lenz's Law: opposes change).

Applications: generators, transformers, induction stoves.
Experiments: magnet in/out of coil, moving coil in field.
        """,
        "quiz": [
            {"q": "Faraday's Law relates induced emf to change in:", 
             "options": ["current", "magnetic flux", "voltage", "resistance"], "ans": 1},
            {"q": "The negative sign in Faraday's Law indicates direction according to:", 
             "options": ["Newton", "Coulomb", "Lenz", "Ohm"], "ans": 2},
            {"q": "If a magnet is pushed into a coil faster, induced emf is:", 
             "options": ["smaller", "larger", "zero", "constant"], "ans": 1},
            {"q": "Magnetic flux is maximum when angle between B and area is:", 
             "options": ["90°", "0°", "180°", "45°"], "ans": 1}
        ]
    },
    "Projectile Motion": {
        "grade": 12,
        "explanation": """
Motion under gravity only (no air resistance), horizontal velocity constant, vertical accelerated by g = 9.8 m/s² downward.

Independence: horizontal & vertical separate.

Horizontal: vx = constant = v cosθ, Δx = vx t

Vertical: vy = viy - gt, Δy = viy t - ½gt², vy² = viy² - 2gΔy

At max height: vy = 0  
Time to max height = vi sinθ / g  
Range (horizontal projectile from height): use vertical to find t, then Δx = vx t
        """,
        "quiz": [
            {"q": "In projectile motion, horizontal acceleration is:", 
             "options": ["g downward", "zero", "g upward", "variable"], "ans": 1},
            {"q": "Time to reach maximum height for angled launch is:", 
             "options": ["(vi sinθ)/g", "(vi cosθ)/g", "2(vi sinθ)/g", "vi/g"], "ans": 0},
            {"q": "At maximum height, vertical velocity is:", 
             "options": ["maximum", "zero", "negative", "vi sinθ"], "ans": 1},
            {"q": "The path of a projectile is:", 
             "options": ["straight line", "parabola", "circle", "hyperbola"], "ans": 1}
        ]
    },
    "Doppler Effect": {
        "grade": 12,
        "explanation": """
Change in observed frequency due to relative motion between source & observer.

For sound: f' = f (v ± vo) / (v ± vs)  
(v = speed of sound ≈ 340 m/s; + if approaching, - if receding)

Source moving toward listener → higher pitch  
Listener moving toward source → higher pitch

Light: red shift (galaxies moving away → expanding universe), blue shift (approaching).
        """,
        "quiz": [
            {"q": "When a source moves toward observer, observed frequency:", 
             "options": ["decreases", "increases", "stays same", "becomes zero"], "ans": 1},
            {"q": "The general Doppler formula for sound is:", 
             "options": ["f' = f (v / vs)", "f' = f (v ± vo)/(v ± vs)", "f' = f v", "f' = f / v"], "ans": 1},
            {"q": "Red shift in light from distant galaxies indicates:", 
             "options": ["universe contracting", "universe expanding", "galaxies stationary", "blue shift"], "ans": 1},
            {"q": "If observer moves away from stationary source, frequency:", 
             "options": ["increases", "decreases", "doubles", "halves"], "ans": 1}
        ]
    },
    # You can add more from previous versions if needed
}

st.title("Physical Sciences Helper – CAPS Grades 10–12")
st.markdown("Select grade and topic to study explanations or practice quizzes. Great for Limpopo learners!")

grade = st.selectbox("Filter by Grade", ["All", 10, 11, 12])

available_topics = [t for t, d in topics.items() if grade == "All" or d["grade"] == int(grade)]
if not available_topics:
    st.warning("No topics for selected grade yet.")
else:
    selected_topic = st.selectbox("Choose a Topic", available_topics)

    if selected_topic:
        data = topics[selected_topic]
        
        tab1, tab2 = st.tabs(["📖 Explanation", "🧪 Quiz (Multiple Choice)"])

        with tab1:
            st.markdown(data["explanation"])

        with tab2:
            questions = data.get("quiz", [])
            if not questions:
                st.info("No quiz questions available yet – check back soon!")
            else:
                random.shuffle(questions)
                score = 0
                total = len(questions)

                for i, q in enumerate(questions, 1):
                    st.subheader(f"Question {i} of {total}")
                    st.write(q["q"])
                    choice = st.radio("Select answer:", q["options"], index=None, key=f"{selected_topic}_{i}")

                    if choice is not None:
                        correct_opt = q["options"][q["ans"]]
                        if choice == correct_opt:
                            score += 1
                            st.success("Correct! ✅")
                        else:
                            st.error(f"Wrong. The correct answer is: **{correct_opt}**")

                if st.button("Calculate Score & Finish Quiz"):
                    percentage = (score / total) * 100 if total > 0 else 0
                    st.markdown(f"**Your score: {score} / {total}** ({percentage:.1f}%)")
                    if percentage >= 80:
                        st.balloons()
                        st.success("Excellent work! Keep it up 🔥")
                    elif percentage >= 50:
                        st.info("Good effort! Review the explanation and try again.")
                    else:
                        st.warning("Don't give up – revise the key concepts and retry!")

st.markdown("---")
st.caption("Built for CAPS Physical Sciences learners • Expand topics in the code as needed